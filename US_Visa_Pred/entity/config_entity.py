import os
import sys
from datetime import datetime
from US_Visa_Pred.constant.pipeline_info import *
from dataclasses import dataclass


timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    pipeline_name : str = PIPELINE_NAME
    artifact_dir : str = os.path.join(ARTIFACTS_DIR,timestamp)
    timestamp : str = timestamp

training_pipeline_config : TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    train_data_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    test_data_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name: str = DATA_INGESTION_COLLECTION_NAME


@dataclass
class DataValidationConfig:
      data_validation_dir: str = os.path.join(
        training_pipeline_config.artifact_dir,
        DATA_VALIDATION_DIR_NAME
    )
      drift_report_dir: str = os.path.join(
        data_validation_dir,
        DATA_VALIDATION_DRIFT_REPORT_DIR
    )
      drift_report_file_path: str = os.path.join(
        drift_report_dir,
        DATA_VALIDATION_DRIFT_REPORT_FILE_NAME
    )
      drift_dashboard_file_path: str = os.path.join(
        drift_report_dir,
        DATA_VALIDATION_DRIFT_DASHBOARD_NAME
    )


@dataclass
class DataTransformationConfig:
     data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_TRANSFORMATION_DIR_NAME)
     data_transformation_transformed_train_dir: str = os.path.join(
          data_transformation_dir,
          DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR_NAME,
          SCALED_TRAIN_FILE_NAME)
     data_transformation_transformed_test_dir: str = os.path.join(
          data_transformation_dir,
          DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR_NAME,
          SCALED_TEST_FILE_NAME)
     data_transformation_object_dir: str = os.path.join(
          data_transformation_dir,
          DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR_NAME,
          PREPROCESSING_OBJECT_FILE_NAME)
     

@dataclass
class ModelTrainerConfig:
     model_trainer_dir: str = os.path.join(training_pipeline_config.artifact_dir, MODEL_TRAINER_DIR_NAME)
     trained_model_dir: str = os.path.join(model_trainer_dir,MODEL_TRAINER_TRAINED_MODEL_DIR,MODEL_FILE_NAME)
     model_expected_score: float = TRAINED_MODEL_EXPECTED_SCORE
     model_trainer_config_file = MODEL_TRAINER_MODEL_CONFIG_FILE_PATH
    
     




