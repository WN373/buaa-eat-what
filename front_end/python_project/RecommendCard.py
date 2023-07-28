# 该界面是 home_interface 中四个卡片之一的推荐菜品卡片
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, QtCore, QtGui

from qfluentwidgets import CardWidget, StrongBodyLabel, IconWidget, TransparentToolButton, FluentIcon, BodyLabel, \
    InfoBar, InfoBarPosition, ScrollArea, TitleLabel, CaptionLabel, SubtitleLabel, LineEdit, ComboBox, PrimaryPushButton


class RecommendCard(CardWidget):
    def __init__(self, parent):
        super().__init__()
        self.parentWidget = parent
        # 配置一下自己的大小
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(380, 410))
        self.setMaximumSize(QtCore.QSize(600, 410))
        self.setObjectName("recCard")

        # 总体垂直布局
        self.verWholeLayout = QtWidgets.QVBoxLayout(self)
        self.verWholeLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verWholeLayout.addSpacing(12)
        # 第一层
        self.hor1 = QtWidgets.QHBoxLayout()
        self.verWholeLayout.addLayout(self.hor1)
        self.hor1.setContentsMargins(5, -1, -1, -1)  # 水平布局内容间距
        self.hor1Icon = IconWidget(self)
        self.hor1Icon.setFixedSize(20, 20)
        recIcon = QtGui.QIcon()
        recIcon.addPixmap(QtGui.QPixmap('resource/images/recommend.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hor1Icon.setIcon(recIcon)
        # 标签
        self.myRecTitleLabel = StrongBodyLabel(self)
        self.myRecTitleLabel.setText('推荐菜品')
        self.hor1Icon2 = IconWidget(self)
        self.hor1Icon2.setFixedSize(20, 20)
        rightIcon = QtGui.QIcon()
        rightIcon.addPixmap(QtGui.QPixmap('resource/images/todo.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hor1Icon2.setIcon(rightIcon)
        # 添加进水平布局
        self.hor1.addWidget(self.hor1Icon)
        self.hor1.addWidget(self.myRecTitleLabel)
        self.hor1.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        )
        self.hor1.addWidget(self.hor1Icon2)

        # 第二层: 水平布局
        self.hor2 = QtWidgets.QHBoxLayout()
        self.verWholeLayout.addLayout(self.hor2)
        self.hor2.addSpacing(20)
        self.verMain = QtWidgets.QVBoxLayout()
        self.hor2.addLayout(self.verMain)
        self.hor2.addSpacing(20)
        self.verMain.addSpacing(20)
        # 标签
        self.titleLabel = SubtitleLabel(self)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setText('菜品推荐')
        self.verMain.addWidget(self.titleLabel)
        # 注释说明
        self.hintLabel = BodyLabel(self)
        self.hintLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hintLabel.setText("""
            我们将根据您提供的就餐时间和口味偏好以及您添加的历史购买记录来为您推荐合适的菜品, 以满足您的就餐需求。
        """)
        self.hintLabel.setWordWrap(True)
        self.hintLabel.setProperty("lightColor", QtGui.QColor(96, 96, 96))
        self.hintLabel.setProperty("darkColor", QtGui.QColor(206, 206, 206))
        self.hintLabel.setObjectName('hintLabel')
        self.verMain.addWidget(self.hintLabel)
        # 一个行输入框(为了调节他的大小, 下面用一个水平布局包住他)
        self.tempHor1 = QtWidgets.QHBoxLayout()
        self.tempHor1.addSpacing(90)
        self.lineEdit = LineEdit()
        self.lineEdit.setPlaceholderText('请输入您的口味偏好哦 ~')
        self.tempHor1.addWidget(self.lineEdit)
        self.tempHor1.addSpacing(90)
        self.verMain.addLayout(self.tempHor1)
        self.verMain.addSpacing(10)
        # 一个标签, 提示选择框的作用
        self.bottomHintLabel = BodyLabel(self)
        self.bottomHintLabel.setAlignment(QtCore.Qt.AlignCenter)  # 让标签文字居中
        self.bottomHintLabel.setText('在这里选择您的就餐时间。')
        self.verMain.addWidget(self.bottomHintLabel)

        self.verMain.addSpacing(5)
        # 单选框
        self.tempHor2 = QtWidgets.QHBoxLayout()
        self.tempHor2.addSpacing(200)
        self.selectBox = ComboBox()
        self.selectBox.addItems(['早餐', '午餐', '晚餐', '随意'])
        self.selectBox.setCurrentIndex(0)
        self.setMinimumWidth(200)
        self.tempHor2.addWidget(self.selectBox)
        self.tempHor2.addSpacing(210)
        self.verMain.addLayout(self.tempHor2)

        self.verMain.addSpacing(20)
        # 生成推荐 按钮
        self.tempHor3 = QtWidgets.QHBoxLayout()
        self.tempHor3.addSpacing(167)
        self.beginButton = PrimaryPushButton()
        self.beginButton.setText('生成推荐')
        # self.beginButton.setAutoDefault(True)
        self.tempHor3.addWidget(self.beginButton)
        self.tempHor3.addSpacing(175)
        self.verMain.addLayout(self.tempHor3)
        self.beginButton.setIcon(FluentIcon.POWER_BUTTON)
        self.verMain.addStretch()
        self.beginButton.clicked.connect(self.clickBeginButton)

    def clickBeginButton(self):
        # 出来推荐界面, 就是生成一个 DishesListView
        preferenceContent = self.lineEdit.text()
        eatTime = self.selectBox.text()
        from DishesListView import DishesListView
        self.recInterface = DishesListView('推荐生成', QIcon(':/images/logo.png'))  # 需要传进去参数, 根据具体的参数生成具体的listView
        self.recInterface.show()
