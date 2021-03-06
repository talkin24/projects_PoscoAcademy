# -*- coding: utf-8 -*-
"""preprocess_scrapping_prd_company.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B7pooisR1kRTJ5_ETMnkYDNT6vtelDWF
"""

def preprocess_scrp_prd_company():
  # mv_id별 prd_comapny 추출 (우선순위 USA-Worldwide/theatrical-all media)
  import pandas as pd
  scrp_prd_company=pd.read_csv('scrp_prd_company.csv')
  scrp_prd_company=scrp_prd_company.drop('Unnamed: 0',axis=1)
  scrp_prd_company=scrp_prd_company.rename({'company':'prd_company'},axis='columns')

  # movie_meta_cleaned.csv 데이터 갯수 : 5535
  # 스크래핑한 prd_company 데이터 갯수 : 5203
  # 스크래핑안된 movie_id 결측치 수 : 5535-5203 = 332 개 

  # USA , theatrical만 뽑은 mv_id, prd_company : 4534 개
  mv_ls=scrp_prd_company['movie_id'].unique()
  mv_ls=mv_ls.tolist()

  com=[]
  mv_id=[]
  for i in mv_ls:
    for j in range(len(scrp_prd_company)):
      if scrp_prd_company['movie_id'][j]==i:
        if (scrp_prd_company['country'][j]=='USA') & (scrp_prd_company['types'][j]=='theatrical'):
          com.append((scrp_prd_company['prd_company'][j]))
          mv_id.append(scrp_prd_company['movie_id'][j])
          break

  # for문으로 돌려 찾은 movie_id와 prd_company 데이터프레임으로 변환
  test=pd.DataFrame({'movie_id':mv_id,
                    'prd_company':com})

  # USA, theatrical이 아닌 movie_id 구하기 
  A=set(mv_id) # usa, theatrical인 movie_id
  B=set(mv_ls) # 스크래핑한 movie_id
  C=B-A
  # set을 list로 변경
  C=list(C)

  # USA , all media만 뽑은 mv_id, prd_company : 202 개
  com_1=[]
  mv_id_1=[]
  for i in C:
    for j in range(len(scrp_prd_company)):
      if scrp_prd_company['movie_id'][j]==i:
        if (scrp_prd_company['country'][j]=='USA') & (scrp_prd_company['types'][j]=='all media'):
          com_1.append((scrp_prd_company['prd_company'][j]))
          mv_id_1.append(scrp_prd_company['movie_id'][j])
          break

  # for문으로 돌려 찾은 movie_id와 prd_company 데이터프레임으로 변환
  test1=pd.DataFrame({'movie_id':mv_id_1,
                    'prd_company':com_1})
  test1.to_csv('test1.csv')

  C=B-A
  D=set(mv_id_1)
  E=C-D

  # World-wid , theatrical만 뽑은 mv_id, prd_company : 40 개
  E=list(E)

  com_2=[]
  mv_id_2=[]
  for i in E:
    for j in range(len(scrp_prd_company)):
      if scrp_prd_company['movie_id'][j]==i:
        if (scrp_prd_company['country'][j]=='World-wide') & (scrp_prd_company['types'][j]=='theatrical'):
          com_2.append((scrp_prd_company['prd_company'][j]))
          mv_id_2.append(scrp_prd_company['movie_id'][j])
          break

  # for문으로 돌려 찾은 movie_id와 prd_company 데이터프레임으로 변환
  test2=pd.DataFrame({'movie_id':mv_id_2,
                    'prd_company':com_2})

  F=set(mv_id_2)
  E=C-D
  G=E-F

  # World-wid , all media만 뽑은 mv_id, prd_company : 128 개
  G=list(G)

  com_3=[]
  mv_id_3=[]
  for i in G:
    for j in range(len(scrp_prd_company)):
      if scrp_prd_company['movie_id'][j]==i:
        if (scrp_prd_company['country'][j]=='World-wide') & (scrp_prd_company['types'][j]=='all media'):
          com_3.append((scrp_prd_company['prd_company'][j]))
          mv_id_3.append(scrp_prd_company['movie_id'][j])
          break

  # for문으로 돌려 찾은 movie_id와 prd_company 데이터프레임으로 변환
  test3=pd.DataFrame({'movie_id':mv_id_3,
                    'prd_company':com_3})

  G=E-F
  H=set(mv_id_3)
  T=G-H

  # USA , DVD만 뽑은 mv_id, prd_company : 220 개
  T=list(T)

  com_4=[]
  mv_id_4=[]
  for i in T:
    for j in range(len(scrp_prd_company)):
      if scrp_prd_company['movie_id'][j]==i:
        if (scrp_prd_company['country'][j]=='USA') & (scrp_prd_company['types'][j]=='DVD'):
          com_4.append((scrp_prd_company['prd_company'][j]))
          mv_id_4.append(scrp_prd_company['movie_id'][j])
          break

  # for문으로 돌려 찾은 movie_id와 prd_company 데이터프레임으로 변환
  test4=pd.DataFrame({'movie_id':mv_id_4,
                    'prd_company':com_4})

  # 지금까지 만들었던 데이터프레임 병합하고 csv파일생성 
  test_fnl=pd.concat([test,test1,test2,test3,test4])

  # movie_meta_cleaned.csv파일의 movie_id를 불러오기
  movie_meta_cleaned=pd.read_csv('movie_meta_cleaned.csv')
  mv_id_cleaned=pd.DataFrame({'movie_id':movie_meta_cleaned['movie_id']})

  # meta의 movie_id에 prd_company를 병합
  prd_company_final=pd.merge(mv_id_cleaned,test_fnl,how='left',on='movie_id')
  prd_company_final.to_csv('prd_company_final.csv')

# preprocess_scrp_prd_company()