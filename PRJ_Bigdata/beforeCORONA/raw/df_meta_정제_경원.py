import pandas as pd
import numpy as np
import re
import math
import csv


df_meta = pd.read_csv('meta_data_last.csv', engine = 'python', encoding ="cp949")
df_meta

def check_missing_total():
    global df_meta
    for i in df_meta.columns:
        nan_cnt = len(df_meta[df_meta[i].isna()])
        dot_cnt = len(df_meta[df_meta[i]=="."])
        print("%s의 결측치 개수 - %d, %d"%(i, nan_cnt, dot_cnt))

def check_missing(a):
    global df_meta
    nan_cnt = len(df_meta[df_meta[a].isna()])
    dot_cnt = len(df_meta[df_meta[a]=="."])
    print("%s의 결측치 개수 - NaN : %d, dot :%d"%(a, nan_cnt, dot_cnt))

def check_missing_after(a):
    global df_meta
    nan_cnt = len(df_meta[df_meta[a].isna()])
    dot_cnt = len(df_meta[df_meta[a]=="."])
    print("%s의 결측치 대체 후 개수 - NaN : %d, dot :%d"%(a, nan_cnt, dot_cnt))

def replace_missing(m,k,j):
    global df_meta
    df_meta.loc[(df_meta["movie_id"]==m), k] = j


def movie_id():
    global df_meta
    # 결측치 확인
    check_missing("movie_id")

    # 형식에 벗어나는 movie_id 확인 및 변환(ex:tt0125664)
    p = re.compile("tt^\d{7}$")

    for i in range(len(df_meta["movie_id"])):
        if len(re.findall(p, df_meta["movie_id"][i])) == 0:
            df_meta.loc[i, "movie_id"] = df_meta.loc[i, "movie_id"]
        else:
            print(df_meta.loc[i, "movie_id"])
    print("중복되지 않은 movie_id :%s개" % (len(df_meta['movie_id'].value_counts())))


def release_year():
    global df_meta
    # 결측치 확인
    check_missing("release_year")

    # 형식에 벗어나는 movie_id 확인 및 변환(ex:YYYY)
    p = re.compile("r^\d{4}$")

    for i in range(len(df_meta["release_year"])):
        if len(re.findall(p, df_meta["release_year"][i])) == 0:
            df_meta.loc[i, "release_year"] = df_meta.loc[i, "release_year"][:4]

    odd_year = [i for i in df_meta["release_year"] if i.isalpha()]
    print("odd year : %s 개" % (len(odd_year)))


def title():
    global df_meta
    # 결측치 확인
    check_missing("title")

    # 중복 title 확인
    print("중복된 title :%s개" % (len(df_meta[df_meta['title'].duplicated()])))

    # title이 in형인 것 확인
    odd_title = [df_meta["movie_id"][i] for i in range(len(df_meta["movie_id"])) if df_meta["title"][i].isdigit()]
    print("Int형 title :%s개" % (len(odd_title)))
    replace_missing("tt0485236", "title", "Indigènes: Sur les traces d'indigène")
    replace_missing("tt4229814", "title", "Autómata")
    replace_missing("tt5091538", "title", "La folle histoire de Max et Léon")
    replace_missing("tt3547740", "title", "The Bélier Family")
    replace_missing("tt7489740", "title", "Neuilly sa mère, sa mère!")
    replace_missing("tt6021478", "title", "Épouse-moi mon pote")
    replace_missing("tt4146338", "title", "Jagten på TV-Fuskerne")
    
     
    
     

def mpa_rating_origin():
    global df_meta
    check_missing("mpa_rating_origin")
    print("drop하는 걸로 결정")

def mpa_rating():
    global df_meta
    # 결측치 확인
    check_missing("mpa_rating")

    # mpa_rating nan 확인 및 대체("NaN" -> ".")
    mpa_nan = df_meta[df_meta["mpa_rating"].isna()]
    print("dot으로 대체한 mpa_rating이 NaN인 개수 : %s" % (len(mpa_nan)))
    df_meta["mpa_rating"] = df_meta["mpa_rating"].fillna(".")

    # mpa_rating 항목 정리
    df_meta["mpa_rating"] = [str(i).upper() for i in df_meta["mpa_rating"]]
    df_meta["mpa_rating"].value_counts()

    df_meta["mpa_rating"] = df_meta["mpa_rating"].apply(lambda x: "NOT RATED" if x == "NOT" else x)
    df_meta["mpa_rating"] = df_meta["mpa_rating"].apply(lambda x: "NC-17" if x == "UNRATED" else x)
    df_meta["mpa_rating"] = df_meta["mpa_rating"].apply(lambda x: "NC-17" if x == "X" else x)
    df_meta["mpa_rating"] = df_meta["mpa_rating"].apply(lambda x: "PG" if x == "GP" else x)
    df_meta["mpa_rating"] = df_meta["mpa_rating"].apply(lambda x: "PG" if x == "M" else x)
    df_meta["mpa_rating"] = df_meta["mpa_rating"].apply(lambda x: "PG" if x == "M/PG" else x)

    mpa_dot = df_meta.query("mpa_rating=='.'")

    for i in mpa_dot.index:
        cnt = 0
        for j in mpa_dot.columns:
            if mpa_dot[j][i] == ".":
                cnt += 1
            try:
                if math.isnan(mpa_dot[j][i]):
                    cnt += 1
            except:
                pass
    #         print(df_meta["movie_id"][i],df_meta["title"][i], cnt)

    replace_missing("tt5851562", "mpa_rating", "PG-13")
    replace_missing("tt3220976", "mpa_rating", "TV-G")

    # 결측치 대체 후의 결측치 수
    check_missing_after("mpa_rating")


