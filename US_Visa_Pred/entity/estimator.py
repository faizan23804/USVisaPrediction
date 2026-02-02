import os,sys
import numpy as np
from pandas import DataFrame

from US_Visa_Pred.exceptions.exception import CustomException
from US_Visa_Pred.logger.logging import logging

class TargetValue:
    def __init__(self) -> None:
        self.Certified:int = 0
        self.Denied:int = 1
    def _asdict(self):
        return self.__dict__
    def reverse_map(self):
        mapping = self._asdict()
        return dict(zip(mapping.values(),mapping.keys()))
    

class USVisaModel:
    def __init__(self,preprocessing_object,trained_model_obejct):
        self.preprocessing_object = preprocessing_object
        self.trained_model_object = trained_model_obejct

    def predict(self, dataframe: DataFrame):
        try:
            transformed_features = self.preprocessing_object.transform(dataframe)
            return self.trained_model_object.predict(transformed_features)
        except Exception as e:
            raise CustomException(e,sys)
        
    def __repr__(self) -> str:
        return f"{type(self.trained_model_object).__name__}()"
    
    def __str__(self) -> str:
        return f"{type(self.trained_model_object).__name__}()"
    
    