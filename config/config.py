class Config():
    mongodb_host:        str = 'mongodb://localhost:27017/'
    db_name:            str = 'weibo'
    uid:                list = ['1858002662', '1669879400']
    max_page:           int = 50

cfg =Config()