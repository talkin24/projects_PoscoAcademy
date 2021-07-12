import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

df_raw = pd.read_csv('./raw/movie_meta_last.csv', engine='python')

df_bgt_empty = df_raw[df_raw['budget'] == "."]
movie_id = df_bgt_empty['movie_id']

i = 0
for ids in movie_id:
    try:
        i += 1
        print(i)
        url = "https://www.imdb.com/title/{}/".format(ids)
        resp = requests.get(url)
        html = resp.text
        soup = BeautifulSoup(html, "html5lib")
        tags_budget = soup.select("#titleDetails > div:nth-child(12)")

        text_budget = ""
        for tag in tags_budget:
            text_budget += tag.text
        p = re.findall(r'\d+', text_budget)
        p = ''.join(p)
        if text_budget == '':
            df_raw.loc[df_raw['movie_id'] == ids, 'budget'] = '.'
        else:
            df_raw.loc[df_raw['movie_id'] == ids, 'budget'] = p
    except:
        print(ids)

df_raw.loc[df_raw['movie_id'] == "tt0081059", 'budget'] = 35000000
df_raw.loc[df_raw['movie_id'] == "tt0077269", 'budget'] = 12000000
df_raw.loc[df_raw['movie_id'] == "tt0066090", 'budget'] = 11000000
df_raw.loc[df_raw['movie_id'] == "tt7489740", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0074812", 'budget'] = 9000000
df_raw.loc[df_raw['movie_id'] == "tt1730760", 'budget'] = 4500000
df_raw.loc[df_raw['movie_id'] == "tt0081617", 'budget'] = 3500000
df_raw.loc[df_raw['movie_id'] == "tt0106792", 'budget'] = 1800000
df_raw.loc[df_raw['movie_id'] == "tt0063592", 'budget'] = 1455000
df_raw.loc[df_raw['movie_id'] == "tt0074225", 'budget'] = 12000000
df_raw.loc[df_raw['movie_id'] == "tt0076271", 'budget'] = 500000
df_raw.loc[df_raw['movie_id'] == "tt0081114", 'budget'] = 350000
df_raw.loc[df_raw['movie_id'] == "tt0079062", 'budget'] = 170000
df_raw.loc[df_raw['movie_id'] == "tt0275230", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5164184", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0080923", 'budget'] = 3000000
df_raw.loc[df_raw['movie_id'] == "tt0139151", 'budget'] = 15000000
df_raw.loc[df_raw['movie_id'] == "tt0119167", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt6173990", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5851562", 'budget'] = 350000
df_raw.loc[df_raw['movie_id'] == "tt6324278", 'budget'] = 75000000
df_raw.loc[df_raw['movie_id'] == "tt4682804", 'budget'] = 27000000
df_raw.loc[df_raw['movie_id'] == "tt1838544", 'budget'] = 19000000
df_raw.loc[df_raw['movie_id'] == "tt0107719", 'budget'] = 19000000
df_raw.loc[df_raw['movie_id'] == "tt8332922", 'budget'] = 17000000
df_raw.loc[df_raw['movie_id'] == "tt0077296", 'budget'] = 14000000
df_raw.loc[df_raw['movie_id'] == "tt7329656", 'budget'] = 12000000
df_raw.loc[df_raw['movie_id'] == "tt7510346", 'budget'] = 14000000
df_raw.loc[df_raw['movie_id'] == "tt0072684", 'budget'] = 11000000
df_raw.loc[df_raw['movie_id'] == "tt6521876", 'budget'] = 10000000
df_raw.loc[df_raw['movie_id'] == "tt2354181", 'budget'] = 89500000  # 가장 가까운 데이터 90000000, 89000000 의 평균값으로 대체
df_raw.loc[df_raw['movie_id'] == "tt7339792", 'budget'] = 6000000
df_raw.loc[df_raw['movie_id'] == "tt7984734", 'budget'] = 4000000
df_raw.loc[df_raw['movie_id'] == "tt0092615", 'budget'] = 4000000
df_raw.loc[df_raw['movie_id'] == "tt0074958", 'budget'] = 3800000
df_raw.loc[df_raw['movie_id'] == "tt0077362", 'budget'] = 3000000
df_raw.loc[df_raw['movie_id'] == "tt6113488", 'budget'] = 5000000
df_raw.loc[df_raw['movie_id'] == "tt0045793", 'budget'] = 1650000
df_raw.loc[df_raw['movie_id'] == "tt0108000", 'budget'] = 800000
df_raw.loc[df_raw['movie_id'] == "tt0104567", 'budget'] = 500000
df_raw.loc[df_raw['movie_id'] == "tt0102989", 'budget'] = 450000
df_raw.loc[df_raw['movie_id'] == "tt0092548", 'budget'] = 350000
df_raw.loc[df_raw['movie_id'] == "tt0068468", 'budget'] = 25000
df_raw.loc[df_raw['movie_id'] == "tt0074486", 'budget'] = 20000

df_raw.loc[df_raw['movie_id'] == "tt0484562", 'budget'] = 45000000
df_raw.loc[df_raw['movie_id'] == "tt0371257", 'budget'] = 50000000
df_raw.loc[df_raw['movie_id'] == "tt0457419", 'budget'] = 65000000
df_raw.loc[df_raw['movie_id'] == "tt0455967", 'budget'] = 18000000
df_raw.loc[df_raw['movie_id'] == "tt0430779", 'budget'] = 35000000
df_raw.loc[df_raw['movie_id'] == "tt0388125", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1336006", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2625810", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4721124", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4846232", 'budget'] = 4500000
df_raw.loc[df_raw['movie_id'] == "tt3859310", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2034031", 'budget'] = 5000000
df_raw.loc[df_raw['movie_id'] == "tt4385888", 'budget'] = 7000000
df_raw.loc[df_raw['movie_id'] == "tt2132285", 'budget'] = 8000000
df_raw.loc[df_raw['movie_id'] == "tt2326612", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2402101", 'budget'] = 20000000
df_raw.loc[df_raw['movie_id'] == "tt6040662", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt6902696", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5691670", 'budget'] = 8500000
df_raw.loc[df_raw['movie_id'] == "tt5715874", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4827558", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5613484", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1727770", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0401420", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0374563", 'budget'] = 17000000
df_raw.loc[df_raw['movie_id'] == "tt0475937", 'budget'] = 3000000 * 1.2
df_raw.loc[df_raw['movie_id'] == "tt1313139", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1166100", 'budget'] = 200000000 * 0.02
df_raw.loc[df_raw['movie_id'] == "tt2788716", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2334733", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5742374", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2141751", 'budget'] = 1850000
df_raw.loc[df_raw['movie_id'] == "tt1763264", 'budget'] = 2900000
df_raw.loc[df_raw['movie_id'] == "tt0497972", 'budget'] = 5000000
df_raw.loc[df_raw['movie_id'] == "tt1037218", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2980472", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5884230", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3480796", 'budget'] = 10000000
df_raw.loc[df_raw['movie_id'] == "tt2368254", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2062700", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2101383", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3062976", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2891174", 'budget'] = 8000000
df_raw.loc[df_raw['movie_id'] == "tt4679210", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1667321", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4669264", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4899370", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt6225520", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt6108178", 'budget'] = 6000000
df_raw.loc[df_raw['movie_id'] == "tt5023260", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1596345", 'budget'] = 19000000
df_raw.loc[df_raw['movie_id'] == "tt0402894", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0480242", 'budget'] = 25000000
df_raw.loc[df_raw['movie_id'] == "tt0465234", 'budget'] = 130000000
df_raw.loc[df_raw['movie_id'] == "tt0997047", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0435670", 'budget'] = 30000000
df_raw.loc[df_raw['movie_id'] == "tt1185416", 'budget'] = 55000000
df_raw.loc[df_raw['movie_id'] == "tt0417433", 'budget'] = 26000000
df_raw.loc[df_raw['movie_id'] == "tt0772193", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1093908", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0452681", 'budget'] = 12000000
df_raw.loc[df_raw['movie_id'] == "tt0396555", 'budget'] = 150000000
df_raw.loc[df_raw['movie_id'] == "tt0467110", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3442006", 'budget'] = 7000000
df_raw.loc[df_raw['movie_id'] == "tt2370248", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0780595", 'budget'] = 26000000
df_raw.loc[df_raw['movie_id'] == "tt5071886", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0401815", 'budget'] = 3500000
df_raw.loc[df_raw['movie_id'] == "tt1858481", 'budget'] = 2500000
df_raw.loc[df_raw['movie_id'] == "tt2215395", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2488778", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4009278", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5270948", 'budget'] = 13000000
df_raw.loc[df_raw['movie_id'] == "tt2390237", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3203528", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4399952", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2317337", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3735246", 'budget'] = 1250000000 * 0.015
df_raw.loc[df_raw['movie_id'] == "tt1188982", 'budget'] = 750000000 * 0.016
df_raw.loc[df_raw['movie_id'] == "tt8108198", 'budget'] = 4500000
df_raw.loc[df_raw['movie_id'] == "tt1255951", 'budget'] = 1000000 * 0.021
df_raw.loc[df_raw['movie_id'] == "tt4110568", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0806088", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1144804", 'budget'] = 12500000
df_raw.loc[df_raw['movie_id'] == "tt2140465", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5859238", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt6971752", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1891757", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2172071", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4559046", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2309764", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0991346", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1395025", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5197544", 'budget'] = 35000000 * 0.015
df_raw.loc[df_raw['movie_id'] == "tt0488414", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3679060", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5474036", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3678782", 'budget'] = 250000000 * 0.015
df_raw.loc[df_raw['movie_id'] == "tt2806788", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2639254", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2758904", 'budget'] = 20000000
df_raw.loc[df_raw['movie_id'] == "tt2172584", 'budget'] = 15000000
df_raw.loc[df_raw['movie_id'] == "tt2091935", 'budget'] = 8000000
df_raw.loc[df_raw['movie_id'] == "tt6277440", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3595298", 'budget'] = 1800000000 * 0.015
df_raw.loc[df_raw['movie_id'] == "tt2905838", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4169250", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3142688", 'budget'] = 120000000 * 0.016
df_raw.loc[df_raw['movie_id'] == "tt6843812", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt7255568", 'budget'] = 800000000 * 0.014
df_raw.loc[df_raw['movie_id'] == "tt4559006", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4559006", 'budget'] = 2900000
df_raw.loc[df_raw['movie_id'] == "tt6452574", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3754940", 'budget'] = 3800000 * 1.1
df_raw.loc[df_raw['movie_id'] == "tt4853102", 'budget'] = 3500000
df_raw.loc[df_raw['movie_id'] == "tt0473488", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt8695030", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4572792", 'budget'] = 10000000
df_raw.loc[df_raw['movie_id'] == "tt0970468", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2261331", 'budget'] = 8000000 * 1.66
df_raw.loc[df_raw['movie_id'] == "tt0400525", 'budget'] = 16000000
df_raw.loc[df_raw['movie_id'] == "tt0427969", 'budget'] = 28000000
df_raw.loc[df_raw['movie_id'] == "tt0810819", 'budget'] = 15000000
df_raw.loc[df_raw['movie_id'] == "tt0796368", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1234654", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0116684", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1229822", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2639336", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2218003", 'budget'] = 15000000
df_raw.loc[df_raw['movie_id'] == "tt4731136", 'budget'] = 40000000
df_raw.loc[df_raw['movie_id'] == "tt2799166", 'budget'] = 6500000
df_raw.loc[df_raw['movie_id'] == "tt2226597", 'budget'] = 35000000
df_raw.loc[df_raw['movie_id'] == "tt1502712", 'budget'] = 120000000
df_raw.loc[df_raw['movie_id'] == "tt1172049", 'budget'] = 10000000
df_raw.loc[df_raw['movie_id'] == "tt3387266", 'budget'] = 14000000
df_raw.loc[df_raw['movie_id'] == "tt2837574", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0267891", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2872462", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0838221", 'budget'] = 16000000
df_raw.loc[df_raw['movie_id'] == "tt2273657", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0975645", 'budget'] = 15700000
df_raw.loc[df_raw['movie_id'] == "tt2056771", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1781058", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0145503", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5977276", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0808331", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1606392", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2112096", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1710417", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0790804", 'budget'] = 20000000
df_raw.loc[df_raw['movie_id'] == "tt5669936", 'budget'] = 25000000
df_raw.loc[df_raw['movie_id'] == "tt2784512", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4669296", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5666304", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4799066", 'budget'] = 2800000
df_raw.loc[df_raw['movie_id'] == "tt1183374", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2511428", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1082853", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0841044", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0275230", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt6980546", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1407084", 'budget'] = 5000000
df_raw.loc[df_raw['movie_id'] == "tt0352994", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0454776", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1226774", 'budget'] = 612650 * 1.6
df_raw.loc[df_raw['movie_id'] == "tt4686844", 'budget'] = 13000000
df_raw.loc[df_raw['movie_id'] == "tt3463106", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2944198", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1067765", 'budget'] = 4000000
df_raw.loc[df_raw['movie_id'] == "tt0989000", 'budget'] = 25000
df_raw.loc[df_raw['movie_id'] == "tt3577624", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1183665", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4714782", 'budget'] = 6000000
df_raw.loc[df_raw['movie_id'] == "tt3297330", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4977530", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1487118", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1320239", 'budget'] = 7500000 * 1.55
df_raw.loc[df_raw['movie_id'] == "tt5195412", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0420293", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1853643", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3208026", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2674430", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt7026672", 'budget'] = 4900000
df_raw.loc[df_raw['movie_id'] == "tt1433811", 'budget'] = 10000000
df_raw.loc[df_raw['movie_id'] == "tt2626350", 'budget'] = 45000000
df_raw.loc[df_raw['movie_id'] == "tt7242142", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4382872", 'budget'] = 12000000
df_raw.loc[df_raw['movie_id'] == "tt2490326", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1767372", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0376479", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3797868", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0475355", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2378507", 'budget'] = 9000000
df_raw.loc[df_raw['movie_id'] == "tt0443473", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2235779", 'budget'] = 200000
df_raw.loc[df_raw['movie_id'] == "tt0800003", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt6018306", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1389096", 'budget'] = 15000000
df_raw.loc[df_raw['movie_id'] == "tt0492044", 'budget'] = 10000000
df_raw.loc[df_raw['movie_id'] == "tt5670152", 'budget'] = 4000000
df_raw.loc[df_raw['movie_id'] == "tt0870211", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0361693", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0426615", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1521848", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0800027", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0780571", 'budget'] = 20000000
df_raw.loc[df_raw['movie_id'] == "tt5208252", 'budget'] = 24000000
df_raw.loc[df_raw['movie_id'] == "tt0489237", 'budget'] = 20000000
df_raw.loc[df_raw['movie_id'] == "tt1932767", 'budget'] = 6000000
df_raw.loc[df_raw['movie_id'] == "tt4383594", 'budget'] = 30000000
df_raw.loc[df_raw['movie_id'] == "tt4126438", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3824458", 'budget'] = 100000
df_raw.loc[df_raw['movie_id'] == "tt2870808", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2393845", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5886440", 'budget'] = 8000000 * 1.1
df_raw.loc[df_raw['movie_id'] == "tt1783732", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1133993", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1278449", 'budget'] = 4000000 * 1.3
df_raw.loc[df_raw['movie_id'] == "tt5989218", 'budget'] = 10000000
df_raw.loc[df_raw['movie_id'] == "tt1247690", 'budget'] = 30000000
df_raw.loc[df_raw['movie_id'] == "tt1045670", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0858479", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0427470", 'budget'] = 16000000
df_raw.loc[df_raw['movie_id'] == "tt0488120", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0433400", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0091875", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0768212", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0419984", 'budget'] = 22000000
df_raw.loc[df_raw['movie_id'] == "tt4334266", 'budget'] = 6000000
df_raw.loc[df_raw['movie_id'] == "tt5962210", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2883512", 'budget'] = 11000000
df_raw.loc[df_raw['movie_id'] == "tt1850397", 'budget'] = 14000000
df_raw.loc[df_raw['movie_id'] == "tt5655222", 'budget'] = 1200000
df_raw.loc[df_raw['movie_id'] == "tt3203620", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt6212478", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1046947", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0408236", 'budget'] = 50000000
df_raw.loc[df_raw['movie_id'] == "tt0408839", 'budget'] = 60000000
df_raw.loc[df_raw['movie_id'] == "tt0815245", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0477051", 'budget'] = 60000000
df_raw.loc[df_raw['movie_id'] == "tt1130988", 'budget'] = 10000000 * 1.5
df_raw.loc[df_raw['movie_id'] == "tt8291224", 'budget'] = 450000000 * 0.014
df_raw.loc[df_raw['movie_id'] == "tt4943322", 'budget'] = 40000000
df_raw.loc[df_raw['movie_id'] == "tt0757361", 'budget'] = 10000000
df_raw.loc[df_raw['movie_id'] == "tt4530422", 'budget'] = 38000000
df_raw.loc[df_raw['movie_id'] == "tt0110684", 'budget'] = 20000000
df_raw.loc[df_raw['movie_id'] == "tt0491175", 'budget'] = 25000000
df_raw.loc[df_raw['movie_id'] == "tt0404802", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0494834", 'budget'] = 20000000
df_raw.loc[df_raw['movie_id'] == "tt5607096", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1164999", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4291600", 'budget'] = 500000 * 1.25
df_raw.loc[df_raw['movie_id'] == "tt4258698", 'budget'] = 1500000
df_raw.loc[df_raw['movie_id'] == "tt0460890", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0460791", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3068194", 'budget'] = 3000000
df_raw.loc[df_raw['movie_id'] == "tt0903657", 'budget'] = 10000000
df_raw.loc[df_raw['movie_id'] == "tt3168230", 'budget'] = 11000000
df_raw.loc[df_raw['movie_id'] == "tt1720616", 'budget'] = 10000000
df_raw.loc[df_raw['movie_id'] == "tt1368440", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5628302", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1528071", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0830570", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4934950", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4814290", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1806913", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2339741", 'budget'] = 15000000
df_raw.loc[df_raw['movie_id'] == "tt3173910", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2356180", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt7212726", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1729637", 'budget'] = 600000000 * 0.02
df_raw.loc[df_raw['movie_id'] == "tt0315642", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt7485048", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5946128", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0456020", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0424823", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0452702", 'budget'] = 19000000
df_raw.loc[df_raw['movie_id'] == "tt0110889", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0486578", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt7668870", 'budget'] = 880000
df_raw.loc[df_raw['movie_id'] == "tt2624412", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2097331", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5304464", 'budget'] = 13600000
df_raw.loc[df_raw['movie_id'] == "tt5164184", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4326444", 'budget'] = 1350000 * 1.1
df_raw.loc[df_raw['movie_id'] == "tt0411195", 'budget'] = 1350000 * 1.2
df_raw.loc[df_raw['movie_id'] == "tt4048272", 'budget'] = 3000000 * 1.1
df_raw.loc[df_raw['movie_id'] == "tt2870756", 'budget'] = 16800000
df_raw.loc[df_raw['movie_id'] == "tt1023441", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1969062", 'budget'] = 6700000
df_raw.loc[df_raw['movie_id'] == "tt0364955", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0790770", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1490785", 'budget'] = 13000000
df_raw.loc[df_raw['movie_id'] == "tt3715320", 'budget'] = 11000000
df_raw.loc[df_raw['movie_id'] == "tt6217608", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3721964", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1661275", 'budget'] = 10000000 * 1.1
df_raw.loc[df_raw['movie_id'] == "tt5789976", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4005402", 'budget'] = 14000000
df_raw.loc[df_raw['movie_id'] == "tt0349467", 'budget'] = 37665000
df_raw.loc[df_raw['movie_id'] == "tt0457433", 'budget'] = 60795000
df_raw.loc[df_raw['movie_id'] == "tt0422774", 'budget'] = 28000000
df_raw.loc[df_raw['movie_id'] == "tt0080923", 'budget'] = 3000000
df_raw.loc[df_raw['movie_id'] == "tt0113755", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0897361", 'budget'] = 12000000
df_raw.loc[df_raw['movie_id'] == "tt0395495", 'budget'] = 25000000
df_raw.loc[df_raw['movie_id'] == "tt0838232", 'budget'] = 70000000
df_raw.loc[df_raw['movie_id'] == "tt0139151", 'budget'] = 15000000
df_raw.loc[df_raw['movie_id'] == "tt7074886", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt6905696", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1530983", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1146325", 'budget'] = 1000000 * 0.8
df_raw.loc[df_raw['movie_id'] == "tt0804516", 'budget'] = 8000000
df_raw.loc[df_raw['movie_id'] == "tt4437216", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4104022", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3774466", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0803057", 'budget'] = 8000000
df_raw.loc[df_raw['movie_id'] == "tt0370986", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1321511", 'budget'] = 30000000
df_raw.loc[df_raw['movie_id'] == "tt0292963", 'budget'] = 18000000
df_raw.loc[df_raw['movie_id'] == "tt0097790", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0444653", 'budget'] = 169000
df_raw.loc[df_raw['movie_id'] == "tt3416742", 'budget'] = 1600000
df_raw.loc[df_raw['movie_id'] == "tt6348138", 'budget'] = 100000000
df_raw.loc[df_raw['movie_id'] == "tt4864932", 'budget'] = 5200000
df_raw.loc[df_raw['movie_id'] == "tt4535650", 'budget'] = 1250000000 * 0.015
df_raw.loc[df_raw['movie_id'] == "tt4129428", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3859980", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3554418", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3390572", 'budget'] = 370000000 * 0.016
df_raw.loc[df_raw['movie_id'] == "tt3148502", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2344678", 'budget'] = 10000000
df_raw.loc[df_raw['movie_id'] == "tt0449994", 'budget'] = 400000000 * 0.022
df_raw.loc[df_raw['movie_id'] == "tt2112124", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1934231", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1734110", 'budget'] = 9000000 * 0.022
df_raw.loc[df_raw['movie_id'] == "tt1375789", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt4682788", 'budget'] = 14582000 * 1.1
df_raw.loc[df_raw['movie_id'] == "tt1084972", 'budget'] = 200000000 * 0.021
df_raw.loc[df_raw['movie_id'] == "tt0343737", 'budget'] = 110000000
df_raw.loc[df_raw['movie_id'] == "tt0113537", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0387514", 'budget'] = 22000000
df_raw.loc[df_raw['movie_id'] == "tt0384793", 'budget'] = 23000000
df_raw.loc[df_raw['movie_id'] == "tt0426883", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt8085790", 'budget'] = 20000000
df_raw.loc[df_raw['movie_id'] == "tt8079248", 'budget'] = 26000000
df_raw.loc[df_raw['movie_id'] == "tt6921996", 'budget'] = 25000000
df_raw.loc[df_raw['movie_id'] == "tt6911608", 'budget'] = 75000000
df_raw.loc[df_raw['movie_id'] == "tt0082801", 'budget'] = 8500000
df_raw.loc[df_raw['movie_id'] == "tt2616810", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2397535", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2012011", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt2395469", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt7721800", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0808399", 'budget'] = 14700000
df_raw.loc[df_raw['movie_id'] == "tt4468740", 'budget'] = 40000000
df_raw.loc[df_raw['movie_id'] == "tt0093793", 'budget'] = 18000000
df_raw.loc[df_raw['movie_id'] == "tt0450345", 'budget'] = 40000000
df_raw.loc[df_raw['movie_id'] == "tt0956038", 'budget'] = 30000000
df_raw.loc[df_raw['movie_id'] == "tt1951261", 'budget'] = 103000000
df_raw.loc[df_raw['movie_id'] == "tt0486583", 'budget'] = 100000000
df_raw.loc[df_raw['movie_id'] == "tt0821640", 'budget'] = 37500000
df_raw.loc[df_raw['movie_id'] == "tt4443658", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0119167", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt1172991", 'budget'] = 15000000
df_raw.loc[df_raw['movie_id'] == "tt2070776", 'budget'] = 13000000 * 1.3
df_raw.loc[df_raw['movie_id'] == "tt1800302", 'budget'] = 20000000
df_raw.loc[df_raw['movie_id'] == "tt1686821", 'budget'] = 30000000
df_raw.loc[df_raw['movie_id'] == "tt6173990", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0110678", 'budget'] = 20000000
df_raw.loc[df_raw['movie_id'] == "tt1786751", 'budget'] = 5000000
df_raw.loc[df_raw['movie_id'] == "tt0432289", 'budget'] = 8000000
df_raw.loc[df_raw['movie_id'] == "tt5108476", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt0375611", 'budget'] = 180000000 * 0.023
df_raw.loc[df_raw['movie_id'] == "tt1182937", 'budget'] = 220000000 * 0.022
df_raw.loc[df_raw['movie_id'] == "tt3767372", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt3495026", 'budget'] = 15670000
df_raw.loc[df_raw['movie_id'] == "tt1740710", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt7431594", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt6836936", 'budget'] = 350000000 * 0.014
df_raw.loc[df_raw['movie_id'] == "tt6588966", 'budget'] = 2000000
df_raw.loc[df_raw['movie_id'] == "tt6527426", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5997666", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt5970844", 'budget'] = 20000000
df_raw.loc[df_raw['movie_id'] == "tt5956100", 'budget'] = 20470000
df_raw.loc[df_raw['movie_id'] == "tt5882970", 'budget'] = 1550000000 * 0.015
df_raw.loc[df_raw['movie_id'] == "tt3405236", 'budget'] = '.'
df_raw.loc[df_raw['movie_id'] == "tt6988116", 'budget'] = 1500000000 * 0.013
df_raw.loc[df_raw['movie_id'] == "tt5286444", 'budget'] = 2900000



df_raw.to_csv('./raw/scrapping_budget.csv', header=True, index=False)
