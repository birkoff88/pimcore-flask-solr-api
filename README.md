## Flask Solr Search API

A minimal Flask-based REST API connected to Apache Solr, deployed on Platform.sh.

### 🔗 Live Demo

[https://main-](https://main-<env>-<project>.platformsh.site)[-](https://main-<env>-<project>.platformsh.site)[.platformsh.site](https://main-<env>-<project>.platformsh.site)

### 🧠 Features

* Lightweight Flask API
* Index documents into Solr
* Perform full-text search
* Fully deployed and hosted on Platform.sh
* Dynamic environment detection via `PLATFORM_RELATIONSHIPS`

---

### 📦 Requirements

* Python 3.10+
* `Flask`, `requests`
* Platform.sh account (for deployment)

---

### 🚀 API Endpoints

#### `GET /`

Health check

```json
{
  "message": "Search API is running"
}
```

#### `POST /documents`

Index a new document into Solr

**Request:**

```json
{
  "id": "test1",
  "title": "Hello Solr"
}
```

**Response:**

```json
{
  "responseHeader": {
    "status": 0,
    ...
  }
}
```

#### `GET /search?q=term`

Search documents in Solr

**Response:**

```json
{
  "response": {
    "docs": [ ... ]
  }
}
```

---

### ⚙️ Deployment (Platform.sh)

1. Clone the repo
2. Run `platform project:set-remote` or `platform init`
3. Push to Platform.sh:

```bash
git push platform main
```

4. Done ✅

---

### 🧪 Local Development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Solr must be running locally at `http://localhost:8983/solr/mycore` for development mode.

---

### 📁 Project Structure

```
├── app.py
├── requirements.txt
├── .platform/
│   ├── .platform.app.yaml
│   ├── services.yaml
│   └── routes.yaml
```

---

### 🔐 Notes

* Flask binds to `0.0.0.0:8080` in deployment
* Solr core is assumed to be `mycore`
* Reads `PLATFORM_RELATIONSHIPS` for Solr config on Platform.sh

---

### 👨‍💻 Author

Boris Petrov – DevOps Engineer 
