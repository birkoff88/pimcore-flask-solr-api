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
            print("Decoded PLATFORM_RELATIONSHIPS:", decoded)  # <-- добави това
            relationships = json.loads(decoded)
            solr = relationships["solr"][0]
            host = solr["host"]
            port = solr["port"]
            path = solr.get("path", "/solr")
            return f"http://{host}:{port}{path}/mycore"
        except Exception as e:
            print("ERROR decoding PLATFORM_RELATIONSHIPS:", e)
            raise
    # Fallback for local dev
    return "http://localhost:8983/solr/mycore"

SOLR_URL = get_solr_url()

@app.route("/")
def home():
    return jsonify({"message": "Search API is running"})

@app.route("/documents", methods=["POST"])
def index_document():
    # Accepts JSON document and sends it to Solr for indexing
    doc = request.get_json()
    response = requests.post(f"{SOLR_URL}/update/json/docs", json=doc, params={"commit": "true"})
    return jsonify(response.json()), response.status_code

@app.route("/search")
def search():
    # Performs a full-text search against Solr using query parameter ?q=
    query = request.args.get("q", "*:*")
    params = {"q": query, "wt": "json"}
    response = requests.get(f"{SOLR_URL}/select", params=params)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