def theater_total():
    global df_meta
    # 결측치 확인
    check_missing("theater_total")

    # odd theater_total 확인 (int형이 아닌 겻)
    print("----------------------------------------")
    print("odd theater_total 확인 (int형이 아닌 겻)")
    for i in range(len(df_meta)):
        if df_meta["theater_total"][i].isalpha():
            print(df_meta["movie_id"][i], df_meta["theater_total"][i])
            
    # odd theater_opening, theater_total를 서치 후 대체
    replace_missing("tt7504726","theater_opening",3752)
    replace_missing("tt7504726","theater_total",3914)
    
    replace_missing("tt5814534","theater_opening",3502)
    replace_missing("tt5814534","theater_total",3502)
    
    replace_missing("tt5697572","theater_opening",3380)
    replace_missing("tt5697572","theater_total",3380)
    
    replace_missing("tt6324278","theater_opening",4242)
    replace_missing("tt6324278","theater_total",4248)
    
    replace_missing("tt1206885","theater_opening",3618)
    replace_missing("tt1206885","theater_total",3618)
    
    replace_missing("tt3513548","theater_opening",2502)
    replace_missing("tt3513548","theater_total",2502)
    
    replace_missing("tt6189022","theater_opening",3286)
    replace_missing("tt6189022","theater_total",3336)
    
    replace_missing("tt5822564","theater_opening",2745)
    replace_missing("tt5822564","theater_total",2745)
    
    replace_missing("tt1540128","theater_opening",2837)
    replace_missing("tt1540128","theater_total",2840)
    
    replace_missing("tt1321869","theater_opening",4)
    replace_missing("tt1321869","theater_total",443)
    
    replace_missing("tt8688634","theater_opening",2665)
    replace_missing("tt8688634","theater_total",2665)
    
    replace_missing("tt7545266","theater_opening",3078)
    replace_missing("tt7545266","theater_total",3081)
    
    replace_missing("tt4682804","theater_opening",37)
    replace_missing("tt4682804","theater_total",231)
    
    replace_missing("tt2461150","theater_opening",3042)
    replace_missing("tt2461150","theater_total",3042)
    
    replace_missing("tt8367814","theater_opening",2165)
    replace_missing("tt8367814","theater_total",2675)
    
    replace_missing("tt0099487","theater_opening",1023)
    replace_missing("tt0099487","theater_total", 1372)
    
    replace_missing("tt8244784","theater_opening",3028)
    replace_missing("tt8244784","theater_total",3028)
    
    replace_missing("tt1478839","theater_opening",2765)
    replace_missing("tt1478839","theater_total",2765)
    
    replace_missing("tt0052618","theater_opening",3084)
    replace_missing("tt0052618","theater_total",3084)
    
    replace_missing("tt7798646","theater_opening",2516)
    replace_missing("tt7798646","theater_total",2516)
    
    replace_missing("tt7083526","theater_opening",2824)
    replace_missing("tt7083526","theater_total",2913)
    
    replace_missing("tt1106860","theater_opening",27)
    replace_missing("tt1106860","theater_total",43)
    
    replace_missing("tt7329656","theater_opening",2853)
    replace_missing("tt7329656","theater_total",2883)
    
    replace_missing("tt7390646","theater_opening",2062)
    replace_missing("tt7390646","theater_total",2062)
    
    replace_missing("tt7510346","theater_opening",2571)
    replace_missing("tt7510346","theater_total",2571)
    
    replace_missing("tt5563334","theater_opening",2439)
    replace_missing("tt5563334","theater_total",2454)
    
    replace_missing("tt5125894","theater_opening",2750)
    replace_missing("tt5125894","theater_total",2750)
    
    replace_missing("tt9173418","theater_opening",2151)
    replace_missing("tt9173418","theater_total",2151)
    
    replace_missing("tt6521876","theater_opening",1)
    replace_missing("tt6521876","theater_total",788)
    
    replace_missing("tt4131800","theater_opening",2528)
    replace_missing("tt4131800","theater_total",2528)
    
    replace_missing("tt4364194","theater_opening",17)
    replace_missing("tt4364194","theater_total",1490)
    
    replace_missing("tt7339792","theater_opening",1620)
    replace_missing("tt7339792","theater_total",1620)
    
    replace_missing("tt9354944","theater_opening",2332)
    replace_missing("tt9354944","theater_total",2332)
    
    replace_missing("tt7984734","theater_opening",8)
    replace_missing("tt7984734","theater_total",978)
    
    check_missing_after("theater_total")
    check_missing_after("theater_opening")


