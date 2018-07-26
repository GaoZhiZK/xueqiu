# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 18:14:34 2018

@author:高智
"""

from urllib import request
import time
import json
import pandas as pd
import configuration_message
import logging

    #设置日志文件---------------------------------------------------------------------
logger = logging.getLogger()  # logging对象
fh = logging.FileHandler("logging.log")  # 文件对象
sh = logging.StreamHandler()  # 输出流对象
fm = logging.Formatter('%(asctime)s-%(filename)s[line%(lineno)d]-%(levelname)s-%(message)s')  # 格式化对象
fh.setFormatter(fm)  # 设置格式
sh.setFormatter(fm)  # 设置格式
logger.addHandler(fh)  # logger添加文件输出流
logger.addHandler(sh)  # logger添加标准输出流（std out）
logger.setLevel(logging.ERROR)  # 设置从那个等级开始提示
    #----------------------------------------------------------------------------------------
#all_page_crawler函数获取一个url所有页面的信息，写入文件
def all_page_crawler(url):
    #输出日期信息-----------------------------------------------------------
    current_time=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    current_time_date=current_time.split(' ')[0]    #只保留年月日
    #-----------------------------------------------------------------------
    #将网址按‘#’分开，以方便操作网址内容----------------------------------------------------
    url_split=url.split('&')
    feature=url_split[-2].split('=')[0]
    page=int(url_split[-3].split('=')[1])
    #-------------------------------------------------------------------------------------
    #解析第一页内容，while做判断用
    try:
        req = request.Request(url, None, configuration_message.headers)   #用Request类构建了一个完整的请求，增加了headers等一些信息
        logging.debug('%s:%d page is OK'  % (feature,page))
    except:
        logging.error('%s:%d page is not OK'  % (feature,page))
        exit()
    response = request.urlopen(req)                                    #打开URL信息
    read_response = response.read().decode("utf-8")                  #读取信息
    #---------------------------------------------------------------------------
    matrix_name=[]          #初始化存储id和name的矩阵
    matrix_feature=[]          #初始化存储股票交易，分享或关注信息的矩阵
    #循环一次，翻一页-------------------------------------------------------
    while read_response!='{}':  
        json_response = json.loads(read_response)                          # 转出json格式
        all_stock=json_response['list']            #json_response是一个字典，所需信息在键值为‘list’中
        
        for stock in all_stock:
            matrix_name_row=[]            #初始化matrix_name矩阵的行
            matrix_feature_row=[]       #初始化matrix_feature矩阵的行
            stock_id=stock['symbol']                     #股票id
            stock_name=stock['name']                 #股票名字
            stock_feature=stock['%s' % feature]      #股票交易，讨论，或分享中一个，与url有关
            matrix_name_row.append(stock_id)
            matrix_name_row.append(stock_name)
            matrix_feature_row.append(stock_id)
            matrix_feature_row.append(current_time_date)
            matrix_feature_row.append(stock_feature)
            matrix_name.append(matrix_name_row)
            matrix_feature.append(matrix_feature_row)

        page+=1             #翻页
        url_split[-3]='page=%d' % page          #将翻页后的页码加入网址中
        url_split[-1]='_=%s' % time.time()      #当前时间
        url='&'.join(url_split)                 #翻页后的网址
        #以下三行解析翻页后网页内容，如果没有内容，循环停止，作为是否循环的条件--------------------
        try:            #读取下一页信息
            req = request.Request(url, None, configuration_message.headers)
            logging.debug('%s:%d page is OK'  % (feature,page))
        except:
            logging.error('%s:%d page is not OK'  % (feature,page))
            exit()
        response = request.urlopen(req)                                    #打开URL信息
        read_response = response.read().decode("utf-8")  
       #---------------------------------------------------------------------------------------------
    id_name_df=pd.DataFrame(columns=['stock_id','stock_name'],data=matrix_name)     #表示stock的id和name对应的dataframe
    id_feature_df=pd.DataFrame(columns=['stock_id','date','stock_%s' % feature],data=matrix_feature)
    return id_name_df,id_feature_df


