import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging import logger
from networksecurity.exception.exception import NetworkSecurityException
# __all__ = ["NetworkSecurityException"]

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def cv_to_json_convert(self, file_path):
        try: 
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_to_mongodb(self, records, db_name, collection_name):
        try:
            self.db_name = db_name
            self.collection_name = collection_name
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.db_name = self.mongo_client[self.db_name]

            self.collection_name = self.db_name[self.collection_name]
            self.collection_name.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "nathiskaralways_db_user"
    COLLECTION = "NetworkData"
    networkobj=NetworkDataExtract()
    records = networkobj.cv_to_json_convert(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_to_mongodb(records=records, db_name=DATABASE, collection_name=COLLECTION)
    print(no_of_records)