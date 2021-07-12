import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

df_raw = pd.read_csv('./raw/movie_meta_last.csv', engine='python')
movie_id = df_raw['movie_id']

i = 0
for ids in movie_id:
    try:
        i += 1
        print(i)
        url = "https://www.imdb.com/title/{}/keywords?ref_=ttpl_ql_4".format(ids)
        resp = requests.get(url)
        html = resp.text
        soup = BeautifulSoup(html, "html5lib")
        tags_kwrds = soup.select("#keywords_content > table > tbody > tr > td > div.sodatext")

        text_kwrds = ""
        for tag in tags_kwrds:
            text_kwrds += tag.text
        if text_kwrds == '':
            df_raw.loc[df_raw['movie_id'] == ids, 'kwrds'] = '.'
        else:
            df_raw.loc[df_raw['movie_id'] == ids, 'kwrds'] = text_kwrds
    except:
        print(ids)

df_raw.to_csv('./raw/scrapping_kwrds.csv', header=True, index=False)
