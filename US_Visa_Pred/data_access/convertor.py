from US_Visa_Pred.configurations.mongodb_conn import *
from US_Visa_Pred.exceptions.exception import CustomException
from US_Visa_Pred.logger.logging import logging
from US_Visa_Pred.constant.pipeline_info import *
import pandas as pd
import numpy as np
import sys
from typing import Optional

class USdata():

    def __init__(self) -> None:

        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise CustomException(e,sys)
        
    def extract_collection_as_dataframe(self,collection_name: str, database_name:Optional[str]=None):

        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]

            df = pd.DataFrame(list(collection.find()))
            if '_id' in df.columns:
                df= df.drop('_id',axis=1)
            df.replace({'na':np.nan},inplace=True)
            return df
        except Exception as e:
            raise CustomException(e,sys)