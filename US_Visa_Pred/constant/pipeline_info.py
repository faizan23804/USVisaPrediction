import os
import sys
import numpy as np
from datetime import date


DATABASE_NAME = "US_VISA_PREDICTION"
COLLECTION_NAME = "VISA_APPROVAL_DATA"
MONGO_DB_URL_KEY = "MongoDB_URL"

"""
Defining common constant variable for training pipeline

"""

TARGET_COLUMN:str = "case_status"
PIPELINE_NAME:str = "us_visa"
ARTIFACTS_DIR:str = "Artifacts"
FILE_NAME:str = "visaData.csv"
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCALED_TRAIN_FILE_NAME:str = "train.npy"
SCALED_TEST_FILE_NAME:str = "test.npy"

SCHEMA_FILE_PATH = os.path.join('config','schema.yaml')
SAVED_MODEL_DIR = os.path.join("saved_models")
MODEL_FILE_NAME = "model.pkl"

AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"


"""
Data Ingestion related constant start with Data_Ingestion VAR name.
"""
DATA_INGESTION_COLLECTION_NAME:str = "VISA_APPROVAL_DATA"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2

"""
Data Validation related constant start with Data_VALIDATION VAR name.
"""
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "report.yaml"
DATA_VALIDATION_DRIFT_DASHBOARD_NAME:str = "drift_dashboard.html"

"""
Data Transformation related constant start with Data_TRANSFORMATION VAR name.
"""
DATA_TRANSFORMATION_DIR_NAME:str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR_NAME:str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR_NAME:str = "preprocessing_object"


"""
Model Trainer related constant start with Model_Trainer VAR name.
"""
MODEL_TRAINER_DIR_NAME:str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR:str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME:str = "model.pkl"
TRAINED_MODEL_EXPECTED_SCORE:float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH = os.path.join("config","model.yaml")


"""
Model Evaluation related constant start with Model_Evaluation VAR name.
"""
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE:float = 0.2
MODEL_BUCKET_NAME = "usvisa-model2026-feb"
MODEL_PUSHER_S3_KEY = "model-registry"