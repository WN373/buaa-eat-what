username_global = ''
url_pre = 'http://127.0.0.1:8000/'
# global username_global


def setUsername(name):
    global username_global
    username_global = name


def getUsername():
    global username_global
    return username_global


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


