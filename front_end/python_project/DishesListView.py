# 这个文件写一些和排列菜品有关的界面
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon, QFont
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPlainTextEdit

from qfluentwidgets import BodyLabel
from home_interface import DishDetailWindow
from qfluentwidgets import ScrollArea, TitleLabel, CaptionLabel, FluentIcon, PushButton, StrongBodyLabel, ToolButton, \
    TransparentToolButton, CardWidget, setThemeColor, CheckBox, PrimaryPushButton, InfoBar, InfoBarPosition, TextEdit, \
    SearchLineEdit, LineEdit, LineEditButton, IconWidget, SubtitleLabel


class MySearchLineEdit(LineEdit):
    def __init__(self, searchRange, parent):
        super().__init__()
        self.parentWidget = parent
        self.searchRange = searchRange  # 本搜索框搜索的范围
        self.searchButton = LineEditButton(FluentIcon.SEARCH, self)
        self.hBoxLayout.addWidget(self.searchButton, 0, Qt.AlignRight)
        self.setTextMargins(0, 0, 59, 0)
        self.searchButton.clicked.connect(self.clickSearch)
        self.setPlaceholderText('在这里输入要搜索的内容哦 ~')

    def search(word: str, allWordList: list) -> list:
        # 使用列表推导式找出匹配项及其匹配度，并将其存储为元组 (匹配项, 匹配度)
        matching_items = [(item, word.count(item)) for item in allWordList if word in item]
        # 使用sorted函数按照匹配度从高到低排序匹配项
        sorted_matching_items = sorted(matching_items, key=lambda x: x[1], reverse=True)
        # 返回排序后的匹配项
        return [item[0] for item in sorted_matching_items]

    def clickSearch(self):
        # 根据一定的搜索算法去搜索
        searchContent = self.text()
        if searchContent == '':
            InfoBar.error(
                title='您还没有输入内容哦 ~',
                content='',
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self.parentWidget
            )
            return 0
        # TODO 根据搜索的内容show出新的dishesListView
        print('正在搜索嗷!!!')


