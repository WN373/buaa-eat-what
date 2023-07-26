# 添加购买记录: 时间 + 购买备注
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, QtCore, QtGui

from TopShowCard import showTop15Window
from qfluentwidgets import CardWidget, StrongBodyLabel, IconWidget, TransparentToolButton, FluentIcon, BodyLabel, \
    InfoBar, InfoBarPosition, ScrollArea, TitleLabel, CaptionLabel, SubtitleLabel, LineEdit, ComboBox, \
    PrimaryPushButton, CalendarPicker


class AddBuyCard(CardWidget):
    def __init__(self, parent):
        super().__init__()
        self.parentWidget = parent

        self.verMain = QtWidgets.QVBoxLayout(self)
        self.buildTopHor()
        self.buildExplainHor()
        self.buildTimeHor()
        self.buildRemarkHor()
        self.buildAddButton()

        self.verMain.addLayout(self.horTop)
        self.verMain.addLayout(self.horExplain)
        self.verMain.addLayout(self.horTimePicker)
        self.verMain.addLayout(self.horRemark)
        self.verMain.addLayout(self.horButton)

        self.addButton.clicked.connect(self.clickAddButton)
        self.visitMoreStarButton.clicked.connect(self.clickVisitMoreStarButton)

    def clickAddButton(self):
        day = self.dayPicker.text()
        detailTime = self.detailPicker.text()
        remark = self.lineEdit.text()
        if day == '选择日期':
            self.showErrorInfo('请选择日期哦 ~')
        elif detailTime == '':
            self.showErrorInfo('请选择餐点哦 ~')
        elif remark == '':
            self.showErrorInfo('请输入购买备注哦 ~')
        else:
            # TODO 向数据库添加
            self.showSuccessInfo('添加成功!')

    def showErrorInfo(self, content):
        InfoBar.error(
            title=content,
            content='',
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self
        )

    def showSuccessInfo(self, content):
        InfoBar.success(
            title=content,
            content='',
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self
        )

    def clickVisitMoreStarButton(self):
        # 打开详细历史记录: 传一个图标, 一个标题, False->不显示金银铜牌子
        self.moreBuyShowWindow = showTop15Window(1)  # 借用一下这个列表
        self.moreBuyShowWindow.show()

    def buildTopHor(self):  # 创建顶层的水平布局
        self.horTop = QtWidgets.QHBoxLayout()
        # 顶层水平布局
        self.recordIcon = IconWidget(self)
        self.recordIcon.setMinimumSize(QtCore.QSize(20, 20))
        self.recordIcon.setMaximumSize(QtCore.QSize(20, 20))
        myRecordIcon = QtGui.QIcon()
        myRecordIcon.addPixmap(QtGui.QPixmap('resource/images/record.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recordIcon.setIcon(myRecordIcon)
        # 小标题
        self.recordTitleLabel = StrongBodyLabel(self)
        self.recordTitleLabel.setText('购买记录')
        self.visitMoreStarButton = TransparentToolButton(self)
        self.visitMoreStarButton.setIcon(FluentIcon.MORE)
        self.horTop.addWidget(self.recordIcon)
        self.horTop.addWidget(self.recordTitleLabel)
        self.horTop.addStretch()
        self.horTop.addWidget(self.visitMoreStarButton)

    def buildExplainHor(self):  # 创建说明的水平布局
        self.horExplain = QtWidgets.QHBoxLayout()
        self.explainLabel = BodyLabel(self)
        self.explainLabel.setProperty("lightColor", QtGui.QColor(96, 96, 96))
        self.explainLabel.setProperty("darkColor", QtGui.QColor(206, 206, 206))
        self.explainLabel.setText('选择时间并添加购买备注以记录您的足迹 ~')
        self.horExplain.addWidget(self.explainLabel)

    def buildTimeHor(self):  # 创建选择时间的水平布局
        self.horTimePicker = QtWidgets.QHBoxLayout()
        self.timeHint = BodyLabel()
        self.timeHint.setText('⏰选择日期: ')

        self.dayPicker = CalendarPicker()
        self.detailPicker = ComboBox()

        self.detailHint = BodyLabel()
        self.detailHint.setText('餐点: ')

        self.detailPicker.addItems(['早餐', '午餐', '晚餐', '其他'])
        self.timeCard = CardWidget()
        self.timeCardInHor = QtWidgets.QHBoxLayout(self.timeCard)
        # self.timeCardInHor.addWidget(self.timeIcon)
        self.timeCardInHor.addWidget(self.timeHint)
        self.timeCardInHor.addWidget(self.dayPicker)
        self.timeCardInHor.addStretch()
        self.timeCardInHor.addWidget(self.detailHint)
        self.timeCardInHor.addWidget(self.detailPicker)

        self.horTimePicker.addWidget(self.timeCard)

    def buildRemarkHor(self):
        self.horRemark = QtWidgets.QHBoxLayout()

        self.remarkCard = CardWidget()
        self.remarkInHor = QtWidgets.QHBoxLayout()
        self.remarkCard.setLayout(self.remarkInHor)
        self.remarkHint = BodyLabel()
        self.remarkHint.setText('📝购买备注: ')

        self.lineEdit = LineEdit()
        self.lineEdit.setPlaceholderText('在这里输入您对此条记录的备注哦 ~')
        self.remarkInHor.addWidget(self.remarkHint)
        self.remarkInHor.addWidget(self.lineEdit)
        self.horRemark.addWidget(self.remarkCard)

    def buildAddButton(self):
        self.horButton = QtWidgets.QHBoxLayout()
        self.addButton = PrimaryPushButton()
        self.addButton.setText('添加记录')
        self.addButton.setIcon(FluentIcon.ADD_TO)
        self.horButton.addStretch()
        self.horButton.addWidget(self.addButton)
        self.horButton.addStretch()
