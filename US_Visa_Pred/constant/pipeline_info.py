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

SCHEMA_FILE_PATH = os.path.join('config','schema.yaml')
SAVED_MODEL_DIR = os.path.join("saved_models")
MODEL_FILE_NAME = "model.pkl"


"""
Data Ingestion related constant start with Data_Ingestion VAR name.
"""
DATA_INGESTION_COLLECTION_NAME:str = "VISA_APPROVAL_DATA"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2

"""
Data Ingestion related constant start with Data_Ingestion VAR name.
"""
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "report.yaml"
DATA_VALIDATION_DRIFT_DASHBOARD_NAME:str = "drift_dashboard.html"