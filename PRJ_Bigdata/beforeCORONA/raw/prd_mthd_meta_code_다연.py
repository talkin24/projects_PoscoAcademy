#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 직접 손으로 결측치를 채워넣은 데이터를 추가한 데이터 프레임
def missing_prd_mthd():

    final_prd_mthd=pd.read_csv('missing_prd_mthd.csv')
    final_prd_mthd.drop(['Unnamed: 0','re_title'],axis=1,inplace=True)
    meta=pd.read_csv('meta_data_last.csv')

    ls_added_value=[]
    for i in range(len(final_prd_mthd)):
        if final_prd_mthd['prd_mthd'][i]==",":
            final_prd_mthd['prd_mthd'][i]='.'
    for i in range(len(final_prd_mthd)):
        if final_prd_mthd['prd_mthd'][i] !='.':
            ls_added_value.append(i)
    print('스크래핑으로 채워넣은 결측치의 수는 %s입니다.' %(len(ls_added_value)))
  
    for i in range(len(meta)):
        for j in range(len(final_prd_mthd)):
            if meta['title'][i]==final_prd_mthd['title'][j]:
                meta['prd_mthd'][i]=final_prd_mthd['prd_mthd'][j]

return meta

