import sys
sys.path.append('..')
from pymongo import MongoClient
from config.config import cfg
import random

class MongoDB():
    def __init__(self, host, db_name):
        self.host, self.db_name = host, db_name
        self.client = MongoClient(host)
        self.db = getattr(self.client, db_name)
    
    def get_collection(self, name: str):
        return getattr(self.db, name)

db = MongoDB(cfg.mongodb_host, cfg.db_name)

def get_numbers(collection, filter):
    return collection.count_documents(filter)

def get_distinct_val(collection, filter):
    return collection.distinct(filter)

def analysis(collection):
    arr = get_distinct_val(collection, "publisher_id")
    ret = {}
    for item in arr:
        ret.update({item: get_numbers(collection, {"publisher_id": item})})
    return ret

def get_random_uid(collection = db.get_collection('user_info')):
    uid = list(collection.find({}, {"uid": 1}))
    uid = map(lambda x: x.get('uid', None), uid)
    uid = list(uid)
    return random.choice(uid)
