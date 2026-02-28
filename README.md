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
| Layer            | Directory / File     | Responsibility                                                      |
| ---------------- | -------------------- | ------------------------------------------------------------------- |
| Configuration    | `constant/`          | Environment keys, global constants, pipeline configs                |
| Data Contracts   | `entity/`            | Config entities, artifact schemas, dataclasses                      |
| Data Pipeline    | `components/`        | Ingestion, validation, transformation, training, evaluation, pusher |
| Orchestration    | `pipeline/`          | Training & prediction pipeline execution                            |
| Cloud Storage    | `cloud_storage/`     | AWS S3 upload/download logic                                        |
| Web Templates    | `templates/`         | HTML files for Web UI                                               |
| Static Assets    | `static/`            | CSS, JavaScript, images                                             |
| API Layer        | `app.py`             | FastAPI application & endpoints                                     |
| Containerization | `Dockerfile`         | Docker image definition                                             |
| Dependencies     | `requirements.txt`   | Python package dependencies                                         |
| CI/CD            | `.github/workflows/` | GitHub Actions automation                                           |


## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```


## How to run?

```bash
conda create -n venv python=3.10 -y
```

```bash
conda activate venv/
```

```bash
pip install -r requirements.txt
```

## Workflow:

1. constants
2. entity
3. components
4. pipeline
5. Main file



### Export the  environment variable
```bash


export MONGODB_URL="mongodb+srv://<username>:<password>...."

export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>


```


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 9846********.dkr.ecr.us-east-1.amazonaws.com/us-visa

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_REGION
   - AWS_ECR_LOGIN_URI
   - ECR_REPOSITORY_NAME


#  Accessing the Application
 - [http://<EC2_PUBLIC_IPV4>:8000].



