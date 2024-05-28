import pandas as pd
import matplotlib.pyplot as plt
import json
import re

# 注意！！！！！改分析的文件只需改 open 里面的文件名即可

# 读取并清理 JSON 文件内容
with open('user.json', 'r', encoding='utf-8') as file:
    file_content = file.read()
    clean_content = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', file_content)  # 移除控制字符

# 加载 JSON 数据
data = json.loads(clean_content)

# 将数据加载到 DataFrame 中
df = pd.json_normalize(data)

# 处理日期列（如果有日期字段）
# df['publish_at'] = pd.to_datetime(df['publish_at'])

# 设置中文字体为 Microsoft YaHei
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用于正常显示负号

# 生成图表
plt.figure(figsize=(10, 6))

# 关注者数量分布
df['followers_count'].plot(kind='bar', title='关注者数量分布')
plt.xlabel('用户')
plt.ylabel('关注者数量')
plt.show()

# 用户描述词云图（示例，不需要安装额外的库）
from wordcloud import WordCloud

text = ' '.join(df['description'].dropna())
wordcloud = WordCloud(font_path='msyh.ttc', width=800, height=400).generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('用户描述词云图')
plt.axis('off')
plt.show()

# 其他可视化
# 如果有更多字段需要可视化，可以添加更多图表
