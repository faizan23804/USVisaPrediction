import sys,os
import pandas as pd
import numpy as np
from pandas import DataFrame

from US_Visa_Pred.exceptions.exception import CustomException
from US_Visa_Pred.logger.logging import logging
from US_Visa_Pred.constant.pipeline_info import *
from US_Visa_Pred.utils.main_utils import *
from US_Visa_Pred.entity.artifact_entity import *
from US_Visa_Pred.entity.config_entity import ModelTrainerConfig
from US_Visa_Pred.entity.estimator import *

from neuro_mf import ModelFactory
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score,ConfusionMatrixDisplay,f1_score,precision_score,recall_score
from sklearn.model_selection import GridSearchCV


class ModelTrainer:
    def __init__(self,data_transformation_artifact: DataTransformationArtifact, model_trainer_config: ModelTrainerConfig) -> None:
        try:
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            raise CustomException(e,sys)


    def get_model_obj_and_report(self,train: np.array,test: np.array): # type: ignore

        try:
            logging.info("Using neuro_mf to get best model object and report")
            model_factory = ModelFactory(model_config_path = self.model_trainer_config.model_trainer_config_file)
            X_train, y_train, X_test, y_test = train[:,:-1], train[:,-1], test[:,:-1], test[:,-1]

            best_model_object = model_factory.get_best_model(X=X_train,
                                                           y=y_train,
                                                             base_accuracy=self.model_trainer_config.model_expected_score)
            model = best_model_object.best_model

            y_pred = model.predict(X_test)

            accuracy_sc = accuracy_score(y_test,y_pred)
            precision_sc = precision_score(y_test,y_pred)
            recall_sc = recall_score(y_test,y_pred)
            f1_sc = f1_score(y_test,y_pred)

            metric_artifact = ClassificatiomMetricArtifact(accuracy_score=accuracy_sc, precision_score=precision_sc, recall_score=recall_sc, f1_score=f1_sc) # type: ignore

            return best_model_object, metric_artifact
        
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def initiate_model_trainer(self):
        try:
            logging.info("Entered initiate_model_trainer method of ModelTrainer class")

            train_arr = load_numpy_array_data(file_path=self.data_transformation_artifact.trained_array_file_path)
            test_arr = load_numpy_array_data(file_path=self.data_transformation_artifact.test_array_file_path)

            best_model_object, metric_artifact = self.get_model_obj_and_report(train=train_arr,test=test_arr)

            preprocessing_obj = load_object(self.data_transformation_artifact.preprocessor_object_file_path)

            if best_model_object.best_score < self.model_trainer_config.model_expected_score:
                logging.info("No best model found with score more than base score")
                raise Exception(f"No Best Model Found with score < {best_model_object.best_score}")
            
            us_visa_model = USVisaModel(preprocessing_object=preprocessing_obj,trained_model_obejct=best_model_object.best_model)
            logging.info("Created usvisa model object with preprocessor and model")
            logging.info("Created best model file path.")
            save_object(self.model_trainer_config.trained_model_dir, us_visa_model)

            model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path=self.model_trainer_config.trained_model_dir, metric_artifact=metric_artifact)
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        
        except Exception as e:
            raise CustomException(e,sys)
    
