import json
import random
import os

class Config():
    mongodb_host:        str = 'mongodb://172.30.64.1:27017/'
    db_name:            str = 'weibo'
    uid:                list = ['2992050891', '1910355794',
                                '2274567792', '1893278624']
    max_page:           int = 50
    cookie:             str = []
    user_agent:         str = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0'

    def get_headers(self):
        return {
            "Cookie": random.choice(self.cookie),
            "User-Agent": random.choice(self.user_agent)
        }

cfg = Config()
with open(os.path.join(os.path.dirname(__file__), 'cookie.txt'), 'r') as f:
    while True:
        x = f.readline().strip()
        if not x:
            break
        else:
            cfg.cookie.append(x)

with open(os.path.join(os.path.dirname(__file__), 'user_agent.json'), 'r') as f:
    x = json.loads(f.read())
    cfg.user_agent = x
