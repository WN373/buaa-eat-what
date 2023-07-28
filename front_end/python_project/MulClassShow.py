# 该类展示 食堂-柜台-菜品 多级结构
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QGraphicsBlurEffect, QVBoxLayout, QFrame
from PyQt5 import QtWidgets, QtCore, QtGui

from AddBuyCard import AddBuyCard
from CommentArea import CommentArea, ReplyWindow
from RecommendCard import RecommendCard
from TopShowCard import TopShowCard
from MulClassShowCounter import MulClassShowCounter
from qfluentwidgets import PrimaryPushButton
from qfluentwidgets import LineEdit
from qfluentwidgets import ToolButton
from qfluentwidgets import MessageBox
from qfluentwidgets import CardWidget, StrongBodyLabel, IconWidget, TransparentToolButton, FluentIcon, BodyLabel, \
    InfoBar, InfoBarPosition, ScrollArea, TitleLabel, CaptionLabel
import global_vars

# ScrollArea -> 是继承自 QWidget 的

class MulClassShow(ScrollArea):
    class ShowItem(CardWidget):
        def __init__(self, labelName, iconAddrList: list, parent):
            super().__init__()
            self.horMain = QtWidgets.QHBoxLayout(self)
            self.parentWidget = parent
            # labelName
            self.labelName = labelName
            # 学二   查看 收藏  删除
            self.cardNameLabel = BodyLabel()
            self.cardNameLabel.setText(self.labelName)
            # 加若干个按钮
            self.button0 = TransparentToolButton()
            self.button1 = TransparentToolButton()
            self.button2 = TransparentToolButton()

            self.button0.setIcon(QIcon(iconAddrList[0]))  # 查看
            self.button1.setIcon(QIcon(iconAddrList[1]))  # 收藏
            self.button2.setIcon(QIcon(iconAddrList[2]))  # 删除

            self.horMain.addSpacing(20)
            self.horMain.addWidget(self.cardNameLabel)
            self.horMain.addStretch()
            self.horMain.addWidget(self.button0)
            self.horMain.addWidget(self.button1)
            self.horMain.addWidget(self.button2)
            self.horMain.addSpacing(20)

            self.button0.clicked.connect(self.clickButton0)
            self.button1.clicked.connect(self.clickButton1)
            self.button2.clicked.connect(self.clickButton2)

        def clickButton0(self):
            # 查看, 页面跳转
            # self.close()
            self.nextInter = MulClassShowCounter([], self.labelName + '柜台一览', '这里可以看到' + self.labelName + '的相关柜台哦 ~', self.labelName)
            self.nextInter.show()
            print('0')

        def clickButton1(self):
            # 收藏, 要查询当前用户是否收藏了这个菜品
            username = global_vars.getUsername()
            print('1')

        def clickButton2(self):
            # 删除, 出来弹窗问是否确定
            print('try to delete!')
            title = '删除确认'
            content = '一旦您删除此项, 其将不再出现在列表中。 您确定要删除 \"' + self.labelName + '\" 项吗 ?'
            print(self.labelName)
            messageBox = MessageBox(title, content, self.parentWidget)
            if messageBox.exec():  # 确定删除
                # print('delete')
                self.parentWidget.deleteCard(self.labelName)
                # 数据库删除这一项 TODO
                InfoBar.success(
                    title='删除成功!',
                    content='',
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=2000,
                    parent=self.parentWidget
                )

    def __init__(self, restList: list, title, subtitle, parent):  # restList 待展示的食堂列表
        super().__init__()
        self.view = QWidget(self)
        self.setParent(parent)
        self.title = title
        self.subtitle = subtitle
        self.toolBar = ToolBar(self.title, self.subtitle, self)
        self.vBoxLayout = QVBoxLayout(self.view)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, self.toolBar.height(), 0, 0)
        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.vBoxLayout.setSpacing(10)
        self.vBoxLayout.setAlignment(Qt.AlignTop)
        self.vBoxLayout.setContentsMargins(36, 20, 36, 36)

        self.view.setObjectName('view')

        self.setStyleSheet("""
            QScrollArea{
                background-color: rgb(249, 249, 249);
                border: none;            
            }
        """)


        self.lst = []
        self.lst.append(self.addCard('学二', ['resource/images/find.png', 'resource/images/star_yes.png', 'resource/images/delete.png'], self))
        self.lst.append(self.addCard('新北一层', ['resource/images/find.png', 'resource/images/star_yes.png', 'resource/images/delete.png'], self))
        self.lst.append(self.addCard('合一三层', ['resource/images/find.png', 'resource/images/star_yes.png', 'resource/images/delete.png'], self))
        self.lst.append(self.addCard('美食苑', ['resource/images/find.png', 'resource/images/star_yes.png', 'resource/images/delete.png'], self))
        self.lst.append(self.addCard('新北地下', ['resource/images/find.png', 'resource/images/star_yes.png', 'resource/images/delete.png'], self))
        self.lst.append(self.addCard('合一四层', ['resource/images/find.png', 'resource/images/star_yes.png', 'resource/images/delete.png'], self))
        # self.lst = ['学二', '新北一层', '合一三层', '美食苑', '新北地下', '合一四层']

    def addCard(self, labelName, iconAddrList, parent):
        card = self.ShowItem(labelName, iconAddrList, parent)
        self.vBoxLayout.addWidget(card, 0, Qt.AlignTop)
        # self.lst.append(card)
        return card
        # self.vBoxLayout.remo

    def deleteCard(self, deleteItemName):
        # 把某一项去除, 然后把剩下的重新显示一遍
        removeItem = None
        for e in self.lst:
            if e.labelName == deleteItemName:
                removeItem = e
                break

        self.vBoxLayout.removeWidget(removeItem)
        removeItem.deleteLater()
        # self.lst.remove(removeItem)


