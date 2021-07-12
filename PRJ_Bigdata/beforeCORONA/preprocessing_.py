import pandas as pd

df_raw = pd.read_csv('./raw/movie_meta_last.csv', engine='python')
df_scrapping_budget = pd.read_csv('./raw/scrapping_budget.csv', engine='python')
df_scrapping_kwrds = pd.read_csv('./raw/scrapping_kwrds.csv', engine='python')

#    변수명 : budget
#    scrapping해서 채워 넣음(IMDB 기준, IMDB에 없는 경우 the numbers 참고하였음)
#    밀려서 들어온 데이터 : tt1781967, tt2367359, tt0387898, tt7017420, tt4950016, tt7048386, tt1587396, tt0498879, tt4403432, tt2010510
#    0이 3개 빠진 듯한 데이터들이 좀 있는데, 그런 관측치는 다른 값들도 없어서 어차피 삭제될 거라 가정하고 수정하지 않음.
def budget(df_raw, df_scrapping):
    df_temp = pd.concat([df_scrapping['movie_id'], df_scrapping['budget']], axis='columns')
    df_raw = df_raw.drop('budget', axis=1)
    df_merge = pd.merge(df_raw, df_temp, on='movie_id', how='inner')
    return df_merge
df_temp = budget(df_raw, df_scrapping_budget)
# 변수명 : series
# 결측치 없음
# 시리즈 유무로 파생변수 생성
def series_new(df_raw):
    df_raw.loc[df_raw['series'] == '.', 'series_new'] = 0
    df_raw.loc[df_raw['series'] != '.', 'series_new' ] = 1
    df_raw['series_new'].astype('int')
    return df_raw
df_temp = series_new(df_temp)
# 변수명 : kwrds
# 결측치 개수 : 1363 -> 215
# imdb에서 plot keywords scrapping 가능 -> 전부 새로 scrapping
# 구분자 \n이므로 정규식으로 텍스트만 뽑아서 써야함
def kwrds(df_raw, df_scrapping):
    df_temp = pd.concat([df_scrapping['movie_id'], df_scrapping['kwrds']], axis='columns')
    df_raw = df_raw.drop('kwrds', axis=1)
    df_merge = pd.merge(df_raw, df_temp, on='movie_id', how='inner')
    return df_merge
df_temp = kwrds(df_temp, df_scrapping_kwrds)

# 변수명 : creative_type
# 이상치 확인 결과 영화가 아닌 TV시리즈 -> 삭제
# 결측치 369개 -> 265개 (The numbers에서 확인)
def creative_type(df_raw):
    # movie_id = ['tt7017420', 'tt4950016', 'tt7048386', 'tt4403432', 'tt2010510']
    # for ids in movie_id:
    #     df_raw.drop(df_raw[df_raw['movie_id'] == ids].index, axis=0, inplace=True)

    contemporary_id = ['tt5851562','tt0160184','tt1206885','tt6189022','tt1540128','tt8688634','tt7545266','tt4682804','tt8367814',
                       'tt1478839','tt8332922','tt7798646','tt7329656','tt7390646','tt7510346','tt0279831','tt0271259','tt0102782',
                       'tt5563334','tt5125894','tt9173418','tt6521876','tt2367359','tt2354181','tt7489740','tt0102915','tt0319829',
                       'tt4364194','tt9354944','tt0055184','tt0364569','tt0053291','tt0045152','tt0314412','tt1666335','tt5928532',
                       'tt0044081','tt0032976','tt0105236','tt0051207','tt0261755','tt0081114','tt2326612','tt0374563','tt0475937',
                       'tt0997047','tt3442006','tt0401815','tt1781058','tt0808331','tt1407084','tt0352994','tt1853643','tt7026672',
                       'tt2883512','tt1164999','tt1321511','tt2616810','tt1951261']
    fantasy_id = ['tt5697572','tt0107719','tt9086228','tt0074225']
    kids_id = ['tt5814534','tt6324278','tt4131800','tt3220976']
    factual_id = ['tt0388230','tt0454776']
    dramatization_id = ['tt3513548','tt0081059','tt4916630','tt7083526','tt7339792','tt0080678','tt0796368','tt2837574','tt2273657',
                        'tt0475355']
    historical_id = ['tt5822564','tt0340376','tt2461150','tt0077296','tt0059113','tt0072684','tt0066090','tt0102443','tt7984734',
                     'tt0077362','tt0044030','tt0063592','tt1229822']
    science_id = ['tt0074812','tt0067065','tt0069768','tt0074486','tt4827558','tt4009278']
    superhero_id = ['tt1502712']
    multiple_id = []

    for ids in contemporary_id:
        df_raw.loc[df_raw['movie_id'] == ids, 'creative_type'] = 'contemporary fiction'
    for ids in fantasy_id:
        df_raw.loc[df_raw['movie_id'] == ids, 'creative_type'] = 'fantasy'
    for ids in kids_id:
        df_raw.loc[df_raw['movie_id'] == ids, 'creative_type'] = 'kids fiction'
    for ids in factual_id:
        df_raw.loc[df_raw['movie_id'] == ids, 'creative_type'] = 'factual'
    for ids in dramatization_id:
        df_raw.loc[df_raw['movie_id'] == ids, 'creative_type'] = 'dramatization'
    for ids in historical_id:
        df_raw.loc[df_raw['movie_id'] == ids, 'creative_type'] = 'historical fiction'
    for ids in science_id:
        df_raw.loc[df_raw['movie_id'] == ids, 'creative_type'] = 'science fiction'
    for ids in superhero_id:
        df_raw.loc[df_raw['movie_id'] == ids, 'creative_type'] = 'super hero'
    for ids in multiple_id:
        df_raw.loc[df_raw['movie_id'] == ids, 'creative_type'] = 'multiple creative types'
    return df_raw
