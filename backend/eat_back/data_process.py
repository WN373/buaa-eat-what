import pandas as pd
import numpy as np
import requests as rq
import json

# 1. 读取数据
f = open('foodlist2.csv', encoding='utf-8')
df = pd.read_csv(f)
# print(df.head())

url = 'http://127.0.0.1:18000/food/createfood/'
unuploaded = []

for row in df.itertuples():
    print(row)
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
errs.to_csv('unuploaded2.csv', encoding='utf-8')