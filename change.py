# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 14:46:52 2018

@author: sz.it.intern1
"""

import pandas as pd
import configuration_message
import os
import time
def day_change(date):
    feature=pd.read_csv('%s\\AllDate_feature.csv' % configuration_message.file_path,header=0)
    #获取前一天日期---------------------
    date_split=date.split('-')        
    date_split[2]=str(int(date_split[2])-1)
    day_before='-'.join(date_split)
    #得到前一天和当天的数据-----------------------------------------------------------------
    feature_day_before=feature[feature.date.isin([day_before])]
    feature_date=feature[feature.date.isin([date])]
    #合并前一天和当天数据，以便于计算该变量
    feature_merge=pd.merge(feature_day_before,feature_date,on=['stock_id'],how='outer')
    #当天值减去前一天的值，得到变化量------------------------
    feature_merge['deal_change']=feature_merge.apply(lambda x:x['stock_deal_y']-x['stock_deal_x'],axis=1)
    feature_merge['follow_change']=feature_merge.apply(lambda x:x['stock_follow_y']-x['stock_follow_x'],axis=1)
    feature_merge['tweet_change']=feature_merge.apply(lambda x:x['stock_tweet_y']-x['stock_tweet_x'],axis=1)
    #得到仅包含id,date和变化量的dataframe
    feature_day_change=feature_merge[['stock_id','date_x','deal_change','follow_change','tweet_change']]
    feature_day_change.rename(columns={'date_x':'date'},inplace=True)
    feature_day_change[['date']]=date
    #存储
    if os.path.exists('%s\\change.csv' % configuration_message.file_path):
        feature_day_change.to_csv('%s\\change.csv' % configuration_message.file_path,header=False,index=False,mode='a',encoding='UTF-8')
    else:
        feature_day_change.to_csv('%s\\change.csv' % configuration_message.file_path,header=False,index=False,encoding='UTF-8')
        
date=time.strftime("%Y-%m-%d", time.localtime())
day_change(date)