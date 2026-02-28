# US Visa prediction

📌 Project Overview

The US Visa Prediction System is an end-to-end Machine Learning + MLOps project that predicts whether a US visa application will be Approved or Denied based on user-provided information such as:

Continent

Education level

Job experience

Job training requirement

Number of employees

Company age

Region of employment

Wage details

Full-time position status

The system is built using FastAPI, follows a modular ML pipeline architecture, and is fully deployed on AWS using Docker, ECR, EC2, and GitHub Actions (CI/CD).

🔁 Pipeline Stages

Data Ingestion

Data Validation

Data Transformation

Model Training

Model Evaluation

Model Pusher (Upload to S3)

                 ┌───────────────────┐
                 │ MongoDB Atlas     │
                 │ (Raw Visa Data)   │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Data Ingestion    │
                 │ (Load to Pandas)  │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Data Validation   │
                 │ (Schema Checks,  │
                 │ Nulls, Drift)     │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Data Transformation│
                 │ (Encoding, Scaling│
                 │ Feature Engg.)    │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Model Trainer     │
                 │ (XGBoost / CatBoost)
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Model Evaluation  │
                 │ (F1, Precision,   │
                 │ Recall)           │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Model Pusher      │
                 │ (Upload to S3)    │
                 └───────────────────┘


☁️ Model Storage & Retrieval (AWS S3)

The best performing model is serialized using pickle

Uploaded to AWS S3

During prediction:

Model is fetched from S3

Loaded into memory

Used for inference


User Form Input (Web UI)
        │
        ▼
FastAPI Endpoint (/predict)
        │
        ▼
USvisaData → Pandas DataFrame
        │
        ▼
Load Model from S3
        │
        ▼
Model.predict()
        │
        ▼
Visa Approved / Not Approved


🖥️ Tech Stack
| Layer            | Technology                      |
| ---------------- | ------------------------------- |
| Language         | Python 3.8                      |
| Backend          | FastAPI                         |
| ML               | Scikit-learn, XGBoost, CatBoost |
| Database         | MongoDB Atlas                   |
| Model Storage    | AWS S3                          |
| Containerization | Docker                          |
| CI/CD            | GitHub Actions                  |
| Image Registry   | Amazon ECR                      |
| Deployment       | AWS EC2                         |



Project Structure
US_Visa_Pred/
│
├── constant/              # Constants & environment keys
├── entity/                # Config & artifact entities
├── components/            # ML pipeline components
├── pipeline/              # Training & prediction pipelines
├── cloud_storage/         # AWS S3 interaction logic
├── templates/             # HTML templates (UI)
├── static/                # CSS / JS files
│
├── app.py                 # FastAPI application
├── Dockerfile
├── requirements.txt
│
└── .github/workflows/     # CI/CD GitHub Actions YAML


🧪 How to Run Locally
1️⃣ Create Conda Environment
conda create -n visa python=3.8 -y
conda activate visa

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set Environment Variables
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster..."
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
export AWS_REGION=us-east-1


4️⃣ Run Application
python app.py

🔄 Git Commands
git add .
git commit -m "Updated US Visa Prediction Project"
git push origin main

🚢 AWS CI/CD Deployment (GitHub Actions)
Git Push
   │
   ▼
GitHub Actions (CI)
   │
   ▼
Docker Image Build
   │
   ▼
Push Image → Amazon ECR
   │
   ▼
EC2 (Self-Hosted Runner)
   │
   ▼
Docker Pull from ECR
   │
   ▼
Run FastAPI Container

🔐 AWS Setup Summary
IAM Permissions Required

AmazonEC2FullAccess

AmazonEC2ContainerRegistryFullAccess

GitHub Secrets

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
AWS_ECR_LOGIN_URI
ECR_REPOSITORY_NAME


🌍 Accessing the Application
[http://<EC2_PUBLIC_IPV4>:8000](http://<EC2_PUBLIC_IPV4>:8000)

