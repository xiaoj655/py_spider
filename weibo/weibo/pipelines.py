# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sys
sys.path.append('..')
from mongo.interface import db

collection = db.get_collection('weibo')

class WeiboPipeline:
    def process_item(self, item, spider):
        collection.insert_one(item)
        return item
