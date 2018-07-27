# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:14:00 2018

@author: sz.it.intern1
"""

import logging
import time
Cookie = "_ga=GA1.2.769278738.1531121394; _gid=GA1.2.241832615.1531121394; device_id=d4e21bae75ddabf978812f8bf018af6f;" \
         " s=f011czopa6; __utmz=1.1531121440.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); " \
         "xq_a_token=428fd5b0a9076b32885b26af5a54a8763149a5b8; xqat=428fd5b0a9076b32885b26af5a54a8763149a5b8; " \
         "xq_r_token=3df9fd6a16743e6448e0c81bd71fad556164d674; xq_is_login=1; u=1721284506; " \
         "xq_token_expire=Fri%20Aug%2003%202018%2015%3A32%3A44%20GMT%2B0800%20(CST); bid=c9d2d2358e8d8cb0fdd496571c44ae63_jjdy8w46;" \
         " aliyungf_tc=AQAAABeo9HNzWAYAsnxoyv7PvPR82mi/; Hm_lvt_1db88642e346389874251b5a1eded6e3=1531121394,1531121440,1531187670;" \
         " __utmc=1; _sid=8mpivrGguuo5525Hfou0ILlIVNdezM; __utma=1.769278738.1531121394.1531203360.1531207634.7;" \
         " __utmt=1; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1531207727; __utmb=1.2.10.1531207634"

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3472.3 Safari/537.36',
    'Cookie': Cookie,
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'xueqiu.com',
    'Referer': 'https://xueqiu.com/hq/screener/CN'
}

name_path='D:/xueqiu/data/data1/AllDate_name.csv'          #文件存储路径
feature_path='D:/xueqiu/data/data1/AllDate_feature.csv'  
change_path='D:/xueqiu/data/data1/change.csv'  
log_level=logging.DEBUG
log_path='D:/xueqiu/data/logging.log'
xueqiu_timeout=30

url1='https://xueqiu.com/stock/screener/screen.json?category=SH&orderby=follow&order=desc&page=1&follow=ALL&_=%s'  % time.time() 
url2='https://xueqiu.com/stock/screener/screen.json?category=SH&orderby=tweet&order=desc&page=1&tweet=ALL&_=%s'  % time.time() 
url3='https://xueqiu.com/stock/screener/screen.json?category=SH&orderby=deal&order=desc&page=1&deal=ALL&_=%s'  % time.time() 
