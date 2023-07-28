# 登录界面
import json
import sys
import time

import requests
from PyQt5.QtCore import Qt, QTranslator, QLocale, QUrl, QByteArray
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager
from PyQt5.QtWidgets import QApplication, QWidget
from qframelesswindow import FramelessWindow, StandardTitleBar, AcrylicWindow
from qfluentwidgets import setThemeColor, FluentTranslator, setTheme, Theme, SplitTitleBar, TeachingTip, \
    TeachingTipTailPosition, InfoBarIcon, SplitFluentWindow, InfoBar, InfoBarPosition
from PyQt5 import QtCore, QtGui, QtWidgets
from main_interface import MainWindow
from register_interface import RegisterWindow


# 数据库函数 =======================================
def isCorrectUser(username: str, password: str) -> bool:  # 判断一对用户名密码是否正确
    a = 1  # TODO  可以在数据库文件里声明一个这样的函数, 我直接导入
    return True




# 数据库函数 =======================================


class Ui_Form_login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1250, 809)
        Form.setMinimumSize(QtCore.QSize(700, 500))
        # 创建水平布局
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")  # 这就是为这个对象(水平布局)起个名字
        # 构造函数创建一个label用于显示背景图片
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        # 创建一个widget作为水平布局的右侧
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(360, 0))
        self.widget.setMaximumSize(QtCore.QSize(360, 16777215))
        self.widget.setStyleSheet("QLabel{\n"
                                  "    font: 13px \'Microsoft YaHei\'\n"
                                  "}")
        self.widget.setObjectName("widget")
        # 创建一个垂直布局, 下属于widget
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # 用于水平居中
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        # 创建一个label, 显示图片logo
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        # 创建一个网格布局, 这是用来显示那个服务器的, 所以自然就用不到了
        # 创建一个label_5对象, 先加进去, 后面有专门的赋值函数
        self.label_5 = BodyLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)

        self.lineEdit_3 = LineEdit(self.widget)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.label_6 = BodyLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)

        self.lineEdit_4 = LineEdit(self.widget)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)  # 设置为密码输入框
        self.lineEdit_4.setClearButtonEnabled(True)  # 设置一键清空文本框内容的按钮是否可用
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)

        # 向verticalLayout_2中添加空白间距(占位符), 20为宽度, 5为高度
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)

        # 设置一个复选框, 表示是否记住密码
        self.checkBox = CheckBox(self.widget)
        self.checkBox.setChecked(True)  # 默认勾选
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)

        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)

        # 添加一个primaryPushButton用于点击
        self.pushButton = PrimaryPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)

        self.register_button = PrimaryPushButton(self.widget)
        self.register_button.setObjectName("register_button")
        self.verticalLayout_2.addWidget(self.register_button)
        self.register_button.setText('点击注册')
        spacerItem4 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)

        # 添加一个HyperlinkButton, 超链接按钮, 用于找回密码
        self.pushButton_2 = HyperlinkButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)

        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)

        # 把加了各种框框的widget添加给总体的水平布局
        self.horizontalLayout.addWidget(self.widget)

        # 为之前的条条框框上内容
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "用户名"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "请输入用户名"))
        self.label_6.setText(_translate("Form", "密码"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "请输入密码"))
        self.checkBox.setText(_translate("Form", "记住密码"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "找回密码"))


from qfluentwidgets import BodyLabel, CheckBox, HyperlinkButton, LineEdit, PrimaryPushButton
from resource_rc_files import resource_rc_login

class LoginWindow(AcrylicWindow, Ui_Form_login):
# class LoginWindow(SplitFluentWindow, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 让函数里配置的那些组件的父界面是self, 也就是登录窗口
        # setTheme(Theme.DARK)
        setThemeColor('#28afe9')  # 背景颜色

        self.setTitleBar(SplitTitleBar(self))  # titleBar 标题栏
        self.titleBar.raise_()

        self.label.setScaledContents(False)  # 图片缩放内容属性
        self.setWindowTitle('BUAA delicious Food')  # 窗口标题
        self.setWindowIcon(QIcon(":/images/logo.png"))  # 窗口标题图标
        self.resize(1000, 650)  # 设置窗口的大小

        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=False)  # 窗口特效
        self.setStyleSheet("LoginWindow{background: rgba(242, 242, 242, 0.8)}")
        # QLabel{
        #         background: transparent;
        #         font: 13px 'Segoe UI';  设置文字的大小和字体(consolas...)
        #         padding: 0 4px;  边距
        #         color: white  颜色
        #     }

        self.titleBar.titleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 13px 'Segoe UI';
                padding: 0 4px;
                color: white
            }
        """)
        # 这三行代码将窗口移动到屏幕中央
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.pushButton.clicked.connect(self.clickLogin)
        self.register_button.clicked.connect(self.clickRegister)

    def clickLogin(self):
        # global global_username
        username = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        import global_vars
        url = global_vars.getUrlLogin()

        # 设置POST请求的数据
        data = {
            'username': username,
            'password': password
        }
        reply = requests.post(url, data=data)
        dic = reply.json()
        if dic['code'] == 200:
            # 切换到主界面
            import global_vars
            global_vars.setUsername(username)
            self.close()
            self.toMainInterface = MainWindow()
            self.toMainInterface.show()
        else:
            # 账号密码输入错误, 重新输入
            TeachingTip.create(
                target=self.pushButton,
                icon=InfoBarIcon.ERROR,
                title='Error!',
                content="账号或密码错误, 请重新输入",
                isClosable=True,
                tailPosition=TeachingTipTailPosition.TOP,
                duration=1000,
                parent=self
            )

    def clickRegister(self):
        # 点击事件, 创建新的窗口
        self.registerWindow = RegisterWindow(self)
        self.registerWindow.show()

    def showSuccessRegister(self):
        InfoBar.success(
            title='',
            content='注册成功!',
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self
        )


    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap(":/images/background.jpg").scaled(
            self.label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)  # 1号label就是存左边的图片的


