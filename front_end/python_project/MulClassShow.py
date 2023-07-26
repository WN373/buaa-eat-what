# 该类展示 食堂-柜台-菜品 多级结构
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QGraphicsBlurEffect, QVBoxLayout, QFrame
from PyQt5 import QtWidgets, QtCore, QtGui

from AddBuyCard import AddBuyCard
from CommentArea import CommentArea, ReplyWindow
from RecommendCard import RecommendCard
from TopShowCard import TopShowCard
from qfluentwidgets import CardWidget, StrongBodyLabel, IconWidget, TransparentToolButton, FluentIcon, BodyLabel, \
    InfoBar, InfoBarPosition, ScrollArea, TitleLabel, CaptionLabel

# ScrollArea -> 是继承自 QWidget 的

class MulClassShow(QWidget):
    class ShowItem(CardWidget):
        def __init__(self, labelName):
            super().__init__()
            # labelName
            self.labelName = labelName
            # 学二   查看 收藏  删除
            self.cardName = BodyLabel()
            self.cardName.setText(self.labelName)

    def __init__(self, restList: list):  # restList 待展示的食堂列表
        super().__init__()
        # 一层一层的
        # self.wid = QWidget(self)
        # self.test = QFrame()
        # self.test.
        # self.hor = QtWidgets.QHBoxLayout()
        # self.hor.addWidget(self.test)
        # self.wid.setLayout(self.hor)





