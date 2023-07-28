# 主界面: 个人设置/推荐菜品/全部菜品/我的收藏/个人足迹/必吃 TOP10/

import sys

from PyQt5.QtCore import Qt, QTranslator, QLocale, QUrl
from PyQt5.QtGui import QIcon, QPixmap, QDesktopServices
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from qframelesswindow import FramelessWindow, StandardTitleBar, AcrylicWindow

from MulClassShow import MulClassShow
from home_interface import HomeWindow
from settings_interface import MySettingsWindow
from qfluentwidgets import setThemeColor, FluentTranslator, setTheme, Theme, SplitTitleBar, CalendarPicker, \
    SplitFluentWindow, MessageBox, NavigationAvatarWidget, NavigationItemPosition, FluentIcon, FluentWindow, InfoBar, \
    InfoBarPosition
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(FluentWindow):

    def __init__(self):
        super().__init__()
        # setTheme(Theme.DARK)
        # self.setStyleSheet('Demo{background: white}')
        self.homeWindow = HomeWindow(self)
        self.addSubInterface(self.homeWindow, FluentIcon.HOME, '首页')
        self.settingsWindow = MySettingsWindow(self)
        self.addSubInterface(self.settingsWindow, FluentIcon.SETTING, '个人设置', NavigationItemPosition.BOTTOM)
        self.hallsWindow = MulClassShow([], '食堂一览', '在这里可以找到所有食堂, 柜台, 菜品的信息哦 ~', self)
        self.hallsWindow.setObjectName('hallsWindow')
        self.addSubInterface(self.hallsWindow, QIcon('resource/images/all.png'), '食堂一览')
        self.resize(900, 700)
        self.setWindowTitle('wuhu!!!!!!')
        self.setWindowIcon(QIcon(":/images/logo.png"))

        InfoBar.success(
            title='欢迎回来!',
            content='宁然',
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self
        )