df_temp = creative_type(df_temp)

# 변수명 : src
# 결측치 310개 -> 237개 (The numbers에서 확인)
def src(df_raw):
    shortfilm = ['tt5814534'] #based on short film
    musical = ['tt5697572'] # Based on Musical or Opera
    original = ['tt6324278','tt6189022','tt1540128','tt8688634','tt7545266','tt4682804','tt4916630','tt8367814','tt0220506',
                'tt7329656','tt7390646','tt0271259','tt5125894','tt2367359','tt4364194','tt9354944','tt7984734','tt0074958',
                'tt0077362','tt0053291','tt0045152','tt1666335','tt2326612','tt4827558','tt0374563','tt0475937','tt2141751',
                'tt0997047','tt0467110','tt3442006','tt0808331','tt0352994','tt1853643','tt2883512','tt1164999','tt2616810',
                'tt1951261'] # Original Screenplay
    fiction = ['tt0160184','tt1206885','tt0340376','tt1478839','tt0077269','tt7510346','tt0059113','tt0072684','tt5563334',
               'tt0314412','tt0401815','tt1229822','tt1781058','tt7026672'] # Based on Fiction Book / Short Story
    factual = ['tt3513548','tt7083526','tt0080678','tt2837574','tt2273657'] # Based on Factual Book/Article
    comic = ['tt5822564','tt1502712','tt1321511'] # Based on Comic/Graphic Novel
    real = ['tt0081059','tt2461150','tt7339792','tt3480796','tt0796368','tt0454776','tt0475355','tt0460791'] # Based on Real Life Events
    movie = ['tt6521876'] # Based on Movie
    toy = ['tt4131800'] # based on toy
    folk = ['tt9086228'] # Based on Folk Tale/Legend/Fairytale
    remake = ['tt1407084'] # remake

    for ids in shortfilm:
        df_raw.loc[df_raw['movie_id'] == ids, 'src'] = 'based on short film'
    for ids in musical:
        df_raw.loc[df_raw['movie_id'] == ids, 'src'] = 'based on musical or opera'
    for ids in original:
        df_raw.loc[df_raw['movie_id'] == ids, 'src'] = 'original screenplay'
    for ids in fiction:
        df_raw.loc[df_raw['movie_id'] == ids, 'src'] = 'based on fiction book/short story'
    for ids in factual:
        df_raw.loc[df_raw['movie_id'] == ids, 'src'] = 'based on factual book/article'
    for ids in comic:
        df_raw.loc[df_raw['movie_id'] == ids, 'src'] = 'based on comic/graphic Novel'
    for ids in real:
        df_raw.loc[df_raw['movie_id'] == ids, 'src'] = 'based on real life events'
    for ids in movie:
        df_raw.loc[df_raw['movie_id'] == ids, 'src'] = 'based on movie'
    for ids in toy:
        df_raw.loc[df_raw['movie_id'] == ids, 'src'] = 'based on toy'
    for ids in folk:
        df_raw.loc[df_raw['movie_id'] == ids, 'src'] = 'based on folk tale/legend/fairytale'
    for ids in remake:
        df_raw.loc[df_raw['movie_id'] == ids, 'src'] = 'remake'
    return df_raw
df_temp = src(df_temp)

# 변수명 : actor
# 결측치 37개 -> 34개 수기입력 (imdb에서 확인)
# actor -> actor1,2,3,4 4개의 변수로 변경
def actor(df_raw):
    df_raw.loc[df_raw['movie_id'] == 'tt4906112', 'actor'] = 'Martin Kove,Jaimie Steck,Mike Mayhall,Chase Victoria'
    df_raw.loc[df_raw['movie_id'] == 'tt6000398', 'actor'] = 'Rica Matsumoto,Veronica Taylor,Rachael Lillis,Ikue Ôtani'
    df_raw.loc[df_raw['movie_id'] == 'tt1981703', 'actor'] = 'Perla Sanchez'

    df_raw['actor_1'] = df_raw['actor'].str.split(',').str[0]
    df_raw['actor_2'] = df_raw['actor'].str.split(',').str[1]
    df_raw['actor_3'] = df_raw['actor'].str.split(',').str[2]
    df_raw['actor_4'] = df_raw['actor'].str.split(',').str[3]
    df_raw['actor_1'].str.strip()
    df_raw['actor_2'].str.strip()
    df_raw['actor_3'].str.strip()
    df_raw['actor_4'].str.strip()
    return df_raw
df_temp = actor(df_temp)

# 변수명 : director
# 결측치 66개
# "(co-director)" 제거
def director(df_raw):
    for idx in range(0, 5551):
        try:
            df_raw['director'].loc[idx] = df_raw['director'].loc[idx].replace('(co-director)', '')
        except:
            pass
    return df_raw
df_temp = director(df_temp)

# 변수명 : writer
# 결측치 : 151
# 각본가 구분이 너무 다양하고 한 영화에 여러명 등장. 영화의 두드러진 특징으로 보기 어려움. 불필요.

# 변수명 : description
# 결측치 : 115
# 변수명 : synop
# 결측치 : 102
# 두 항목은 plot을 설명한다는 공통점. 즉 대체 가능. 둘 다 없는 관측치는 존재하지 않음.
# 대개 description 품질이 더 좋음

df_temp.to_csv('./raw/df_temp.csv', header=True, index=False)
