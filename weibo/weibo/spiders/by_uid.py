from typing import Iterable
import requests
import scrapy
import scrapy.exceptions
from config.config import cfg
from weibo.tools import common
from lxml import etree
import time
import random

class Item():
    publisher_id:       int  = None
    content:            str  = None
    publish_at:         str  # %Y-%m-%d %H-%M
    publish_tool:       str = '无'
    is_forward:         bool
    forward_who:        str
    img_url_list:       list[str]
    footer:             list[int] # like, forward, comment
    article_id:         str # customer field, used to remove duplicates  = publisher_id + blog_id

class ByUidSpider(scrapy.Spider):
    name = "by_uid"
    allowed_domains = ["weibo.cn"]
    max_page = cfg.max_page
    start_urls = [f"https://weibo.cn/{x}/profile" for x in cfg.uid]
    current_uid = None

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, callback=self.initial)
        
    def start_requests(self):
        for x in cfg.uid:
            self.current_uid = x
            # yield scrapy.Request(f"https://weibo.cn/{x}/profile")
            yield scrapy.Request('https://weibo.cn/1858002662/profile?page=17')

    # set max page
    def initial(self, response):
        _max_page = response.xpath("//div[@id='pagelist']//div/text()").extract()
        _max_page = int(_max_page[1].split('/')[-1][:-1])
        self.max_page = min(_max_page, self.max_page)
        self.parse(response)
    
    def parse(self, response):
        # get all content divs
        contents = response.xpath("//div[@class='c']")[:-1]
        article_id = map(lambda x: x.xpath('./@id').extract()[0][2:], contents)
        content = map(lambda x: ''.join(x.xpath("./div/span[@class='ctt']/text()").extract()), contents)
        is_forward = map(lambda x: common.is_forward(x), contents)
        footer = map(lambda x: common.get_footer(x), contents)
        publish_at = map(lambda x: common.get_publish_time(x), contents)
        publish_tool = map(lambda x: common.get_publish_tool(x), contents)
        img_url_list = []

        for x in contents:
            hrefs = x.xpath('./div')[0].xpath('./a/@href').extract()
            # 先判断有没有 组图 a链接
            _ = list(filter(lambda x: x.startswith('https://weibo.cn/mblog/picAll'), hrefs))
            if(len(_) > 0):
                a = requests.get(_[0], headers=cfg.get_headers())
                d = etree.HTML(a.content).xpath("//div[@class='c']//a/@href")
                ret = filter(lambda x: x.startswith('/mblog/oripic'), d)
                img_url_list.append(list(ret))
            else:
                try:
                    hrefs = x.xpath('./div')[1].xpath('./a/@href').extract()
                    _ = list(filter(lambda x: x.startswith('https://weibo.cn/mblog/oripic'), hrefs))
                    img_url_list.append(_)
                except Exception:
                    img_url_list.append([])
        
        article_id = map(lambda x: self.current_uid + '#' + x, article_id)
        for x in zip(content, is_forward, footer, publish_at, publish_tool, img_url_list, article_id):
            _is_forward, forward_who = x[1]
            yield {
                "content": x[0],
                "is_forward": _is_forward,
                "forward_who": forward_who,
                "footer": x[2],
                "publish_at": x[3],
                "publish_tool": x[4],
                "img_url_list": x[5],
                "article_id": x[6],
                "publisher_id": self.current_uid
            }
        
        cur_page = response.xpath("//div[@id='pagelist']//div/text()").extract()[-1].split('/')[0]
        cur_page = int(cur_page)
        if(cur_page > self.max_page):
            print(f'爬取用户{self.current_uid}完毕')
            return
        else:
            nxt = response.xpath("//div[@id='pagelist']//div/a/@href").extract()[0]
            print(f'用户: {self.current_uid}, 第{cur_page}页')
            time.sleep(random.randint(5,10))
            yield response.follow(nxt, callback=self.parse)
    