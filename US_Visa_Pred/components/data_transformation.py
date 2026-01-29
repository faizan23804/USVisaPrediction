import sys,os
import pandas as pd
import numpy as np


from US_Visa_Pred.exceptions.exception import CustomException
from US_Visa_Pred.logger.logging import logging
from US_Visa_Pred.constant.pipeline_info import *
from US_Visa_Pred.utils.main_utils import *
from US_Visa_Pred.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact
from US_Visa_Pred.entity.config_entity import DataTransformationConfig
from US_Visa_Pred.entity.estimator import TargetValue

from imblearn.combine import SMOTEENN
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder, PowerTransformer


class DataTransformation:
    def __init__(self,data_ingestion_artifact: DataIngestionArtifact,
                 data_transformation_config: DataTransformationConfig,
                 data_validation_artifact: DataValidationArtifact,):
                 
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config
            self.schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise CustomException(e,sys)
        
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def object_transformer(self,):
        try:
            logging.info("Got the Columns from the schema config")

            ed_order=["High School","Bachelor's","Master's","Doctorate"]
            binary_order = ['N', 'Y']
            categories = [
                ed_order,
                binary_order,
                binary_order,
                binary_order]

            scaler = StandardScaler()
            ohe_encoder = OneHotEncoder(drop='first', handle_unknown='ignore',sparse_output=False)
            or_encoder = OrdinalEncoder(categories=categories)

            logging.info("Encoders Initialized")

            ohe_columns = self.schema_config['ohe_columns']
            or_columns = self.schema_config['or_columns']
            transform_columns = self.schema_config['transform_columns']
            num_features = self.schema_config['num_features']

            logging.info("Initializing PowerTransformer")

            transform_pipe = Pipeline(steps=[
                ('tranform',PowerTransformer('yeo-johnson'))
            ])

            preprocessor = ColumnTransformer(
                [
                    ("onehot",ohe_encoder,ohe_columns),
                    ("ordinal",or_encoder,or_columns),
                    ("tranformer",transform_pipe,transform_columns),
                    ("scaled",scaler,num_features)
                ],remainder='passthrough'
            )

            logging.info("Preprocessor Object Created.")
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def initiate_data_transformer(self):
        try:
            if self.data_validation_artifact.validation_status:
                logging.info("Starting data transformation")
                preprocessor = self.object_transformer()

                train_df = DataTransformation.read_data(file_path=self.data_ingestion_artifact.trained_file_path)
                test_df = DataTransformation.read_data(file_path=self.data_ingestion_artifact.test_file_path)

                #Training Set FE

                input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN],axis = 1)
                target_feature_train_df = train_df[TARGET_COLUMN]

                logging.info("Got train features and test features of Training dataset")


                input_feature_train_df["company_age"] = CURRENT_YEAR-input_feature_train_df["yr_of_estab"]

                logging.info("Added company_age column to the Training dataset")

                drop_cols = self.schema_config["drop_columns"]              
                input_feature_train_df = drop_columns(df = input_feature_train_df, cols=drop_cols)

                logging.info("drop the columns in drop_cols of Training dataset")

                target_feature_train_df = target_feature_train_df.replace(TargetValue()._asdict())

                #Testing Set FE

                input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN],axis = 1)
                target_feature_test_df = test_df[TARGET_COLUMN]

                input_feature_test_df["company_age"] = CURRENT_YEAR-input_feature_test_df["yr_of_estab"]

                logging.info("Added company_age column to the Test dataset")

                drop_cols = self.schema_config["drop_columns"]
                input_feature_test_df = drop_columns(df = input_feature_test_df, cols=drop_cols)

                logging.info("drop the columns in drop_cols of Test dataset")

                target_feature_test_df = target_feature_test_df.replace(TargetValue()._asdict())

                logging.info("Got train features and test features of Testing dataset")

                #Applying Preprocessor Object
                
                logging.info(
                    "Applying preprocessing object on training dataframe and testing dataframe"
                )

                input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df)

                logging.info("Used the preprocessor object to transform the train features")

                input_feature_test_arr = preprocessor.transform(input_feature_test_df)

                logging.info("Used the preprocessor object to transform the test features")

                #Correcting class imbalance using Smoteenn

                logging.info("Applying SMOTEENN on Training dataset")

                smt = SMOTEENN(sampling_strategy="minority")

                input_feature_train_final, target_feature_train_final = smt.fit_resample(input_feature_train_arr, target_feature_train_df) # type: ignore
                    
                
                logging.info("Applied SMOTEENN on training dataset")

                # Test data untouched
                input_feature_test_final = input_feature_test_arr
                target_feature_test_final = target_feature_test_df
                
                
                train_arr = np.c_[
                    input_feature_train_final, np.array(target_feature_train_final)
                ]

                test_arr = np.c_[
                    input_feature_test_final, np.array(target_feature_test_final)
                ]

                save_object(self.data_transformation_config.data_transformation_object_dir, preprocessor)
                save_numpy_array_data(self.data_transformation_config.data_transformation_transformed_train_dir, array=train_arr)
                save_numpy_array_data(self.data_transformation_config.data_transformation_transformed_test_dir, array=test_arr)

                logging.info("Saved the preprocessor object")

                logging.info(
                    "Exited initiate_data_transformation method of Data_Transformation class"
                )

                data_transformation_artifact = DataTransformationArtifact(
                    preprocessor_object_file_path=self.data_transformation_config.data_transformation_object_dir,
                    trained_array_file_path=self.data_transformation_config.data_transformation_transformed_train_dir,
                    test_array_file_path=self.data_transformation_config.data_transformation_transformed_test_dir
                )
                return data_transformation_artifact
            else:
                raise Exception(self.data_validation_artifact.message)





            
        except Exception as e:
            raise CustomException(e,sys)














      