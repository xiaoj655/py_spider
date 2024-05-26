# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from db.mongo import db

class WeiboPipeline:
    collection = db.get_collection('weibo3')

    def process_item(self, item, spider):
        if(not item.get('article_id', None)):
            return item
        try:
            self.collection.insert_one(item)
        except Exception:
            self.collection.delete_one({"article_id": item['article_id']})
            self.collection.insert_one(item)
        return item

class WeiboUserInfoPipline:
    collection = db.get_collection('user_info')

    def process_item(self, item, spider):
        try:
            self.collection.insert_one(item)
        except Exception:
            self.collection.delete_one({"uid": item['uid']})
            self.collection.insert_one(item)
        return item
        