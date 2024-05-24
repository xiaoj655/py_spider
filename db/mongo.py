import sys
sys.path.append('..')
from pymongo import MongoClient
from config.config import cfg

class MongoDB():
    def __init__(self, host, db_name):
        self.host, self.db_name = host, db_name
        self.client = MongoClient(host)
        self.db = getattr(self.client, db_name)
    
    def get_collection(self, name: str):
        return getattr(self.db, name)

db = MongoDB(cfg.mongodb_host, cfg.db_name)
