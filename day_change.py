# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:16:53 2018

@author: sz.it.intern1
"""

import pandas as pd
import config
import os
from datetime import date, timedelta

def day_change(today):
    feature=pd.read_csv(config.feature_path,header=0)
    #获取前一天日期---------------------
    yestoday=today - timedelta(days=1)
    #得到前一天和当天的数据-----------------------------------------------------------------
    feature_day_before=feature[feature.date.isin([str(yestoday)])]
    feature_date=feature[feature.date.isin([str(today)])]
    #合并前一天和当天数据，以便于计算该变量
    feature_merge=pd.merge(feature_day_before,feature_date,on=['stock_id'],how='outer')
    #当天值减去前一天的值，得到变化量------------------------
    feature_merge['deal_change']=feature_merge.apply(lambda x:x['stock_deal_y']-x['stock_deal_x'],axis=1)
    feature_merge['follow_change']=feature_merge.apply(lambda x:x['stock_follow_y']-x['stock_follow_x'],axis=1)
    feature_merge['tweet_change']=feature_merge.apply(lambda x:x['stock_tweet_y']-x['stock_tweet_x'],axis=1)
    #得到仅包含id,date和变化量的dataframe
    feature_day_change=feature_merge[['stock_id','date_x','deal_change','follow_change','tweet_change']]
    feature_day_change.rename(columns={'date_x':'date'},inplace=True)
    feature_day_change[['date']]=today
    #存储
    if os.path.exists(config.change_path):
        feature_day_change.to_csv(config.change_path,header=False,index=False,mode='a',encoding='UTF-8')
    else:
        feature_day_change.to_csv(config.change_path,header=False,index=False,encoding='UTF-8')
        
today=date.today()
change=day_change(today)