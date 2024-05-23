import requests
import json
from mongo.interface import db
import re

cookie = "_T_WM=a7cf630d849a38dc33b529a13e171e8c; SCF=AiHvORT6oh6IjzqlxdG9D3LouMNOAshKdZ0-QqWMXfXYREAbxHxj8IufRQpiI_DMZlc95Ipr105sTJXBQZI1JIs.; SUB=_2A25LS0NyDeRhGeFH6VAY9C_FzTiIHXVoKdq6rDV6PUJbktAGLUGhkW1Ne6Rgx1JgDQTac837BINA7b_zzcuIdS5p; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW-xwH7-1A2OihRyU1GzXTR5JpX5KMhUgL.FoM4eoz4Sh24SoB2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMN1KzE1KBp1KqX; SSOLoginState=1716466466; ALF=1719058466"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "cookie": cookie,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-"
}

a = [1,2,3]
b = '赞[123]'
print(re.search(r'\d+', b).group())