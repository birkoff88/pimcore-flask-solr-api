from flask import Flask, request, jsonify
import requests
import os
import base64
import json

app = Flask(__name__)

# Dynamically retrieve the Solr URL from PLATFORM_RELATIONSHIPS if running on Platform.sh
def get_solr_url():
    platform_rels = os.getenv("PLATFORM_RELATIONSHIPS")
    if platform_rels:
        try:
            decoded = base64.b64decode(platform_rels).decode("utf-8")
            relationships = json.loads(decoded)
            solr = relationships["solr"][0]
            host = solr["host"]
            port = solr["port"]
            path = solr.get("path", "/solr")
            print("Decoded PLATFORM_RELATIONSHIPS:", decoded)
            print("Final SOLR_URL:", f"http://{host}:{port}/{path.strip('/')}")
            # Ensure correct format (no double slashes)
            return f"http://{host}:{port}/{path.strip('/')}"
        except Exception as e:
            print("ERROR decoding PLATFORM_RELATIONSHIPS:", e)
            raise
    # Fallback for local dev
    return "http://localhost:8983/solr/collection1"

SOLR_URL = get_solr_url()



@app.route("/")
def home():
    return jsonify({
        "message": "Flask-Solr Search API is running!",
        "available_endpoints": {
            "/": "Health check (GET)",
            "/documents": "Index a document (POST)",
            "/search?q=term": "Full-text search (GET)"
        },
        "solr_url": SOLR_URL
    })

@app.route("/documents", methods=["POST"])
def index_document():
    doc = request.get_json()
    print("📄 Indexing document:", doc)
    response = requests.post(f"{SOLR_URL}/update/json/docs", json=doc, params={"commit": "true"})
    print("📥 Solr index response:", response.text)
    return jsonify(response.json()), response.status_code


@app.route("/search")
def search():
    query = request.args.get("q", "*:*")
    params = {"q": query, "wt": "json"}
    print("🔎 Search query:", query)
    print("📡 Requesting Solr at:", f"{SOLR_URL}/select")
    print("🧾 With params:", params)
    response = requests.get(f"{SOLR_URL}/select", params=params)
    print("📬 Raw Solr response:", response.text)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
