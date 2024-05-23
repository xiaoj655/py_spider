import json
import jieba
import jieba.analyse

with open('ac_paper.json', 'r', encoding='utf-8') as f:
    content = json.loads(f.read())
    data = content[2]['data']
    text = ''
    for i in data:
        text += i['b_title']
    keywords = jieba.analyse.extract_tags(text,topK=20)
    keywords2 = jieba.analyse.textrank(text, topK=20)
    print(keywords)
    print(keywords2)