class ToolBar(QWidget):
    class EditWindow(CardWidget):  # 输入要添加的食堂名
        def __init__(self, parent):  # 此parent其实是parent的parent, 而不是ToolBar
            super().__init__()
            self.parentWidget = parent
            self.setWindowTitle('输入添加对象名称')
            self.setWindowIcon(QIcon(':/images/logo.png'))
            self.verMain = QtWidgets.QVBoxLayout(self)
            self.verMain.addSpacing(30)
            self.editLine = LineEdit()
            self.editLine.setPlaceholderText('在这里输入您要添加的对象的名称')
            self.horEdit = QtWidgets.QHBoxLayout()
            self.horEdit.addSpacing(40)
            self.horEdit.addWidget(self.editLine)
            self.horEdit.addSpacing(40)
            self.verMain.addLayout(self.horEdit)
            self.horButton = QtWidgets.QHBoxLayout()
            self.button = PrimaryPushButton()
            self.button.setText('点击添加')
            self.horButton.addStretch()
            self.horButton.addWidget(self.button)
            self.horButton.addStretch()
            self.verMain.addLayout(self.horButton)
            self.button.clicked.connect(self.clickButton)
            self.resize(400, 200)

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
                card = self.parentWidget.addCard(text, ['resource/images/find.png', 'resource/images/star_yes.png', 'resource/images/delete.png'], self.parentWidget)
                self.parentWidget.lst.append(card)  # TODO 这里只是模拟
                self.close()

    def __init__(self, title, subtitle, parent=None):
        super().__init__(parent=parent)
        self.titleLabel = TitleLabel(title)
        self.parentWidget = parent
        self.subtitleLabel = CaptionLabel(subtitle)
        self.vBoxLayout = QVBoxLayout(self)
        self.setFixedHeight(138)
        # self.setFixedWidth(300)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(36, 22, 36, 12)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addSpacing(4)
        self.vBoxLayout.addWidget(self.subtitleLabel)
        self.vBoxLayout.addSpacing(4)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.horWid = QWidget()
        self.horWid.setLayout(self.buttonLayout)
        self.horWid.setFixedWidth(parent.width())
        self.horWid.setFixedWidth(780)
        self.vBoxLayout.addWidget(self.horWid)
        self.buttonLayout.addStretch()
        self.addButton = ToolButton(FluentIcon.ADD, self)
        self.buttonLayout.addWidget(self.addButton)
        self.addButton.clicked.connect(self.clickAddButton)

    def clickAddButton(self):
        self.addWidget = self.EditWindow(self.parentWidget)
        self.addWidget.show()