import pandas as pd
import numpy as np
import requests as rq
import json

# 1. 读取数据
f = open('foodlist5.csv', encoding='utf-8')
df = pd.read_csv(f)
# print(df.head())

url = 'http://127.0.0.1:18000/food/createfood/'
url1 = 'http://127.0.0.1:18000/food/createregion/'
url2 = 'http://127.0.0.1:18000/food/createcounter/'
unuploaded = []
regions = []
counters = []

for row in df.itertuples():
    print(row)
    if row[4] not in regions:
        regions.append(row[4])
        data = {
            'region_name': row[4],
        }
        r = rq.post(url1, data=data)
        print(r.json())
    if row[5] not in counters:
        counters.append(row[5])
        data = {
            'region_name': row[4],
            'counter_name': row[5],
        }
        r = rq.post(url2, data=data)
        print(r.json())
    data = {
        'food_name': row[2],
        'price': str(row[3]),
        'tags': ', '.join([str(row[7]), str(row[6]) if str(row[6]) != 'nan' else '' ]),
        'region_name': row[4],
        'counter_name': str(row[5]),
        'photo_url': '',
    }
    print(data)
    r = rq.post(url, data=data)

    try:
        print(r.json())
        if r.json()['code'] != 200:
            print('error')
            unuploaded.append(row)
            # break
    except json.decoder.JSONDecodeError:
        print(r.text)
        # break

    # break

errs = pd.DataFrame(unuploaded)
errs.to_csv('unuploaded4.csv', encoding='utf-8')