class DishesListView(CardWidget):
    def __init__(self, windowTitle, iconTitle, listType=0, dishList=[]):
        """
        参数:
        dishList: 要展示出来的菜对象
        listType: 界面类型
            == 1, 表示 查看某食堂某柜台的菜
        """

        super().__init__()
        self.windowTitle = windowTitle
        self.iconTitle = iconTitle

        self.setWindowTitle(self.windowTitle)
        self.setWindowIcon(self.iconTitle)
        # 总体垂直布局
        self.verWholeLayout = QtWidgets.QVBoxLayout(self)
        # 第0层: 修饰
        self.hor0 = QtWidgets.QHBoxLayout()
        self.hor0.addStretch()
        self.icon0 = IconWidget()
        self.icon0.setIcon(QIcon('resource/images/heart.png'))
        self.icon0.setFixedSize(45, 45)
        self.hor0.addWidget(self.icon0)
        self.subTitle = SubtitleLabel()
        self.subTitle.setText('我的收藏')
        self.hor0.addWidget(self.subTitle)
        self.hor0.addStretch()
        self.verWholeLayout.addSpacing(15)
        self.verWholeLayout.addLayout(self.hor0)
        # self.verWholeLayout.addSpacing(5)
        # 第一层: 一个水平布局, 主体为 搜索框: 把所有包含这几个字的都显示出来, 并且按照匹配度(简化为包含的字的个数)自高到低排序
        self.horLayout1 = QtWidgets.QHBoxLayout()
        self.verWholeLayout.addLayout(self.horLayout1)
        self.verWholeLayout.addSpacing(10)
        self.searchWindow = MySearchLineEdit([], self)
        self.horLayout1.addSpacing(60)
        self.tempVer = QtWidgets.QVBoxLayout()
        self.tempVer.addSpacing(30)
        if listType == 1:
            self.tempHor = QtWidgets.QHBoxLayout()
            self.tempHor.addWidget(self.searchWindow)
            self.addButton = ToolButton()
            self.addButton.setIcon(FluentIcon.ADD_TO)
            self.tempHor.addWidget(self.addButton)
            self.addButton.clicked.connect(self.clickAddButton)
            self.tempVer.addLayout(self.tempHor, Qt.AlignVCenter)
        else:
            self.tempVer.addWidget(self.searchWindow, Qt.AlignVCenter)
        self.tempVer.addSpacing(10)
        self.horLayout1.addLayout(self.tempVer)
        self.horLayout1.addSpacing(60)
        # 第二层: 一个水平布局, 主体为一个gridLayout
        self.horLayout2 = QtWidgets.QHBoxLayout()
        self.verWholeLayout.addLayout(self.horLayout2)
        self.horLayout2.addSpacing(50)
        self.mainWidget = QWidget()
        self.horLayout2.addWidget(self.mainWidget)
        self.horLayout2.addSpacing(50)
        # 下面布置这个scrollView, 里面是一个垂直布局, 上面是grid, 下面是space
        self.mainGridLayout = QtWidgets.QGridLayout()
        self.mainWidget.setLayout(self.mainGridLayout)
        self.scrollArea = ScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.mainGridLayout.addWidget(self.scrollArea)
        self.window = QWidget()
        self.scrollArea.setWidget(self.window)
        self.realGridLayout = QtWidgets.QGridLayout()
        self.window.setLayout(self.realGridLayout)
        self.realGridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.realGridLayout.setContentsMargins(20, 40, 20, 20)
        self.realGridLayout.setSpacing(12)
        self.setFixedSize(670, 750)  # 设置固定的大小, 这样的话, 无法用鼠标改变它的大小
        self.setGrids()

    class AddFoodWindow(CardWidget):  # 输入要添加的食堂名
        class EditItem(CardWidget):
            def __init__(self, labelName, hint):
                super().__init__()
                self.labelName = labelName
                self.hint = hint

                self.editLine = LineEdit()
                self.editLine.setPlaceholderText(hint)

                self.horEdit = QtWidgets.QHBoxLayout(self)
                self.horEditLabel = BodyLabel()
                self.horEditLabel.setText(str(labelName) + ': ')
                self.horEdit.addSpacing(40)
                self.horEdit.addWidget(self.horEditLabel)
                self.horEdit.addWidget(self.editLine)
                # self.horEdit.addSpacing(40)
                self.setFixedWidth(330)

        def __init__(self, parent=None):  # 此parent其实是parent的parent, 而不是ToolBar
            super().__init__()
            self.parentWidget = parent
            self.setWindowTitle('添加菜品')
            self.setWindowIcon(QIcon(':/images/logo.png'))
            self.verMain = QtWidgets.QVBoxLayout(self)
            self.verMain.addSpacing(30)
            self.verMain.setContentsMargins(20, 0, 20, 0)
            self.editName = self.EditItem('菜名', '在这里输入菜名')
            self.editPrice = self.EditItem('价格', '在这里输入价格, 注意加单位')
            self.editTags = self.EditItem('标签', '注意以逗号分隔')

            self.verMain.addWidget(self.editName)
            self.verMain.addWidget(self.editPrice)
            self.verMain.addWidget(self.editTags)

            self.verMain.addSpacing(10)

            self.horButton = QtWidgets.QHBoxLayout()
            self.button = PrimaryPushButton()
            self.button.setText('点击添加')
            self.horButton.addStretch()
            self.horButton.addWidget(self.button)
            self.horButton.addStretch()
            self.verMain.addLayout(self.horButton)
            self.verMain.addSpacing(25)
            self.button.clicked.connect(self.clickButton)
            self.resize(400, 250)

        def clickButton(self):
            text = self.editLine.text()
            if text == '':
                InfoBar.error(
                    title='添加失败!',
                    content='输入的内容不能为空',
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=2000,
                    parent=self
                )
            else:
                InfoBar.success(
                    title='添加成功!',
                    content='',
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=2000,
                    parent=self.parentWidget
                )
                # 数据库, 给食堂列表添加一个食堂  TODO
                card = self.parentWidget.addCard(text, ['resource/images/find.png', 'resource/images/star_yes.png',
                                                        'resource/images/delete.png'], self.parentWidget)
                self.parentWidget.lst.append(card)
                self.close()

    def clickAddButton(self):
        # 弹出一个窗口, 填添加菜品的信息
        self.addInfoWindow = self.AddFoodWindow()
        self.addInfoWindow.show()


    def setGrids(self):
        # TODO 这里访问数据库, 展示真正的 dishCard
        self.realGridLayout.addWidget(self.DishCard(), 0, 0)
        self.realGridLayout.addWidget(self.DishCard(), 0, 1)
        self.realGridLayout.addWidget(self.DishCard(), 1, 1)
        self.realGridLayout.addWidget(self.DishCard(), 2, 1)

    class DishCard(CardWidget):
        def __init__(self):
            super().__init__()

            self.verWholeLayout = QtWidgets.QVBoxLayout(self)
            self.horLayout = QtWidgets.QHBoxLayout()
            self.verWholeLayout.addLayout(self.horLayout)
            # 下面布置这个verLayout2
            self.imageLabel = QLabel()
            # TODO 数据库
            self.imageLabel.setPixmap(QtGui.QPixmap(":/images/logo.png"))
            self.imageLabel.setFixedSize(130, 130)
            self.imageLabel.setScaledContents(True)
            self.horLayout.addSpacing(10)
            self.horLayout.addWidget(self.imageLabel)
            self.buildVerIcon()
            self.horLayout.addLayout(self.verIcon)
            # 一个收藏量, 一个查看详情
            self.hor2 = QtWidgets.QHBoxLayout()
            self.hor2.addSpacing(25)
            # 米饭logo
            self.riceIcon = IconWidget()
            self.riceIcon.setIcon(QIcon("resource/images/rice.png"))
            self.riceIcon.setFixedSize(15, 15)
            self.hor2.addWidget(self.riceIcon)
            self.hor2.addSpacing(10)
            self.nameLabel = QLabel()
            # TODO 这里要替换成数据库查询来的名字
            self.nameLabel.setText('土豆炖鲸鱼')
            self.nameLabel.setStyleSheet("""
                QLabel{
                    background: transparent;
                    font: 12px 'Microsoft YaHei';
                    padding: 0 0px;
                    color: rgb(0, 143, 212)
                }
            """)
            self.hor2.addWidget(self.nameLabel, Qt.AlignHCenter)
            self.hor2.addStretch()
            # 查看详情的按钮
            self.findButton = TransparentToolButton()
            self.findButton.setIcon(FluentIcon.SEARCH)
            self.hor2.addWidget(self.findButton)
            self.hor2.addSpacing(22)
            self.findButton.clicked.connect(self.clickFindButton)
            self.verWholeLayout.addLayout(self.hor2)

        def buildVerIcon(self):
            self.verIcon = QtWidgets.QVBoxLayout()
            # star
            self.horStar = QtWidgets.QHBoxLayout()
            self.starLabel = QLabel()
            self.starLabel.setPixmap(QtGui.QPixmap("resource/images/star_yes.png"))
            self.starLabel.setFixedSize(14, 14)  # 设置标签的大小(不代表里面的内容的大小)
            self.starLabel.setScaledContents(True)  # 让内容随着label大小的变化而做出适应变化
            self.countStarLabel = QLabel()
            self.countStarLabel.setText('13')
            self.countStarLabel.setStyleSheet("""
                QLabel{
                    background: transparent;
                    font: 12px 'Microsoft YaHei';
                    padding: 0 0px;
                    color: black
                }
            """)
            self.horStar.addStretch()
            self.horStar.addWidget(self.starLabel)
            self.horStar.addWidget(self.countStarLabel)
            self.horStar.addSpacing(22)
            self.verIcon.addLayout(self.horStar)
            # buy
            self.horBuy = QtWidgets.QHBoxLayout()
            self.buyLabel = QLabel()
            self.buyLabel.setPixmap(QtGui.QPixmap("resource/images/buy_yes.png"))
            self.buyLabel.setFixedSize(14, 14)
            self.buyLabel.setScaledContents(True)
            self.buyCountLabel = QLabel()
            self.buyCountLabel.setText('14')
            self.buyCountLabel.setStyleSheet("""
                QLabel{
                    background: transparent;
                    font: 12px 'Microsoft YaHei';
                    padding: 0 0px;
                    color: black
                }
            """)
            self.horBuy.addStretch()
            self.horBuy.addWidget(self.buyLabel)
            self.horBuy.addWidget(self.buyCountLabel)
            self.horBuy.addSpacing(22)
            self.verIcon.addLayout(self.horBuy)
            # chat
            self.horChat = QtWidgets.QHBoxLayout()
            self.chatLabel = QLabel()
            self.chatLabel.setPixmap(QtGui.QPixmap("resource/images/comment.png"))
            self.chatLabel.setFixedSize(14, 14)
            self.chatLabel.setScaledContents(True)
            self.chatCountLabel = QLabel()
            self.chatCountLabel.setText('14')
            self.chatCountLabel.setStyleSheet("""
                QLabel{
                    background: transparent;
                    font: 12px 'Microsoft YaHei';
                    padding: 0 0px;
                    color: black
                }
            """)
            self.horChat.addStretch()
            self.horChat.addWidget(self.chatLabel)
            self.horChat.addWidget(self.chatCountLabel)
            self.horChat.addSpacing(22)
            self.verIcon.addLayout(self.horChat)

        def clickFindButton(self):
            # TODO 调出来这道菜的页面, 查数据库
            self.findDetailWindow = DishDetailWindow()
            self.findDetailWindow.show()
