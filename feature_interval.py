# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 14:46:52 2018

@author: 高智
"""

import pandas as pd
import configuration_message
#这个函数作用是给定日期，三个特征任意一个，下界，上界，返回这个区间中的股票
def feature_abnormal(date,feature,lowerbound,upperbound):
    change=pd.read_csv('%s\\change.csv' % configuration_message.file_path,header=0)   #读取每日变化量的数据
    change_day=change[change.date.isin([date])]             #将特定日期的数据取出来  
    change_feature=change_day[['stock_id','%s_change' % feature]]       #取出某个特征
    change_feature=change_feature.dropna()                  #去除空列
    change_feature_sort=change_feature.sort_values('%s_change' % feature)        #排序
    #取出区间中的股票
    stock=change_feature_sort[(change_feature_sort['%s_change' % feature] >= lowerbound)&(change_feature_sort['%s_change' % feature] <= upperbound)].reset_index(drop=True)     #每天交易量大于等于5的股票
    return stock
feature_abnormal('2018-07-25','tweet',-200,-1)




#统计每个交易量的股票
def deal_abnormal(date):
    change=pd.read_csv('%s\\change.csv' % configuration_message.file_path,header=0)
    change_day=change[change.date.isin([date])]
    deal_change=change_day[['deal_change']]
    deal_change['num']=1
    deal_num=deal_change.groupby('deal_change').agg('sum').reset_index()    #如交易量为n 的股票有多少支
    return deal_num