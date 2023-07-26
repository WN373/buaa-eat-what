# 这个card用来展示占据热榜前几名的菜(热度相同的话按照字典序排)
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from qfluentwidgets import CardWidget, StrongBodyLabel, IconWidget, TransparentToolButton, FluentIcon, BodyLabel, \
    InfoBar, InfoBarPosition, ScrollArea, TitleLabel, CaptionLabel, SubtitleLabel, LineEdit, ComboBox, \
    PrimaryPushButton, ProgressRing, SpinBox, LargeTitleLabel, TableWidget


class TopShowCard(CardWidget):
    def __init__(self, parent):
        self.parentWidget = parent
        super().__init__()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(380, 410))
        self.setMaximumSize(QtCore.QSize(600, 410))
        self.setObjectName("topShowCard")
        # 总体垂直布局
        self.verWholeLayout = QtWidgets.QVBoxLayout(self)
        self.verWholeLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verWholeLayout.addSpacing(5)
        # 第一层
        self.hor1 = QtWidgets.QHBoxLayout()
        self.verWholeLayout.addLayout(self.hor1)
        self.hor1.setContentsMargins(5, -1, -1, -1)  # 水平布局内容间距
        self.hor1Icon = IconWidget(self)
        self.hor1Icon.setFixedSize(20, 20)
        hotIcon = QtGui.QIcon()
        hotIcon.addPixmap(QtGui.QPixmap('resource/images/hot.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hor1Icon.setIcon(hotIcon)
        # 标签
        self.myHotTitleLabel = StrongBodyLabel(self)
        self.myHotTitleLabel.setText('热门必吃 TOP 8')
        # 三个按钮
        self.spinBox = SpinBox()
        self.spinBox.setRange(0, 8)
        self.spinBox.setFixedHeight(29)
        self.hor1AddButton = TransparentToolButton()
        self.hor1AddButton.setIcon(QIcon('resource/images/add.png'))
        self.hor1SubButton = TransparentToolButton()
        self.hor1SubButton.setIcon(QIcon('resource/images/sub.png'))
        self.hor1MoreButton = TransparentToolButton()
        self.hor1MoreButton.setIcon(FluentIcon.MORE)

        # 添加进水平布局
        self.hor1.addWidget(self.hor1Icon)
        self.hor1.addWidget(self.myHotTitleLabel)
        self.hor1.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        )
        self.hor1.addWidget(self.hor1AddButton)
        self.hor1.addWidget(self.hor1SubButton)
        # self.hor1.addWidget(self.spinBox)
        self.hor1.addWidget(self.hor1MoreButton)
        self.verWholeLayout.addSpacing(30)
        # 子标题
        self.topLabel = SubtitleLabel(self)
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setText('必吃榜')
        self.verWholeLayout.addWidget(self.topLabel)

        # 必吃榜下面是一个水平布局: 垂直(star)+垂直+垂直(buy)
        self.hor = QtWidgets.QHBoxLayout()
        self.hor.addStretch()
        self.verWholeLayout.addLayout(self.hor)
        self.ver1 = QtWidgets.QVBoxLayout()
        self.ver2 = QtWidgets.QVBoxLayout()
        self.ver3 = QtWidgets.QVBoxLayout()
        # ver1
        self.ver1.setContentsMargins(0, 10, 0, 0)
        self.ver1.addSpacing(30)
        self.starIcon = IconWidget(self)
        self.starIcon.setFixedSize(20, 20)
        self.starIcon.setIcon(QIcon('resource/images/star_yes.png'))
        self.starCountLabel = LargeTitleLabel()
        # TODO 这里应该查数据库
        self.starCountLabel.setText('3')
        self.starNameLabel = BodyLabel()
        self.starNameLabel.setText('收藏')

        self.ver1hor1 = QtWidgets.QHBoxLayout()
        self.ver1hor2 = QtWidgets.QHBoxLayout()
        self.ver1hor3 = QtWidgets.QHBoxLayout()
        self.ver1hor1.addWidget(self.starIcon)
        self.ver1hor2.addWidget(self.starCountLabel)
        self.ver1hor3.addWidget(self.starNameLabel)
        self.ver1hor1.addStretch()
        self.ver1hor1.setContentsMargins(5, 0, 0, 0)
        self.ver1hor2.setContentsMargins(5, 0, 0, 0)
        self.ver1.addLayout(self.ver1hor1)
        self.ver1.addLayout(self.ver1hor2)
        self.ver1.addLayout(self.ver1hor3)
        self.ver1.addStretch()
        self.hor.addLayout(self.ver1)
        self.hor.addStretch()
        # ver2
        self.buildProgressRing()
        self.ver2.addWidget(self.progressRing)
        self.ver2Widget = QWidget()
        self.ver2Widget.setLayout(self.ver2)
        self.hor.addWidget(self.ver2Widget)
        self.ver2Widget.setFixedWidth(200)
        self.hor.addStretch()
        self.ver2hor1 = QtWidgets.QHBoxLayout()
        self.priceLabel = BodyLabel()
        self.priceLabel.setText('价格: 23 元/份')
        self.ver2hor1.addStretch()
        self.ver2hor1.addWidget(self.priceLabel)
        self.ver2hor1.addStretch()
        self.ver2.addLayout(self.ver2hor1)
        self.ver2.addStretch()
        # ver3
        self.ver3.setContentsMargins(0, 10, 0, 0)
        self.ver3.addSpacing(30)
        self.buyIcon = IconWidget(self)
        self.buyIcon.setFixedSize(20, 20)
        self.buyIcon.setIcon(QIcon('resource/images/buy_yes.png'))
        self.buyCountLabel = LargeTitleLabel()
        # TODO 这里应该查数据库
        self.buyCountLabel.setText('5')
        self.buyNameLabel = BodyLabel()
        self.buyNameLabel.setText('购买')

        self.ver3hor1 = QtWidgets.QHBoxLayout()
        self.ver3hor2 = QtWidgets.QHBoxLayout()
        self.ver3hor3 = QtWidgets.QHBoxLayout()
        self.ver3hor1.addWidget(self.buyIcon)
        self.ver3hor2.addWidget(self.buyCountLabel)
        self.ver3hor3.addWidget(self.buyNameLabel)
        self.ver3hor1.addStretch()
        self.ver3hor1.setContentsMargins(5, 0, 0, 0)
        self.ver3hor2.setContentsMargins(5, 0, 0, 0)
        self.ver3.addLayout(self.ver3hor1)
        self.ver3.addLayout(self.ver3hor2)
        self.ver3.addLayout(self.ver3hor3)
        self.ver3.addStretch()
        self.hor.addLayout(self.ver3)
        self.hor.addStretch()

    def resetShowDish(self):  # 根据菜排名, 重新设置提示菜品
        now_val = self.spinBox.value()
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setWeight(50)
        if str(now_val) == '0':
            font.setPointSize(10)
            font.setPointSize(10)
            self.progressRing.setFont(font)
            self.progressRing.setFormat('快点右上角的加号!!')
            return 0
        font.setPointSize(12)
        self.progressRing.setFont(font)
        realNo = 9 - now_val
        # TODO 这个需要查数据库得到这个排名的具体的菜名
        dishName = '土豆炖鲸鱼'
        self.progressRing.setFormat('Top ' + str(realNo) + ' ' + dishName)

    def clickAddButton(self):
        new_val = self.spinBox.value() + 1
        self.spinBox.setValue(new_val)
        self.resetShowDish()

    def clickSubButton(self):
        new_val = self.spinBox.value() - 1
        self.spinBox.setValue(new_val)
        self.resetShowDish()

    def clickMoreButton(self):
        # 展示出top15
        self.topShowWindow = showTop15Window(0)
        self.topShowWindow.show()

    def buildProgressRing(self):
        # 进程表
        self.progressRing = ProgressRing()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.progressRing.sizePolicy().hasHeightForWidth())
        self.progressRing.setSizePolicy(sizePolicy)
        self.progressRing.setMinimumSize(QtCore.QSize(150, 150))
        self.progressRing.setMaximumSize(QtCore.QSize(220, 220))
        self.progressRing.setMaximum(8)  # 钟表示的最大数值
        self.progressRing.setAlignment(QtCore.Qt.AlignCenter)
        self.progressRing.setTextVisible(True)
        self.progressRing.setOrientation(QtCore.Qt.Horizontal)
        self.progressRing.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressRing.setUseAni(False)
        self.progressRing.setStrokeWidth(15)  # 设置圆环的环截面的宽度
        self.progressRing.setObjectName("progressRing")
        self.verWholeLayout.addWidget(self.progressRing)
        self.hor1AddButton.clicked.connect(self.clickAddButton)
        self.hor1SubButton.clicked.connect(self.clickSubButton)
        self.spinBox.valueChanged.connect(self.progressRing.setValue)
        self.hor1MoreButton.clicked.connect(self.clickMoreButton)
        self.resetShowDish()


