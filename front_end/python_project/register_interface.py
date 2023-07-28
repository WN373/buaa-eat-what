import re
import sys
import time

import requests
from PyQt5.QtCore import Qt, QTranslator, QLocale
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget
from qframelesswindow import FramelessWindow, StandardTitleBar, AcrylicWindow
from qfluentwidgets import setThemeColor, FluentTranslator, setTheme, Theme, SplitTitleBar, TeachingTip, \
    TeachingTipTailPosition, InfoBarIcon, LineEdit, BodyLabel, PrimaryPushButton, StateToolTip, InfoBar, InfoBarPosition
from PyQt5 import QtCore, QtGui, QtWidgets
from main_interface import MainWindow
# 数据库函数 =======================================

def checkUsername(username: str) -> bool:
    # 检查长度是否满足要求
    if len(username) > 20:
        return False

    # 使用正则表达式检查是否只包含字母、数字、特殊字符@、.、-和_
    pattern = r'^[a-zA-Z0-9@.\-_]+$'
    if re.match(pattern, username):
        return True
    else:
        return False

def registerToDb(username: str, password: str):
    # 向数据库注册用户(此时的用户名和密码已经通过合法性检验, 直接存入数据库)
    a = 1


# 数据库函数 =======================================
class Ui_Form_register(object):
    def setupUi(self, Form):  # 给Form设置ui界面
        Form.setObjectName("Form")
        Form.resize(496, 500)
        Form.setMinimumSize(QtCore.QSize(496, 500))  # 设定在调整窗口大小时的最小大小
        # 创建一个窗口
        self.widget = QtWidgets.QWidget(Form)  # 设置父界面
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(360, 0))
        self.widget.setMaximumSize(QtCore.QSize(360, 16777215))
        # self.widget.setContentsMargins(70, 0, 0, 0)  # 貌似是这个窗体的内边距
        self.widget.setStyleSheet("QLabel{\n"
                                  "    font: 13px \'Microsoft YaHei\'\n"
                                  "}")
        self.widget.setObjectName("widget")
        # 垂直布局
        self.verLayout = QtWidgets.QVBoxLayout(self.widget)  # 该模块的父亲木块是self
        self.verLayout.setContentsMargins(130, 0, 0, 0)  # 这个函数设置的是本身(本身不变)和外框之间的间距
        self.verLayout.setSpacing(9)
        self.verLayout.setObjectName("verLayout")

        spacerItem = QtWidgets.QSpacerItem(2, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verLayout.addItem(spacerItem)

        # logo显示
        self.label_logo = QtWidgets.QLabel(self.widget)
        self.label_logo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy)
        self.label_logo.setMinimumSize(QtCore.QSize(50, 50))
        self.label_logo.setMaximumSize(QtCore.QSize(50, 50))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(":/images/logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.verLayout.addWidget(self.label_logo, 0, QtCore.Qt.AlignCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verLayout.addItem(spacerItem1)

        # 标签: 提示用户名
        self.usernameHint_label = BodyLabel(self.widget)
        self.usernameHint_label.setObjectName("usernameHint_label")
        self.usernameHint_label.setText("用户名")
        self.verLayout.addWidget(self.usernameHint_label)

        # 文本框
        self.username_edit = LineEdit(self.widget)
        self.username_edit.setClearButtonEnabled(True)
        self.username_edit.setPlaceholderText("请输入用户名")
        self.username_edit.setObjectName("username")
        self.verLayout.addWidget(self.username_edit)

        # 标签: 提示密码
        self.passwordHint_label = BodyLabel(self.widget)
        self.passwordHint_label.setText("密码")
        self.passwordHint_label.setObjectName("passwordHint_label")
        self.verLayout.addWidget(self.passwordHint_label)

        # 文本框: 输入密码
        self.password_edit = LineEdit(self.widget)
        self.password_edit.setClearButtonEnabled(True)
        self.password_edit.setPlaceholderText("至少8个字符, 不可全为数字")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_edit")
        self.verLayout.addWidget(self.password_edit)

        # 标签: 提示密码
        self.passwordHint2_label = BodyLabel(self.widget)
        self.passwordHint2_label.setText("确认密码")
        self.passwordHint2_label.setObjectName("passwordHint_label")
        self.verLayout.addWidget(self.passwordHint2_label)

        # 文本框: 输入密码
        self.password_edit2 = LineEdit(self.widget)
        self.password_edit2.setClearButtonEnabled(True)
        self.password_edit2.setPlaceholderText("请再次输入密码")
        self.password_edit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit2.setObjectName("password_edit")
        self.verLayout.addWidget(self.password_edit2)

        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verLayout.addItem(spacerItem3)

        # 按钮: 确认注册
        self.register_button = PrimaryPushButton(self.widget)
        self.register_button.setObjectName("register_button")
        self.register_button.setText("确认注册")
        self.verLayout.addWidget(self.register_button)

        QtCore.QMetaObject.connectSlotsByName(Form)


class RegisterWindow(AcrylicWindow, Ui_Form_register):
    def __init__(self, login_interface):
        super().__init__()
        self.setupUi(self)
        setThemeColor('#28afe9')  # 背景颜色
        self.parent = login_interface
        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()

        self.label_logo.setScaledContents(True)  # 图片缩放内容属性
        self.setWindowTitle('Register')
        self.setWindowIcon(QIcon(":/images/logo.png"))

        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=False)
        self.setStyleSheet("RegisterWindow{background: rgba(242, 242, 242, 0.8)}")

        self.titleBar.titleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 13px 'Segoe UI';
                padding: 0 4px
                color: white
            }
        """)

        self.register_button.clicked.connect(self.clickRegister)

    def clickRegister(self):
        username = self.username_edit.text()
        password1 = self.password_edit.text()
        password2 = self.password_edit2.text()
        if username == '':
            self.showErrorTip(self.username_edit, "请输入用户名")
        elif password1 == '':
            self.showErrorTip(self.password_edit, "请输入密码")
        elif password2 == '':
            self.showErrorTip(self.password_edit2, "请确认密码")
        elif password1 == password2:
            from url_communication import checkRegisterInfo
            ret = checkRegisterInfo(username, password2)
            if ret == '':  # 注册成功
                registerToDb(username, password1)
                self.stateTooltip = StateToolTip('', '', self)
                self.stateTooltip.setContent('注册成功!')
                self.stateTooltip.setState(True)
                self.stateTooltip.show()
                self.parent.showSuccessRegister()
                self.close()
            else:
                InfoBar.error(
                    title='注册失败',
                    content=ret,
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.BOTTOM,
                    duration=2000,
                    parent=self
                )
        elif password1 != password2:
            self.showErrorTip(self.register_button, "两次输入密码不一致, 请重新输入")

    def showErrorTip(self, target, content):
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

    def resizeEvent(self, e):
        super().resizeEvent(e)






