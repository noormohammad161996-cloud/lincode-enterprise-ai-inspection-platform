# 🚀 Lincode Enterprise AI Inspection Platform

A production-style AI-powered inspection platform built using FastAPI, PostgreSQL, and Microservices Architecture.

---

# 📌 Project Overview

This project simulates an industrial AI inspection system where users upload machine part images, the backend communicates with an AI Prediction Service, and the prediction is stored in PostgreSQL.

The project is designed following real-world DevOps and Microservices architecture.

---

# 🏗 Architecture

```
                User
                  │
                  ▼
          FastAPI Backend
                  │
      Upload Image & API
                  │
                  ▼
         AI Prediction Service
                  │
                  ▼
           PostgreSQL Database
```

---

# 🚀 Features

- Image Upload API
- AI Prediction Service
- REST APIs
- PostgreSQL Integration
- File Upload Validation
- Automatic Prediction Storage
- Swagger Documentation
- Microservices Communication
- Production-ready Project Structure

---

# 🛠 Tech Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

### Database

- PostgreSQL

### AI Service

- FastAPI
- Dummy Prediction Engine

### DevOps

- Git
- GitHub

---

# 📂 Project Structure

```
lincode-enterprise-devops/
│
├── backend/
│
├── ai-service/
│
├── frontend/
│
├── docker/
│
├── sample-images/
│
└── README.md
```

---

# ⚙ Backend APIs

## Health

```
GET /health/
```

---

## Upload Image

```
POST /api/v1/inspection/upload
```

Uploads an image and stores AI prediction.

---

## Get All Inspections

```
GET /api/v1/inspection/
```

---

## Get Inspection

```
GET /api/v1/inspection/{id}
```

---

## Delete Inspection

```
DELETE /api/v1/inspection/{id}
```

---

# 🤖 AI Prediction Service

```
POST /predict
```

Input

```json
{
    "filename":"bearing-good-01.jpg"
}
```

Example Response

```json
{
    "prediction":"Good",
    "confidence":97.83
}
```

---

# 📸 Sample Images

```
bearing-good-01.jpg
bearing-good-02.jpg
bearing-defect-01.jpg
gear-crack-01.jpg
steel-defect-01.jpg
```

---

# ▶ Run Backend

```
cd backend

source venv/bin/activate

uvicorn app.main:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# ▶ Run AI Service

```
cd ai-service

source venv/bin/activate

uvicorn app:app --reload --port 8001
```

Swagger

```
http://127.0.0.1:8001/docs
```

---

# ✅ Current Progress

- ✔ Backend API
- ✔ PostgreSQL Integration
- ✔ CRUD Operations
- ✔ Image Upload
- ✔ AI Prediction Service
- ✔ Backend ↔ AI Communication
- ✔ Prediction Persistence

---

# 🚀 Upcoming Features

- Docker
- Docker Compose
- Jenkins CI/CD
- Kubernetes
- Prometheus
- Grafana
- GitHub Actions

---

# 👨‍💻 Author

**Noor Mohammad**

GitHub:

https://github.com/noormohammad161996-cloud