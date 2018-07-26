# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:41:25 2018

@author: 高智
"""
import all_page_crawler
import time
import os
import configuration_message
import pandas as pd
url1='https://xueqiu.com/stock/screener/screen.json?category=SH&orderby=follow&order=desc&page=1&follow=ALL&_=%s'  % time.time() 
url2='https://xueqiu.com/stock/screener/screen.json?category=SH&orderby=tweet&order=desc&page=1&tweet=ALL&_=%s'  % time.time() 
url3='https://xueqiu.com/stock/screener/screen.json?category=SH&orderby=deal&order=desc&page=1&deal=ALL&_=%s'  % time.time() 
def AllDate(url1,url2,url3):
    #读取三个网页信息-------------------------------------------------------------------
    follow_name,follow=all_page_crawler.all_page_crawler(url1)
    tweet_name,tweet=all_page_crawler.all_page_crawler(url2)
    deal_name,deal=all_page_crawler.all_page_crawler(url3)
    #-------------------------------------------------------------------------------
    #汇总三个网页信息----------------------------------------------------------------
    name_merge1=pd.merge(follow_name,tweet_name,on=['stock_id','stock_name'],how='outer')        #
    name_merge2=pd.merge(name_merge1,deal_name,on=['stock_id','stock_name'],how='outer')
    name_merge3=name_merge2.drop_duplicates(subset=['stock_id','stock_name'],keep='first')       
    feature_merge1=pd.merge(follow,tweet,on=['stock_id','date'],how='outer')
    feature_merge2=pd.merge(deal,feature_merge1,on=['stock_id','date'],how='outer')
    #----------------------------------------------------------------------------------------------------
    feature_merge3=feature_merge2.drop_duplicates(subset=['stock_id','date','stock_deal','stock_follow','stock_tweet'],keep='first') #删除重复行
    #保存为csv文件--------------------------------------------------
    if os.path.exists('%s\\AllDate_name.csv' % configuration_message.file_path):
        name_merge3.to_csv('%s\\AllDate_name.csv' % configuration_message.file_path,header=False,index=False,mode='a',encoding='UTF-8')
        feature_merge3.to_csv('%s\\AllDate_feature.csv' % configuration_message.file_path,header=False,index=False,mode='a',encoding='UTF-8')
    else:
        name_merge3.to_csv('%s\\AllDate_name.csv' % configuration_message.file_path,header=True,index=False,encoding='UTF-8')
        feature_merge3.to_csv('%s\\AllDate_feature.csv' % configuration_message.file_path,header=True,index=False,encoding='UTF-8')
    #-------------------------------------------------------------------------------------------------------
AllDate(url1,url2,url3)





