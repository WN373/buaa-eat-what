username_global = ''
# global username_global


def setUsername(name):
    global username_global
    username_global = name


def getUsername():
    global username_global
    return username_global
