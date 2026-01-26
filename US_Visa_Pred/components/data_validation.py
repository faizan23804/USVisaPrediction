import sys
import os
import pandas as pd
import numpy as np
import json
from pandas import DataFrame

from US_Visa_Pred.exceptions.exception import CustomException
from US_Visa_Pred.logger.logging import logging
from US_Visa_Pred.constant.pipeline_info import SCHEMA_FILE_PATH
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab, CatTargetDriftTab
from US_Visa_Pred.utils.main_utils import read_yaml_file, write_yaml_file
from US_Visa_Pred.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from US_Visa_Pred.entity.config_entity import DataValidationConfig

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="evidently")


class DataValidation:
    def __init__(self,data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self.schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise CustomException(e,sys)
        

    def validate_columns(self,dataframe:DataFrame) -> bool:
        try:
            status = len(dataframe.columns) == len(self.schema_config['columns'])
            logging.info(f"Are the Number of Columns Valid: {status}")
            return status
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def does_columns_exists(self, df: DataFrame) -> bool:
        try:
            dataframe_columns = df.columns
            missing_num_cols = []
            missing_cat_cols = []

            for column in self.schema_config["numerical_columns"]:
                if column not in dataframe_columns:
                    missing_num_cols.append(column)

            if len(missing_num_cols)>0:
                logging.info(f"Missing Numerical Column: {missing_num_cols}")

            for column in self.schema_config["categorical_columns"]:
                if column not in dataframe_columns:
                    missing_cat_cols.append(column)

            if len(missing_cat_cols)>0:
                logging.info(f"Missing Categorical Column: {missing_cat_cols}")

            return False if len(missing_cat_cols)>0 or len(missing_num_cols)>0 else True

        except Exception as e:
            raise CustomException(e,sys)
        

    @staticmethod
    def read_data(file_path) -> DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def detect_dataset_drift(self, base_df: DataFrame, current_df: DataFrame, ) -> bool:
        """
        Method Name :   detect_dataset_drift
        Description :   This method validates if drift is detected
        
        Output      :   Returns bool value based on validation results
        On Failure  :   Write an exception log and then raise an exception
        """
        try:

            os.makedirs(
            os.path.dirname(self.data_validation_config.drift_dashboard_file_path),
            exist_ok=True)
        
            dashboard_path = self.data_validation_config.drift_dashboard_file_path
            data_drift_dashboard = Dashboard(tabs=[DataDriftTab()])
            data_drift_dashboard.calculate(base_df, current_df)
            data_drift_dashboard.save(dashboard_path)

            data_drift_profile = Profile(sections=[DataDriftProfileSection()])
            data_drift_profile.calculate(base_df, current_df)

            report = data_drift_profile.json()
            json_report = json.loads(report)

            write_yaml_file(file_path=self.data_validation_config.drift_report_file_path, content=json_report)

            n_features = json_report["data_drift"]["data"]["metrics"]["n_features"]
            n_drifted_features = json_report["data_drift"]["data"]["metrics"]["n_drifted_features"]

            logging.info(f"{n_drifted_features}/{n_features} drift detected.")
            drift_status = json_report["data_drift"]["data"]["metrics"]["dataset_drift"]
            return drift_status
        except Exception as e:
            raise CustomException(e, sys) from e
        
    def initiate_data_validation(self) -> DataValidationArtifact:
        """
        Method Name :   initiate_data_validation
        Description :   This method initiates the data validation component for the pipeline
        
        Output      :   Returns bool value based on validation results
        On Failure  :   Write an exception log and then raise an exception
        """

        try:
            validation_error_msg = ""
            logging.info("Starting data validation")
            train_df, test_df = (DataValidation.read_data(file_path=self.data_ingestion_artifact.trained_file_path),
                                 DataValidation.read_data(file_path=self.data_ingestion_artifact.test_file_path))

            status = self.validate_columns(dataframe=train_df)
            logging.info(f"All required columns present in training dataframe: {status}")
            if not status:
                validation_error_msg += f"Columns are missing in training dataframe."
            status = self.validate_columns(dataframe=test_df)

            logging.info(f"All required columns present in testing dataframe: {status}")
            if not status:
                validation_error_msg += f"Columns are missing in test dataframe."

            status = self.does_columns_exists(df=train_df)

            if not status:
                validation_error_msg += f"Columns are missing in training dataframe."
            status = self.does_columns_exists(df=test_df)

            if not status:
                validation_error_msg += f"columns are missing in test dataframe."

            validation_status = len(validation_error_msg) == 0

            if validation_status:
                drift_status = self.detect_dataset_drift(train_df, test_df)
                if drift_status:
                    logging.info(f"Drift detected.")
                    validation_error_msg = "Drift detected"
                else:
                    validation_error_msg = "Drift not detected"
            else:
                logging.info(f"Validation_error: {validation_error_msg}")
                

            data_validation_artifact = DataValidationArtifact(
                validation_status=validation_status,
                message=validation_error_msg,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
                drift_dashboard_file_path=self.data_validation_config.drift_dashboard_file_path
            )

            logging.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise CustomException(e, sys) from e