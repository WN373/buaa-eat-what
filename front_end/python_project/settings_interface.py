# 个人设置界面: 个人头像, 昵称, 注册时间, 退出登录, 修改密码, 应用主题,
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QFrame
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

        self.modifyPasswordCard = ModifyPasswordCard(self)
        self.selfInfoGroup.addSettingCard(self.modifyPasswordCard)
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


from qfluentwidgets import CardWidget
class ModifyPasswordCard(QFrame):
    def __init__(self, parent=None):
        super().__init__()
        self.parentWidget = parent
        self.setFixedHeight(95)
        self.horMain = QtWidgets.QHBoxLayout(self)
        self.horMain.setContentsMargins(16, 0, 0, 0)
        from qfluentwidgets import IconWidget
        self.icon = IconWidget()
        self.icon.setIcon(QIcon('resource/images/modify.png'))
        self.icon.setFixedSize(16, 16)

        from qfluentwidgets import BodyLabel
        self.label = BodyLabel()
        self.label.setText('修改密码')



        from qfluentwidgets import LineEdit
        self.horEdit1 = QtWidgets.QHBoxLayout()
        self.edit1Label = BodyLabel()
        self.edit1Label.setText('新密码: ')
        self.horEdit1.addWidget(self.edit1Label)
        self.editPassword1 = LineEdit()
        self.editPassword1.setPlaceholderText('输入您的新密码 ~')
        self.editPassword1.setFixedWidth(200)
        self.horEdit1.addWidget(self.editPassword1)

        self.horEdit2 = QtWidgets.QHBoxLayout()
        self.edit2Label = BodyLabel()
        self.edit2Label.setText('确认密码: ')
        self.horEdit2.addWidget(self.edit2Label)
        self.editPassword2 = LineEdit()
        self.editPassword2.setPlaceholderText('请再次输入新密码 ~')
        self.editPassword2.setFixedWidth(200)

        self.editPassword1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPassword2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horEdit2.addWidget(self.editPassword2)

        self.ver = QtWidgets.QVBoxLayout()
        self.ver.addLayout(self.horEdit1)
        self.ver.addLayout(self.horEdit2)

        from qfluentwidgets import PrimaryPushButton
        self.button = PrimaryPushButton()
        self.button.setText('点击修改')

        self.horMain.addWidget(self.icon)
        self.horMain.addSpacing(16)
        self.horMain.addWidget(self.label)
        self.horMain.addStretch(1)
        self.horMain.addLayout(self.ver)
        self.horMain.addStretch(4)
        self.horMain.addWidget(self.button)
        self.horMain.addSpacing(18)
        self.setStyleSheet("""
            QFrame{
                background-color: rgb(253, 253, 253);
                border-radius: 6px;
                border: 1px;
            }
        """)
        self.button.clicked.connect(self.clickButton)

    def clickButton(self):
        from global_vars import username_global
        username = username_global
        password1 = self.editPassword1.text()
        password2 = self.editPassword2.text()
        if password1 != password2:
            self.showErrorTip(self.button, '两次输入密码不一致, 请重新输入')
        else:
            # 检查密码格式
            from url_communication import modifyPassword
            ret = modifyPassword(username, password2)
            from qfluentwidgets import InfoBar, InfoBarPosition
            if ret:
                self.editPassword1.setText('')
                self.editPassword2.setText('')
                InfoBar.success(
                    title='修改成功!',
                    content='',
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=2000,
                    parent=self.parentWidget
                )
            else:
                InfoBar.error(
                    title='修改失败!',
                    content='',
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=2000,
                    parent=self.parentWidget
                )
    def showErrorTip(self, target, content):
        from qfluentwidgets import TeachingTip, InfoBarIcon, TeachingTipTailPosition
        TeachingTip.create(
            target=target,
            icon=InfoBarIcon.ERROR,
            title='Error!',
            content=content,
            isClosable=True,
            tailPosition=TeachingTipTailPosition.TOP,
            duration=1000,
            parent=self
        )
