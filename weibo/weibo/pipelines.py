# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from db.mongo import db

collection = db.get_collection('weibo2')
class WeiboPipeline:

    def process_item(self, item, spider):
        try:
            collection.insert_one(item)
        except Exception:
            collection.delete_one({"article_id": item['article_id']})
            collection.insert_one(item)
        return item
