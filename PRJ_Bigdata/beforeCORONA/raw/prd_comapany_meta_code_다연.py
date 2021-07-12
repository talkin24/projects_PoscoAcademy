#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 필요한 라이브러리 불러오기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import string
import requests
from bs4 import BeautifulSoup

def missing_prd_company():
    data=pd.read_csv('C:/Users/user1/Downloads/missing_prd_company.csv')
    data=data.drop('Unnamed: 0',axis=1)
    meta=pd.read_csv('C:/Users/user1/Downloads/meta_data_last.csv')
    index=meta[meta['prd_company'].isnull()].index.to_list()

    for i in range(len(meta)):
        if meta['prd_company'][i]=='.':
            meta['prd_company'][i]=''
        for j in range(len(index)):
            if i==index[j]:
                meta['prd_company'][i]=''
  
    for i in range(len(meta)):
        for j in range(len(data)):
            if meta['title'][i]==data['title'][j]:
                meta['prd_company'][i]=data['prd_company'][j]

    missing_nums=[]
    for i in range(len(data)):
        if data['prd_company'][i] !='.':
            missing_nums.append(i)

    print('스크래핑으로 %s의 결측치를 채웠고, 남은 prd_company의 결측치 수는 %s입니다.' %(len(missing_nums),(len(data)-len(missing_nums))))

    return meta

meta_prd_company=missing_prd_company()
meta_prd_company.to_csv('meta_prd_company.csv')

