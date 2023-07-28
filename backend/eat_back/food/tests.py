from django.test import TestCase
import requests


def buyFood(foodName, username):
    data = {
        'food_name': foodName,
        'username': username 
    }
    reply = requests.post('http://127.0.0.1:8000/food/buyfood/', data=data)
    print(reply.text)
    return
    dic = reply.json()
    if dic['code'] == 200:
        return True
    else:
        return False
    
def addFood(foodName, price, tags):
    data = {
        'food_name': foodName,
        'price': price,
        'tags': tags
    }
    reply = requests.post('http://127.0.0.1:8000/food/createfood/', data=data)
    dic = reply.json()
    if dic['code'] == 200:
        print(dic['msg'])
        return True
    else:
        print(dic['msg'])
        return False

# Create your tests here.
buyFood('豆浆','myk')
