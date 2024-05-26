from typing import Iterable
import scrapy
import os
import json
import time
from db.mongo import get_random_uid
import random


class Item:
    uid:                str
    screen_name:        str
    description:        str
    followers_count:    int

def get_item_entries(x):
    _x = x['user']
    return {
        "uid":              _x.get('idstr', None),
        "screen_name":      _x.get('screen_name', None),
        "description":      _x.get('description', None),
        "followers_count":  _x.get('followers_count', 0),
        "verified_reason":  _x.get('verified_reason', None),
        "desc1":            x.get('desc1', None),
        "desc2":            x.get("desc2", None)
    }

class SideDetailSpider(scrapy.Spider):
    name = "side_detail"
    allowed_domains = ["weibo.com"]
    # uid = ['1755370981']
    start_urls = ["https://weibo.com"]
    custom_settings = {
        "ITEM_PIPLINES": {
            "weibo.piplines.WeiboUserInfoPipline": 999
        }
    }
    cnt = 0

    def start_requests(self):
        for item in [f'https://weibo.com/ajax/profile/sidedetail?uid=1645773865']:
            yield scrapy.Request(item, callback=self.parse)
                    

    def parse(self, response):
        rep = json.loads(response.body)
        recom_users = rep['data']['recom']['recomm_users']
        items = map(lambda x: get_item_entries(x), recom_users)
        for item in items:
            yield item
        
        time.sleep(21)
        if(random.randint(1,10)>7):
            time.sleep(15)
        u = get_random_uid()
        self.cnt += 1
        try:
            yield scrapy.Request(f'https://weibo.com/ajax/profile/sidedetail?uid={u}', \
                            callback=self.parse)
            print(f'用户{u}, 第{self.cnt}个')
        except Exception:
            yield scrapy.Request(f'https://weibo.com/ajax/profile/sidedetail?uid={u}', \
                            callback=self.parse)
            print(f'用户{u}, 第{self.cnt}个')

