import pandas as pd
import matplotlib.pyplot as plt
import ujson as json
import re



# 读取并清理 JSON 文件内容
with open('weibo.weibo3.json', 'r', encoding='utf-8') as file:
    file_content = file.read()
    clean_content = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', file_content)  # 移除控制字符

    # 加载 JSON 数据
data = json.loads(clean_content)

# 将数据加载到 DataFrame 中
df = pd.json_normalize(data)

# 处理日期列
df['publish_at'] = pd.to_datetime(df['publish_at'])

# 设置中文字体为 SimHei
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用于正常显示负号

# 生成图表
plt.figure(figsize=(10, 6))

# 每日发布数量
publish_daily_counts = df.set_index('publish_at').resample('D').size()
if not publish_daily_counts.empty:
    publish_daily_counts.plot(kind='line', title='每日发布数量')
    plt.xlabel('日期')
    plt.ylabel('发布数量')
    plt.show()

# 转发与否的分布
is_forward_counts = df['is_forward'].value_counts()
if not is_forward_counts.empty:
    is_forward_counts.plot(kind='pie', labels=['不转发', '转发'], autopct='%1.1f%%', title='转发与否的分布')
    plt.ylabel('')
    plt.show()

# 每条微博的图片数量
df['img_count'] = df['img_url_list'].apply(len)
img_count_counts = df['img_count'].value_counts().sort_index()
if not img_count_counts.empty:
    img_count_counts.plot(kind='bar', title='每条微博的图片数量分布')
    plt.xlabel('图片数量')
    plt.ylabel('微博数量')
    plt.show()