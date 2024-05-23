from pymongo import MongoClient
from config.config import cfg

class DB():
    def __init__(self, host, db_name):
        self.host = host
        self.db_name = db_name
        self.client = MongoClient(host)
        self.db = getattr(self.client, self.db_name)
    
    def get_db(self):
        pass
    
    def get_collection(self, name):
        return getattr(self.db, name)

db = DB(cfg.mongodb_host, cfg.db_name)