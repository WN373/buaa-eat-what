# 个人设置界面: 个人头像, 昵称, 注册时间, 退出登录, 修改密码, 应用主题,
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import QtWidgets

from qfluentwidgets import FluentIcon as FIF, OptionsSettingCard
from qfluentwidgets import ScrollArea, ExpandLayout, SettingCardGroup, PrimaryPushSettingCard


class MySettingsWindow(ScrollArea):
    def __init__(self, mainWindow, parent=None):
        super().__init__()
        self.parent = mainWindow
        self.selfInfoGroup = None
        self.setObjectName("MySettingsWindow")
        # self.resize(867, 781)

        # 设置QScrollArea区域的背景色
        self.setStyleSheet("""
            QScrollArea{
                background-color: rgb(249, 249, 249);
                border: none;            
            }
        """)

        # 设置标签
        self.settingLabel = QLabel('设置', self)
        self.settingLabel.move(60, 30)
        self.settingLabel.setObjectName("settingLabel")
        self.settingLabel.setStyleSheet("""
            QLabel{
                background-color: transparent;
                font: 33px 'Microsoft YaHei Light';
            }
        """)

        # 整体框架
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        self.setWidget(self.scrollWidget)

        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 120, 0, 20)
        self.setWidgetResizable(True)
        self.initGroups()
        self.addGroups()
        self.setCardEffect()

    def initGroups(self):
        # 个人信息
        self.selfInfoGroup = SettingCardGroup("个人信息", self.scrollWidget)
        self.informationCard = PrimaryPushSettingCard(
            "退出登录",
            FIF.PEOPLE,
            "宁然",
            "Register date: 2023-01-02",
            self.selfInfoGroup
        )
        self.selfInfoGroup.addSettingCard(self.informationCard)

        # 个性化
        # class mytest():
        #     def __init__(self):
        #         self.name = 'ThemeMode'


        # self.personalGroup = SettingCardGroup('个性化', self.scrollWidget)
        # self.themeCard = OptionsSettingCard(
        #     mytest(),
        #     '应用主题',
        #     '改变应用的外观',
        #     texts=['亮色', '暗色'],
        #     parent=self.personalGroup
        # )
        # self.personalGroup.addSettingCard(self.themeCard)

    def addGroups(self):
        # self.selfInfoGroup.addSettingCard(self)
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(60, 10, 60, 0)
        self.expandLayout.addWidget(self.selfInfoGroup)
        # self.expandLayout.addWidget(self.personalGroup)

    def setCardEffect(self):  # 比如: 设置按钮点击效果
        self.informationCard.clicked.connect(self.exitUpLoad)

    def exitUpLoad(self):
        # 退出登录
        from login_interface import LoginWindow
        self.toLogin = LoginWindow()
        self.toLogin.show()
        self.parent.close()