def theater_opening():
#     theater_opening에서 이상치 확인 : 119개영화에 대해서 theater_opening의 값이 과하게 작음.
# (theater_total-theater_opening)의 평균을 이상치 대체 -> 근거 : 매출/유명도 진짜 낮은 다른 영화와 비교
    global df_meta
    
    replace_missing("tt7017420", "theater_total",".")
    replace_missing("tt0498879", "theater_total",".")
    
    theater_exc_dot = df_meta[['movie_id','theater_opening', 'theater_total']]
    
    theater_exc_dot["theater_opening"] = list(map(int, [x.replace(".","-1") for x in theater_exc_dot["theater_opening"]]))
    theater_exc_dot["theater_total"] = list(map(int, [x.replace(".","-1") for x in theater_exc_dot["theater_total"]]))
    
    theater_odd_movie_Id = []
    theater_subtract = 0
    theater_odd_len = 0 
    theater_nor_len = 0

    for i in range(len(theater_exc_dot)):
        if theater_exc_dot["theater_opening"][i] != "-1" and theater_exc_dot["theater_opening"][i] <= 20 and theater_exc_dot["theater_total"][i] >= 1500 :
            theater_odd_movie_Id.append(theater_exc_dot["movie_id"][i])
            theater_odd_len += 1
        elif theater_exc_dot["theater_opening"][i] != "-1" and theater_exc_dot["theater_total"][i] != "-1":
            theater_subtract += theater_exc_dot["theater_total"][i] - theater_exc_dot["theater_opening"][i] 
            theater_nor_len += 1
    print(theater_subtract, theater_nor_len, theater_odd_len)
    
    # (theater_total - theater_opening)의 평균
    theater_mid = int(theater_subtract/ theater_nor_len)
    theater_mid
    
    cnt = 0
    for i in range(len(df_meta)):
        if df_meta["movie_id"][i] in theater_odd_movie_Id:
            if df_meta["theater_total"][i] != "." and df_meta["theater_opening"][i] != ".":
                sub = int(df_meta["theater_total"][i]) - theater_mid
                df_meta.loc[(df_meta["movie_id"]==df_meta["movie_id"][i]), "theater_opening"] = sub
                cnt += 1
    print(cnt)

    print("평균으로 대체한 theater_opening 결측치 : %s개" % (cnt))


def NumOfReviews():
    global df_meta

    # 결측치 확인
    check_missing("reviews_users")
    check_missing("reviews_critics")

    # 새로 스크래핑한 csv파일(NumOfReviews_final) 불러오기
    df_review = pd.read_csv('NumOfReviews_final.csv', engine='python', encoding="cp949")

    # 기존 reviews_users, review_critics drop
    df_meta.drop(columns="reviews_users", inplace=True)
    df_meta.drop(columns="reviews_critics", inplace=True)

    # Scraping 한 reviews_user merge
    df_meta = pd.merge(df_meta, df_review, on="movie_id")

    print("---------------------------------------------")
    check_missing_after("reviews_users")
    check_missing_after("reviews_critics")


def metascore():
    global df_meta

    # 결측치 확인
    check_missing("metascore")

    # 새로 스크래핑한 csv파일(NumOfReviews_final) 불러오기
    df_metaScore = pd.read_csv('MetaScore+.csv', engine='python', encoding="cp949")

    # metascore이 NaN 확인 및 대체
    metaScore_nan = df_meta[df_meta["metascore"].isna()]

    # NaN인 metaScore 값들 있으면 값으로 대체, 없으면 "."으로 대체
    for i in metaScore_nan.index:
        if math.isnan(metaScore_nan["metascore"][i]):
            if metaScore_nan["metascore"][i] == ".":
                pass
            else:
                df_meta.loc[i, "metascore"] = df_metaScore.loc[i, "metascore"]

    print("---------------------------------------------")
    check_missing_after("metascore")





# 실행시 주석을 풀어주세요
# movie_id()
# release_year()
# title()
# mpa_rating_origin()
# mpa_rating()
# theater_opening()
# theater_total()
# NumOfReviews()
# metascore()

# check_missing_total()