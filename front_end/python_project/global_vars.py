username_global = ''
url_pre = 'http://127.0.0.1:8000/'


def setUsername(name):
    global username_global
    username_global = name


def getUsername():
    global username_global
    return username_global
