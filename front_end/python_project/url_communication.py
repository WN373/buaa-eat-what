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


def addFood(foodName, price, tags):
    data = {
        'food_name': foodName,
        'price': price,
        'tags': tags
    }
    reply = requests.post(getUrlCreateFood(), data=data)
    dic = reply.json()
    if dic['code'] == 200:
        return True
    else:
        return False



