from django.test import TestCase



import requests

url_pre = 'http://127.0.0.1:8000/'


def getUrlPre():
    global url_pre
    return url_pre


def getUrlLogin():
    global url_pre
    return url_pre + 'login/login/'


def getUrlRegister():
    global url_pre
    return url_pre + 'login/register/'


def getUrlCreateFood():
    """
    data = {
        'food_name': '名称',
        'price': '价格',
        'tags': '标签'
    }
    requests.post(url, data=data)
    """

    global url_pre
    return url_pre + 'food/createfood/'


def getUrlGetFoodByName():
    """
    requests.get(url, params=data)
    """

    global url_pre
    return url_pre + 'food/getfoodbyname/'

def getUrlBuyFood():
    global url_pre
    return url_pre + 'food/buyfood/'

def getUrlTopFood():
    global url_pre
    return url_pre + 'food/gettopfood/'

def getUrlPurchaseHistory():
    global url_pre
    return url_pre + 'food/getpurchasehistory/'

def getUrlDeletePurchaseHis():
    global url_pre
    return url_pre + 'food/deletepurchasehistory/'

def getUrlDeletePurchaseHis():
    global url_pre
    return url_pre + 'food/changepurchasehistory/'

def getUrlChangePurchaseHis():
    global url_pre
    return url_pre + 'food/changepurchasehistory/'

# ============================================= 相关函数

def isCorrectUser(username: str, password: str) -> bool:  # 判断一对用户名密码是否正确
    url = getUrlLogin()
    # 设置POST请求的数据
    data = {
        'username': username,
        'password': password
    }
    reply = requests.post(url, data=data)
    dic = reply.json()
    if dic['code'] == 200:
        return True
    else:
        return False


def checkRegisterInfo(username, password) -> str:  # 检查用户名和是否合法以及用户名是否存在
    # ret ''    ->  完全正确
    # ret '..'  ->  错误信息
    data = {
        'username': username,
        'password1': password,
        'password2': password
    }
    reply = requests.post(getUrlRegister(), data=data)
    dic = reply.json()
    if dic['code'] == 200:
        return ''
    else:
        errors = dic['errors']
        if 'username' in errors:
            return errors['username'][0]
        else:
            lst = errors['password2']
            return lst[0]


def getFoodByName(foodName: str):  # 失败返回None
    data = {
        'food_name': foodName
    }
    reply = requests.get(getUrlGetFoodByName(), params=data)
    dic = reply.json()
    if dic['code'] == 200:
        return dic['data']
    else:
        return None


def addFood(foodName, region_name, counter_name, price, tags, food_url):
    data = {
        'food_name': foodName,
        'region_name': region_name,
        'counter_name': counter_name,
        'price': price,
        'tags': tags,
        'food_url': food_url
    }
    reply = requests.post(getUrlCreateFood(), data=data)
    print(reply.text)
    dic = reply.json()
    if dic['code'] == 200:
        return True
    else:
        return False
    
def buyFood(foodName, user_name, rate=0.0):
    data = {
        'food_name': foodName,
        'user_name': user_name,
        'rate': rate
    }
    reply = requests.post(getUrlBuyFood(), data=data)
    dic = reply.json()
    if dic['code'] == 200:
        return True
    else:
        return False
    
def getTopFood():
    reply = requests.get(getUrlTopFood())
    dic = reply.json()
    if dic['code'] == 200:
        return True
    else:
        return False
    
    
def getPurchaseHistory(user_name):
    data = {
        'user_name': user_name
    }
    reply = requests.post(getUrlPurchaseHistory(), data=data)
    dic = reply.json()
    print(len(dic['data']))
    if dic['code'] == 200:
        return True
    else:
        return False
    
def deletePurchaseHistory(user_name, id):
    data = {
        'user_name': user_name,
        'id': id
    }
    reply = requests.post(getUrlDeletePurchaseHis(), data=data)
    dic = reply.json()
    if dic['code'] == 200:
        return True
    else:
        return False
    

def changePurchaseHistory(user_name, id, food_name, rate, date, time):
    data = {
        'user_name': user_name,
        'id': id,
        'food_name': food_name,
        'rate': rate,
        'date': date,
        'time': time
    }
    reply = requests.post(getUrlChangePurchaseHis(), data=data)
    dic = reply.json()
    if dic['code'] == 200:
        return True
    else:
        return False



# Create your tests here.
changePurchaseHistory('nr2', 19, '豆浆', 3, '2023-07-14', '其他')


