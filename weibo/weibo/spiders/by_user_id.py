import scrapy
from scrapy.exceptions import CloseSpider
from datetime import datetime, timedelta
from config.config import cfg
import time
import re


class ByUserIdSpider(scrapy.Spider):
    name = "by-user-id"
    allowed_domains = ["weibo.cn"]
    max_page = cfg.max_page
    # start_urls = ["https://weibo.cn/2803301701/profile"]
    start_urls = [f'https://weibo.cn/{x}/profile' for x in cfg.uid]


    def gettime(self, info):
        time = info.css('.ct::text').get().split('来自')[0]
        if '刚刚' in time:
            time = datetime.now().strftime('%Y-%m-%d %H:%M')
        elif '分钟' in time:
            m = int(time[:time.find('分钟')])
            time = (datetime.now() - timedelta(minutes=m)).strftime('%Y-%m-%d %H:%M')
        elif '今天' in time:
            t = datetime.now().strftime('%Y-%m-%d')
            time = t + ' ' + time[3:]
        elif '月' in time:
            y= datetime.now().strftime('%Y')
            month = time[0:2]
            day = time[3:5]
            time = time[7:12]
            time = y + '-' + month + '-' + day + ' ' + time
        else:
            time = time[:16]
        return time[0:-1]
    def get_footer(self, info):
        star_num = 0
        forward_num = 0
        comment_num = 0
        for x in info.css('a')[-4:]:
            _t = x.css('a::text').get()
            if '赞' in _t:
                star_num = int(re.search(r'\d+', _t).group())
            elif '转发' in _t:
                forward_num = int(re.search(r'\d+', _t).group())
            elif '评论' in _t:
                comment_num = int(re.search(r'\d+', _t).group())
        return {"star_num": star_num, "forward_num": forward_num, "comment_num": comment_num}
            
                

    def parse(self, response):
        content = response.xpath('//div[@class="c"]')
        content = content[0:-1]
        for x in content:
            try:
                _content = x.css('.ctt::text').getall()
                _time = self.gettime(x)
                yield {
                    "content": ''.join(_content),
                    "time": _time,
                    "footer": self.get_footer(x),
                    "publisher": "2803301701"
                }
            except Exception as e:
                print('error', e)
        next_page = response.xpath('//div[@class="pa"]//a/@href')[0].get()

        # 判断是否达到最大页数
        if(int(next_page.split('=')[-1]) > self.max_page):
            raise CloseSpider(f'reach max page{self.max_page}')

        time.sleep(1)
        yield response.follow(next_page, callback=self.parse)