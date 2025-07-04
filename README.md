# Flask Solr Search API

A minimal Flask-based REST API connected to Apache Solr, deployed on Platform.sh.

## 🔗 Live Demo

[https://main-bvxea6i-hiaxa77qsgape.de-2.platformsh.site](https://main-bvxea6i-hiaxa77qsgape.de-2.platformsh.site)

## 🧠 Features

* Lightweight Flask API
* Index documents into Solr
* List all indexed documents
* Dynamic Solr URL detection via `PLATFORM_RELATIONSHIPS`
* Fully deployed via Platform.sh + GitHub Actions

## 🚀 API Endpoints

**POST /documents**
Index a document into Solr:

```
curl -X POST https://main-bvxea6i-hiaxa77qsgape.de-2.platformsh.site/documents \
  -H "Content-Type: application/json" \
  -d '{"id": "101", "text_t": "Pimcore integration test"}'
```

**GET /search?q=\*:**
List all indexed documents:

```
curl "https://main-bvxea6i-hiaxa77qsgape.de-2.platformsh.site/search?q=*:*"
```

🚧 Note: Due to the default Solr schema on Platform.sh, only predefined dynamic fields (like `text_t`) are indexed and searchable. Other fields may be ignored unless a custom schema is applied. This demo avoids schema customization for simplicity.

## ⚙️ Deployment (Platform.sh)

To deploy this project:

```bash
git clone https://github.com/birkoff88/pimcore-flask-solr-api.git
cd pimcore-flask-solr-api
platform project:set-remote hiaxa77qsgape
git push platform main
```
**Note:** Requires a [Platform.sh](https://platform.sh/) account and the [Platform.sh CLI](https://docs.platform.sh/development/cli.html) installed.


Live app: https://main-bvxea6i-hiaxa77qsgape.de-2.platformsh.site


CI/CD is handled by GitHub Actions.

## 🧪 Local Development

To run locally:

1. Start Solr in Docker:

```bash
docker run -d -p 8983:8983 --name my-solr solr
docker exec -it my-solr solr create_core -c collection1
```

2. Set up Python and Flask:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Solr will be available at [http://localhost:8983/solr/collection1](http://localhost:8983/solr/collection1)

## 📁 Project Structure

```
├── app.py
├── .github/
│   └── workflows/deploy.yml
├── .platform/
│   ├── services.yaml
│   ├── routes.yaml
│   └── local/
│       ├── .gitignore
│       ├── project.yaml
│       └── README.txt
├── .platform.app.yaml
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 👨‍💻 Author

Boris Petrov
DevOps Engineer | Platform.sh Demo Project
