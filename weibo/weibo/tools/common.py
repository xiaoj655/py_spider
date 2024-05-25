import re
from datetime import datetime, timedelta

def is_forward(content):
    if(len(content.xpath(".//span[@class='cmt']")) == 0):
        return False, None
    try:
        who = content.xpath('./div')[0].xpath("./span[@class='cmt']/a/text()").extract()[0]
        return True, who
    except Exception:
        return True, None

# footer is the last block of a content block
def get_footer(content):
    _as = content.xpath('./div')[-1].xpath('./a/text()').extract()
    ret = []
    for y in _as[-4:-1]:
        num = re.search(r'\d+', y).group()
        ret.append(num)
    return ret

def get_publish_time(content):
    _time = content.xpath("./div/span[@class='ct']/text()").extract()[0].split('\xa0')[0]
    # ['今天 20:16', '05月23日 22:04', '05月22日 18:35', '05月20日 19:14', '05月14日 18:48',
    # '04月30日 18:06', '04月23日 15:14', '04月23日 12:10', '04月17日 12:25', '04月13日 20:12']
    # times = []
    if '今天' in _time:
        return datetime.now().strftime('%Y-%m-%d ') + _time[-5:]
    elif '月' in _time:
        return datetime.now().strftime('%Y-') + _time[:2] + '-' \
                    + _time[3:5] + ' ' + _time[-5:]
    elif '刚刚' in _time:
        return datetime.now().strftime('%Y-%m-%d %H:%M')
    elif '分钟' in _time:
        return (datetime.now() - timedelta(minutes=int(_time[:_time.find('分钟')])
                                                )
                    ).strftime('%Y-%m-%d %H:%M')
    else:
        # 2022-02-30 02:21
        return _time[:16]

def get_img_list(content):
    _ret = content.xpath('./div')[-1].xpath('./a/@href').extract()
    return _ret

def get_publish_tool(content):
    _ = content.xpath('./div')[-1].xpath("./span[@class='ct']/text()").extract()[0].split('\xa0')
    if len(_) < 2 :
        return '无'
    _ = _[1][2:]
    return _