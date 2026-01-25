import sys
import os
import certifi
from US_Visa_Pred.exceptions.exception import CustomException
from US_Visa_Pred.logger.logging import logging
from US_Visa_Pred.constant.pipeline_info import *
import pymongo

ca = certifi.where()

class MongoDBClient:

    client=None

    def __init__(self,database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGO_DB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Enviroment key {MONGO_DB_URL_KEY} is not set")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAfile=ca)
                self.client = MongoDBClient.client
                self.database = self.client[database_name]
                self.database_name = database_name

                logging.info("MongoDB Connection Successfull")

        except Exception as e:
            raise CustomException(e,sys)