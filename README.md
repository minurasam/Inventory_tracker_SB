# 📦 Inventory Tracker for Small Businesses

A fullstack web application for small businesses to manage and track their inventory with user authentication, transaction history, file uploads, and dashboard analytics — powered by **FastAPI**, **React**, and **AWS**.

---

## 🖼️ Architecture Diagram

![AWS Architecture](./A_diagram_of_an_Inventory_Tracker_application_arch.png)

---

## 🚀 Live Demo

> 🚧 Deployment in progress...

---

## 📚 Features

- 👥 Role-based Authentication (Admin, Staff)
- 📋 Product CRUD: add, update, and remove inventory
- 📤 Upload invoices & receipts to **AWS S3**
- 📊 Dashboard with insights: low-stock alerts, most moved items
- 🧾 Transaction history: stock-ins and stock-outs
- 📧 Email alerts via **AWS SES** *(optional)*
- ☁️ Hosted on **AWS EC2, S3, CloudFront, and RDS**

---

## 🛠️ Tech Stack

### 🔧 Backend
- [FastAPI](https://fastapi.tiangolo.com/) + Pydantic
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://aws.amazon.com/rds/)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for S3 integration
- JWT Authentication
- Dockerized API server (Gunicorn + Uvicorn)
- Unit tested with Pytest

### 💻 Frontend
- React + TypeScript
- Tailwind CSS + ShadCN UI
- React Query + Axios
- Chart.js / Recharts

### ☁️ AWS Services
- EC2 (Ubuntu instance for backend)
- RDS (PostgreSQL)
- S3 (invoices, receipts)
- CloudFront + S3 (frontend static hosting)
- IAM (secure roles & permissions)
- SES (optional: email alerts)

---

## ⚙️ Installation

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/inventory-tracker.git
cd inventory-tracker
```

### 2️⃣ Backend Setup

cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env

# Apply DB migrations
alembic upgrade head

# Run the server
uvicorn app.main:app --reload


### 3️⃣ Frontend Setup

cd frontend
npm install
npm run dev

### 🧪 Testing

# Run backend tests
cd backend
pytest