class showTop15Window(CardWidget):
    # def __init__(self, lst):  # lst里面取前15道菜即可
    def __init__(self, mode):
        super().__init__()
        self.mode = mode  # 0->top15展示  1->购买记录展示
        self.buildHorTitle()
        self.verMain = QtWidgets.QVBoxLayout(self)
        self.verMain.addSpacing(20)
        self.verMain.addLayout(self.horTitle)
        self.verMain.addSpacing(15)
        self.setWindowTitle('必吃 TOP 15')
        self.setWindowIcon(QIcon('resource/images/hot.png'))
        self.horMain = QtWidgets.QHBoxLayout()
        self.verMain.addLayout(self.horMain)
        self.horMain.addSpacing(20)
        self.ver1 = QtWidgets.QVBoxLayout()
        self.ver1.addSpacing(53)
        self.icon1 = IconWidget()
        self.icon1.setIcon(QIcon('resource/images/no1.png'))
        self.icon2 = IconWidget()
        self.icon2.setIcon(QIcon('resource/images/no2.png'))
        self.icon3 = IconWidget()
        self.icon3.setIcon(QIcon('resource/images/no3.png'))
        self.icon1.setFixedSize(20, 20)
        self.icon2.setFixedSize(20, 20)
        self.icon3.setFixedSize(20, 20)
        self.ver1.addWidget(self.icon1)
        self.ver1.addSpacing(11)
        self.ver1.addWidget(self.icon2)
        self.ver1.addSpacing(13)
        self.ver1.addWidget(self.icon3)
        self.ver1.addStretch()
        if self.mode == 0:  # == 0的话才是展示top模式, 才需要加牌子
            self.horMain.addLayout(self.ver1)
        else:
            self.horMain.addSpacing(24)
        self.tableView = TableWidget(self)
        self.tableView.setWordWrap(False)
        self.tableView.setRowCount(15)
        self.tableView.setColumnCount(6)
        self.dishList = []
        for i in range(15):
            self.dishList.append([str(i + 1), '土豆炖鲸鱼', '学二一层', '12', '13', '0.5元/碗'])

        for i, entry in enumerate(self.dishList):
            for j in range(6):
                tempItem = QTableWidgetItem(entry[j])
                if j == 1:
                    tempItem.setForeground(QColor(84, 150, 205))
                if j == 0:
                    if i < 3:
                        tempItem.setForeground(QColor(241, 111, 133))
                    else:
                        tempItem.setForeground(QColor(255, 131, 44))
                self.tableView.setItem(i, j, tempItem)
        self.tableView.verticalHeader().hide()
        self.tableView.setHorizontalHeaderLabels(
            ['序号', '菜名', '售卖点', '购买量', '收藏量', '价格'])
        # self.tableView.resizeColumnsToContents()
        self.setStyleSheet("showTop20Window{background: rgb(249, 249, 249)} ")
        self.horMain.setContentsMargins(0, 0, 0, 0)
        self.horMain.addWidget(self.tableView)
        self.setFixedSize(720, 780)

    def buildHorTitle(self):
        self.horTitle = QtWidgets.QHBoxLayout()
        self.horTitle.addStretch()
        self.iconCup = IconWidget()
        self.iconCup.setIcon(QIcon('resource/images/praise_cup.png'))
        self.iconCup.setFixedSize(45, 45)
        self.horTitle.addWidget(self.iconCup)
        self.subTitle = SubtitleLabel()
        self.subTitle.setText('必吃 TOP 15')
        self.horTitle.addWidget(self.subTitle)
        self.horTitle.addStretch()

