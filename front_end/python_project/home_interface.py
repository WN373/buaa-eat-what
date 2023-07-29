# 家界面
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QGraphicsBlurEffect, QVBoxLayout
from PyQt5 import QtWidgets, QtCore, QtGui

from AddBuyCard import AddBuyCard
from CommentArea import CommentArea, ReplyWindow
from RecommendCard import RecommendCard
from TopShowCard import TopShowCard
from qfluentwidgets import CardWidget, StrongBodyLabel, IconWidget, TransparentToolButton, FluentIcon, BodyLabel, \
    InfoBar, InfoBarPosition, ScrollArea, TitleLabel, CaptionLabel



class HomeWindow(QWidget):
    def __init__(self, parentWidget):
        super().__init__()
        self.topLoc = (0, 1)
        self.starLoc = (1, 0)
        self.recLoc = (0, 0)
        self.buyLoc = (1, 1)
        self.parentWidget = parentWidget
        self.setObjectName('homeWindow')
        self.initGridLayout()
        self.addMyStarGrid()
        # self.signalToSlot()
        self.addRecCard()
        self.addTopShowCard()
        self.addBuyCard()

    def initGridLayout(self):
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 40, 20, 20)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName("gridLayout")

    def addRecCard(self):
        self.recCard = RecommendCard(self)
        self.gridLayout.addWidget(self.recCard, self.recLoc[0], self.recLoc[1], 1, 1)

    def addTopShowCard(self):
        self.topShowCard = TopShowCard(self)
        self.gridLayout.addWidget(self.topShowCard, self.topLoc[0], self.topLoc[1], 1, 1)

    def addBuyCard(self):
        self.buyCard = AddBuyCard(self)
        self.gridLayout.addWidget(self.buyCard, self.buyLoc[0], self.buyLoc[1], 1, 1)

    def addMyStarGrid(self):
        # 加收藏card
        self.myStarCard = CardWidget(self)
        self.myStarCard.setMinimumSize(QtCore.QSize(370, 0))
        self.myStarCard.setMaximumSize(QtCore.QSize(600, 395))
        self.myStarCard.setMinimumSize(QtCore.QSize(370, 0))  # 最小高度一定不能太高, 不然的话屏幕就显示不全了
        self.myStarCard.setMaximumSize(QtCore.QSize(600, 395))
        self.myStarCard.setObjectName("myStarCard")
        # 整体的垂直布局
        self.myStarVerLayout = QtWidgets.QVBoxLayout(self.myStarCard)
        self.myStarVerLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)  # 大小为默认约束
        self.myStarVerLayout.setObjectName('myStarVerLayout')
        # 顶层的水平布局
        self.myStarHorLayout = QtWidgets.QHBoxLayout()
        self.myStarHorLayout.setContentsMargins(5, -1, -1, -1)  # 水平布局内容间距 -> 指布局内边距
        self.myStarHorLayout.setObjectName('myStarHorLayout')

        self.initStarLayoutComponent()
        self.addStarComponentToLayout()
        # 加小格标题

    def initStarLayoutComponent(self):  # 初始化布局的组成元件
        # 顶层水平布局
        # 小icon
        self.starIconWid = IconWidget(self.myStarCard)
        self.starIconWid.setMinimumSize(QtCore.QSize(20, 20))
        self.starIconWid.setMaximumSize(QtCore.QSize(20, 20))
        starIcon = QtGui.QIcon()
        starIcon.addPixmap(QtGui.QPixmap('resource/images/star3.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.starIconWid.setIcon(starIcon)
        self.starIconWid.setObjectName('starIconWid')
        # 小标题
        self.myStarTitleLabel = StrongBodyLabel(self.myStarCard)
        self.myStarTitleLabel.setText('我的收藏')
        # 按钮 —— 查看更多
        # self.visitMoreStarButton = TransparentToolButton(self.myStarCard)
        # self.visitMoreStarButton.setObjectName('visitMoreButton')
        # self.visitMoreStarButton.setIcon(FluentIcon.MORE)
        # logo - heart2
        self.heartLogo = IconWidget()
        self.heartLogo.setIcon(QIcon('resource/images/heart2.png'))
        self.heartLogo.setFixedSize(25, 25)

    def addStarComponentToLayout(self):
        # grid添加
        self.gridLayout.addWidget(self.myStarCard, self.starLoc[0], self.starLoc[1], 1, 1)
        # star 顶层水平
        self.myStarHorLayout.addWidget(self.starIconWid)
        self.myStarHorLayout.addWidget(self.myStarTitleLabel)
        self.myStarHorLayout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.myStarHorLayout.addWidget(self.heartLogo)
        # star 全局垂直
        self.myStarVerLayout.addLayout(self.myStarHorLayout)
        self.initShowItems()


    def clickAddStarDishButton(self):  # 不应该在这里点添加收藏
        # 应该弹出一个窗口, 添加收藏
        print('看到你点击添加收藏啦!!!')

    def clickVisitMoreStarButton(self):
        # TODO 这里查询数据库传参来显示对应的画面
        from DishesListView import DishesListView
        self.findAllStarView = DishesListView('全部收藏', QIcon(':/images/logo.png'))
        self.findAllStarView.show()

    def initShowItems(self):
        # self.starShowItemList = []
        # for i in range(4):
        #     self.starShowItemList.append(StarShowItem('待添加', '', '', self.myStarCard, self))
        #     self.myStarVerLayout.addWidget(self.starShowItemList[i])
        # self.myStarVerLayout.addStretch()
        self.starCard1 = SubStarCard('🏬 食堂收藏', cardType=0)
        self.starCard2 = SubStarCard('🍱 柜台收藏', cardType=1)
        self.starCard3 = SubStarCard('🍔 菜品收藏', cardType=2)
        self.starShowVer = QtWidgets.QVBoxLayout()
        self.starShowVer.addSpacing(10)
        self.starShowVer.addWidget(self.starCard1)
        self.starShowVer.addSpacing(10)
        self.starShowVer.addWidget(self.starCard2)
        self.starShowVer.addSpacing(10)
        self.starShowVer.addWidget(self.starCard3)
        self.starShowVer.addSpacing(10)
        # self.starShowVer 现在这里装有三个card
        self.iconHeart = IconWidget()
        self.iconHeart.setIcon(QIcon('resource/images/heart.png'))
        self.iconHeart.setFixedSize(110, 110)
        self.hor2Main = QtWidgets.QHBoxLayout()
        self.hor2Main.addStretch()
        self.verIconHeart = QtWidgets.QVBoxLayout()
        self.verIconHeart.addStretch()
        self.verIconHeart.addWidget(self.iconHeart)
        self.verIconHeart.addStretch()
        # self.hor2Main.addWidget(self.iconHeart)
        self.hor2Main.addLayout(self.verIconHeart)
        self.hor2Main.addStretch()
        self.hor2Main.addLayout(self.starShowVer)
        self.hor2Main.addStretch()
        self.myStarVerLayout.addSpacing(10)
        self.myStarVerLayout.addLayout(self.hor2Main)
        self.myStarVerLayout.addStretch()


class SubStarCard(CardWidget):
    # 一个文字提示 + 一个查看详情的图标
    def __init__(self, labelText: str, cardType=0):
        """
        cardType ->
            0: 食堂
            1: 柜台
            2: 菜品
        """
        super().__init__()
        self.labelText = labelText
        self.cardType = cardType
        self.setContentsMargins(15, 0, 0, 0)
        self.horMain = QtWidgets.QHBoxLayout(self)
        self.hintLabel = BodyLabel()
        self.hintLabel.setText(labelText)
        self.horMain.addWidget(self.hintLabel)
        self.horMain.addStretch()
        self.iconButton = TransparentToolButton()
        self.iconButton.setIcon(FluentIcon.SEARCH)
        self.iconButton.setFixedSize(15, 15)
        self.horMain.addWidget(self.iconButton)
        self.horMain.addSpacing(15)
        self.iconButton.clicked.connect(self.clickIconButton)
        self.setFixedWidth(210)

    def clickIconButton(self):
        from MulClassShow import MulClassShow
        from MulClassShowCounter import MulClassShowCounter
        if self.cardType == 0:  # 食堂收藏
           self.hallStarWindow = MulClassShow([], '食堂收藏', '在这里可以看到您所有收藏的食堂的信息哦 ~', showType=1)
           self.hallStarWindow.show()
        elif self.cardType == 1:  # 柜台收藏
            self.gridStarWindow = MulClassShowCounter([], '柜台收藏', '在这里可以看到您所有收藏的柜台的信息哦 ~', showType=1)
            self.gridStarWindow.show()
        elif self.cardType == 2:  # 菜品收藏
            from DishesListView import DishesListView
            self.starDishes = DishesListView('收藏菜品', QIcon('resource/images/star_yes.png'), listType=1)
            self.starDishes.show()

# class StarShowItem(QWidget):
#     def __init__(self, dishName, dinnerLocation, price, parent, homeWindow):
#         super().__init__()
#         self.parentWidget = parent
#         self.homeWindow = homeWindow
#         self.horLayout = QtWidgets.QHBoxLayout(self)
#         if dinnerLocation == '':
#             self.isNull = True  # 现在是空的
#
#         self.lookStarDetailButton = TransparentToolButton()
#         self.lookStarDetailButton.setObjectName('lookStarDetailButton')
#         self.lookStarDetailButton.setIcon(FluentIcon.SEARCH)
#         self.horLayout.addWidget(self.lookStarDetailButton)
#
#         self.deleteStarDishButton = TransparentToolButton()
#         self.deleteStarDishButton.setObjectName('deleteStarDishButton')
#         self.deleteStarDishButton.setIcon(FluentIcon.DELETE)
#         self.horLayout.addWidget(self.deleteStarDishButton)
#
#         self.dishNameLabel = BodyLabel()
#         self.dishNameLabel.setText(dishName)
#         self.priceLabel = BodyLabel()
#         self.priceLabel.setText(price)
#         self.dinnerLocationLabel = BodyLabel()
#         self.dinnerLocationLabel.setText(dinnerLocation)
#         self.horLayout.addWidget(self.dishNameLabel)
#         self.horLayout.addWidget(self.dinnerLocationLabel)
#         self.horLayout.addWidget(self.priceLabel)
#
#         self.deleteStarDishButton.clicked.connect(self.clickDelete)
#         self.lookStarDetailButton.clicked.connect(self.clickSearch)
#         self.setFixedHeight(40)
#
#     def deleteSelf(self):
#         self.reset('待添加', '', '')
#         self.isNull = True
#
#     def reset(self, dishName, dinnerLocation, price):
#         self.dishNameLabel.setText(dishName)
#         self.dinnerLocationLabel.setText(dinnerLocation)
#         self.priceLabel.setText(price)
#         self.isNull = False
#
#     def clickDelete(self):
#         if self.isNull:
#             InfoBar.info(
#                 title='无法删除尚未添加的内容哦',
#                 content='',
#                 orient=Qt.Horizontal,
#                 isClosable=True,
#                 position=InfoBarPosition.TOP,
#                 duration=2000,
#                 parent=self.parentWidget
#             )
#         else:
#             InfoBar.info(
#                 title='成功删除',
#                 content=self.dishNameLabel.text(),
#                 orient=Qt.Horizontal,
#                 isClosable=True,
#                 position=InfoBarPosition.TOP,
#                 duration=2000,
#                 parent=self.parentWidget
#             )
#             self.deleteSelf()
#
#     def clickSearch(self):
#         if self.isNull:  # 是空的话, 弹窗提示无法查看
#             InfoBar.info(
#                 title='无法查看尚未添加的内容哦',
#                 content='',
#                 orient=Qt.Horizontal,
#                 isClosable=True,
#                 position=InfoBarPosition.TOP,
#                 duration=2000,
#                 parent=self.parentWidget
#             )
#             self.homeWindow.starShowItemList[1].reset('土豆炖鲸鱼🐋', '学二食堂', '0.5元 / 份')
#         else:
#             # 打开某道菜品的详情界面
#             self.testWindow = DishDetailWindow()
#             self.testWindow.show()


class DishDetailWindow(CardWidget):  # 该窗口类用于展示一道菜品的详细信息, 包括评论等
    # 所有的菜的卡片都可以收藏/购买, 但是一定是在这个窗口类点击的相关的按钮
    class InfoItemWidget(QWidget):
        def __init__(self, itemName, commentArea):
            super().__init__()
            self.commentArea = commentArea
            self.horLayout = QtWidgets.QHBoxLayout(self)
            self.horLayout.setObjectName('horLayout')
            self.itemName = itemName
            # 图标
            self.iconButton = TransparentToolButton()
            self.iconButton.setObjectName('iconButton')
            self.itemChineseName = ''
            self.showContent = '查数据库'
            if self.itemName == 'comment':  # 评论
                self.iconButton.setIcon(FluentIcon.CHAT)
                self.itemChineseName = '评论数'
            elif self.itemName == 'star':
                self.iconButton.setIcon(QIcon('resource/images/star_no.png'))
                self.itemChineseName = '收藏数'
            elif self.itemName == 'buy':
                self.iconButton.setIcon(QIcon('resource/images/buy_no.png'))
                self.itemChineseName = '购买数'
            elif self.itemName == 'price':
                self.iconButton.setIcon(QIcon('resource/images/price.png'))
                self.itemChineseName = '价   格'
            elif self.itemName == 'location':
                self.iconButton.setIcon(QIcon('resource/images/location.png'))
                self.itemChineseName = '售卖地'

            self.horLayout.addWidget(self.iconButton)
            self.itemNameLabel = BodyLabel()
            self.setObjectName('itemNameLabel')
            self.itemNameLabel.setText(self.itemChineseName)
            self.horLayout.addWidget(self.itemNameLabel)
            # FIXME 这里需要查数据库
            self.itemContentLabel = BodyLabel()
            self.itemContentLabel.setText(self.showContent)
            self.itemContentLabel.setObjectName('itemContentLabel')
            self.horLayout.addWidget(self.itemContentLabel)
            self.iconButton.clicked.connect(self.clickIconButton)

        def clickIconButton(self):
            # 如果是收藏/购买, 要换个图标, 如果是评论, 要开启评论弹窗, 如果是价格就不用动
            if self.itemName == 'star':
                isStar = False
                """
                如果这个用户已经收藏了这个菜, 那么图标要变亮, 否则要变暗
                """
                if not isStar:
                    self.iconButton.setIcon(QIcon('resource/images/star_yes.png'))
                    # TODO 添加到数据库收藏
                else:
                    self.iconButton.setIcon(QIcon('resource/images/star_no.png'))
            elif self.itemName == 'buy':
                isBuy = False
                """
                购买的逻辑同上
                """
                if not isBuy:
                    self.iconButton.setIcon(QIcon('resource/images/buy_yes.png'))
                    # TODO 添加到数据库购买
                else:
                    self.iconButton.setIcon(QIcon('resource/images/buy_no.png'))
            elif self.itemName == 'comment':
                # parent, replyObject
                self.commentWindow = ReplyWindow(self.commentArea, '')
                self.commentWindow.show()

    # 菜品图片, 收藏数, 购买量 (水平布局)
    # 评论 scroll
    def __init__(self):
        super().__init__()
        self.resize(600, 700)
        self.setMinimumSize(QtCore.QSize(600, 700))

        # 先把这个评论区new出来
        self.commentArea = CommentArea('评论', '哎呦, 不错哦, 发条评论吧 ~')
        self.commentArea.setObjectName('commentArea')

        self.setWindowTitle('土豆炖鲸鱼🐋')
        self.setWindowIcon(QIcon(":/images/logo.png"))
        # 总体上是一个垂直布局
        self.verWholeLayout = QtWidgets.QVBoxLayout(self)
        self.verWholeLayout.setObjectName('verWholeLayout')

        self.horLayout = QtWidgets.QHBoxLayout()  # TODO 添加到总体垂直

        self.dishImageLabel = QtWidgets.QLabel(self)
        self.dishImageLabel.setPixmap(QtGui.QPixmap(":/images/logo.png"))
        self.dishImageLabel.setObjectName('dishImageLabel')

        self.horLayout.addWidget(self.dishImageLabel)

        # 接下来是一个垂直布局, 用来显示这个菜的各个信息
        self.verInfoLayout = QtWidgets.QVBoxLayout()
        self.verInfoLayout.setObjectName('verInfoLayout')
        self.verInfoLayout.setSpacing(0)  # 设置垂直排列的多个控件之间的间距

        self.infoItemWidget1 = self.InfoItemWidget('star', self.commentArea)
        self.infoItemWidget1.setObjectName('infoItemWidget1')
        self.infoItemWidget2 = self.InfoItemWidget('buy', self.commentArea)
        self.infoItemWidget2.setObjectName('infoItemWidget2')
        self.infoItemWidget3 = self.InfoItemWidget('comment', self.commentArea)
        self.infoItemWidget3.setObjectName('infoItemWidget3')
        self.infoItemWidget4 = self.InfoItemWidget('location', self.commentArea)
        self.infoItemWidget4.setObjectName('infoItemWidget4')
        self.infoItemWidget5 = self.InfoItemWidget('price', self.commentArea)
        self.infoItemWidget5.setObjectName('infoItemWidget5')
        self.infoItemWidget1.setFixedHeight(35)
        self.infoItemWidget2.setFixedHeight(35)
        self.infoItemWidget3.setFixedHeight(35)
        self.infoItemWidget4.setFixedHeight(35)
        self.infoItemWidget5.setFixedHeight(35)

        self.verInfoLayout.addWidget(self.infoItemWidget1)
        self.verInfoLayout.addWidget(self.infoItemWidget2)
        self.verInfoLayout.addWidget(self.infoItemWidget3)
        self.verInfoLayout.addWidget(self.infoItemWidget4)
        self.verInfoLayout.addWidget(self.infoItemWidget5)

        self.horLayout.addLayout(self.verInfoLayout)
        self.verWholeLayout.addLayout(self.horLayout)
        # 下面是评论区, 先建一个下侧垂直布局
        self.belowVerLayout = QtWidgets.QVBoxLayout()
        self.belowVerLayout.setObjectName('belowVerLayout')
        self.verWholeLayout.addLayout(self.belowVerLayout)  # 把下侧垂直布局加入到总体垂直布局中
        # 一个滚动区
        self.verWholeLayout.addWidget(self.commentArea)
