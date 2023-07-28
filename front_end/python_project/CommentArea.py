from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon, QFont
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QPlainTextEdit
import datetime
from qfluentwidgets import ScrollArea, TitleLabel, CaptionLabel, FluentIcon, PushButton, StrongBodyLabel, ToolButton, \
    TransparentToolButton, CardWidget, setThemeColor, CheckBox, PrimaryPushButton, InfoBar, InfoBarPosition


def get_current_time():
    # 获取当前时间
    now = datetime.datetime.now()

    # 格式化为指定格式
    formatted_time = now.strftime("%Y-%m-%d %H:%M")

    return formatted_time


class ReplyWindow(CardWidget):
    def __init__(self, parent, replyObject):  # 这个parent就是那个Scroll区域 CommentArea 对象
        super().__init__()
        self.parentWidget = parent
        self.replyObject = replyObject  # 表示这个回复窗口要回复的对象
        windowTitle = ''
        if replyObject == '':
            windowTitle += '评论菜品'
        else:
            windowTitle += ('回复  @' + replyObject)
        self.setWindowTitle(windowTitle)  # 最好显示出来回复谁
        self.setWindowIcon(QIcon(':/images/logo.png'))
        # setThemeColor('#FFFFFF')  # 背景颜色
        # self.setStyleSheet("""
        #     QWidget {
        #         color: black
        #     }""")
        # self.setStyleSheet("background-color: lightblue;")
        self.setStyleSheet("background-color: #ffffff;")



        self.verRealWhole = QtWidgets.QVBoxLayout(self)
        self.verRealWhole.addSpacing(60)

        self.horWholeLayout = QtWidgets.QHBoxLayout()
        self.horWholeLayout.addSpacing(50)
        self.verWholeLayout = QtWidgets.QVBoxLayout()
        self.horWholeLayout.addLayout(self.verWholeLayout)
        self.verRealWhole.addLayout(self.horWholeLayout)
        self.horWholeLayout.addSpacing(50)
        self.verRealWhole.addSpacing(40)
        # self.verWholeLayout.addSpacing(60)
        # 第一层: 留言内容
        self.horLayout1 = QtWidgets.QHBoxLayout()
        self.verWholeLayout.addLayout(self.horLayout1)

        self.verLayout1 = QtWidgets.QVBoxLayout()
        self.label1 = StrongBodyLabel()
        self.label1.setText('留言内容：  ')
        # self.label1.setFont(font)
        self.label1.setStyleSheet("""QLabel{font: 15px 'Microsoft YaHei';}""")
        self.verLayout1.addWidget(self.label1)
        self.verLayout1.addStretch()  # 把标签挤到上面去

        self.horLayout1.addLayout(self.verLayout1)

        self.editArea = QPlainTextEdit()
        self.editArea.setPlaceholderText('在这里输入评论内容哦 ~')
        # self.editArea.setStyleSheet("QPlainTextEdit::placeholder { font-size: 120px; }")
        # self.editArea.setInputMethodHints('在这里输入评论内容哦 ~')
        self.editArea.setFont(QFont("Microsoft YaHei", 10))
        self.editArea.setStyleSheet("border: 1px solid gray; border-radius: 10px;")
        self.horLayout1.addWidget(self.editArea)

        # 空白符, 加一加间距
        self.verWholeLayout.addSpacing(15)
        # 第二层: 是否匿名
        self.horLayout2 = QtWidgets.QHBoxLayout()
        self.verWholeLayout.addLayout(self.horLayout2)
        self.label2 = StrongBodyLabel()
        self.label2.setText('开启匿名：  ')
        self.label2.setStyleSheet("""QLabel{font: 15px 'Microsoft YaHei';}""")
        self.horLayout2.addWidget(self.label2)

        self.checkBox = CheckBox(self)
        self.checkBox.setChecked(False)
        self.horLayout2.addWidget(self.checkBox)
        self.horLayout2.addStretch()

        self.verWholeLayout.addSpacing(20)
        # 第三层: 确认发布按钮
        self.overButton = PrimaryPushButton()
        self.overButton.setText('确认发布')
        self.verWholeLayout.addWidget(self.overButton)
        self.resize(650, 400)
        self.setMinimumSize(QtCore.QSize(650, 400))
        self.overButton.clicked.connect(self.clickOverButton)

    def clickOverButton(self):
        if self.editArea.toPlainText() == '':
            InfoBar.error(
                title='您还没有输入内容哦 ~',
                content='',
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self
            )
            return 0
        # 显示评论成功, 加评论(界面+数据库)
        InfoBar.success(
            title='评论成功!',
            content='',
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self.parentWidget
        )
        user = ''
        if self.checkBox.isChecked():  # 匿名评论
            user += '匿名用户'
        else:
            user += '坤坤'  # 获取当前登录着的用户名
        time = get_current_time()
        # TODO 注意存进数据库!!
        self.parentWidget.addCommentItem(
            username=user, content=self.editArea.toPlainText(), time=time, replyUser=self.replyObject)
        self.close()


class ToolBar(QWidget):
    def __init__(self, title, subtitle, parent=None):
        super().__init__(parent=parent)
        # rgb(24, 25, 28)
        self.titleLabel = TitleLabel(title, self)
        self.subtitleLabel = CaptionLabel(subtitle, self)
        self.titleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 25px 'Microsoft YaHei';
                padding: 0 0px;
                color: rgb(24, 25, 28)
            }
        """)

        self.subtitleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 12px 'Microsoft YaHei';
                padding: 0 0px;
                color: rgb(192, 194, 198)
            }
        """)
        self.vBoxLayout = QVBoxLayout(self)
        # self.buttonLayout = QHBoxLayout()

        self.__initWidget()

    def __initWidget(self):
        self.setFixedHeight(138)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(36, 22, 36, 12)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addSpacing(4)
        self.vBoxLayout.addWidget(self.subtitleLabel)
        self.vBoxLayout.setAlignment(Qt.AlignTop)


class CommentItem(QWidget):
    def __init__(self, username, time, content, replyUser, scroll):
        super().__init__()
        self.parentWidget = scroll
        self.username = username
        self.time = time
        self.content = content
        self.replyUser = replyUser
        # 整体垂直布局
        self.verWholeLayout = QtWidgets.QVBoxLayout(self)

        self.horUsernameLayout = QtWidgets.QHBoxLayout()
        self.horContentLayout = QtWidgets.QHBoxLayout()
        self.horTimeReplyLayout = QtWidgets.QHBoxLayout()

        self.verWholeLayout.addLayout(self.horUsernameLayout)
        self.verWholeLayout.addLayout(self.horContentLayout)
        self.verWholeLayout.addLayout(self.horTimeReplyLayout)

        # 第一层: 一个名字标签
        self.nameLabel = StrongBodyLabel()
        self.nameLabel.setText(self.username)
        self.nameLabel.setTextColor(QColor(251, 114, 153))
        self.nameLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 13px 'Microsoft YaHei';
                padding: 0 0px;
            }
        """)
        self.horUsernameLayout.addWidget(self.nameLabel)
        # 第二层: 一个评论内容标签 回复 @I_love_Ei :
        if self.replyUser != '':  # 有回复对象
            self.replyLabel = QLabel()
            self.replyLabel.setText('回复 ')
            self.replyLabel.setStyleSheet("""
                QLabel{
                    background: transparent;
                    font: 14px 'Microsoft YaHei';
                    padding: 0 0px;
                    color: black
                }
            """)

            self.replyUserLabel = QLabel()
            self.replyUserLabel.setText('@' + self.replyUser + ' : ')
            QColor('')
            self.replyUserLabel.setStyleSheet("""
                QLabel{
                    background: transparent;
                    font: 14px 'Microsoft YaHei';
                    padding: 0 0px;
                    color: rgb(0, 143, 212)
                }
            """)

            self.horContentLayout.addWidget(self.replyLabel)
            self.horContentLayout.addWidget(self.replyUserLabel)
        self.contentLabel = QLabel()
        self.contentLabel.setText(self.content)
        self.horContentLayout.addWidget(self.contentLabel)
        self.contentLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 14px 'Microsoft YaHei';
                padding: 0 0px;
                color: black
            }
        """)
        self.horContentLayout.addStretch()
        # 第三层: 一个发表时间标签 + 一个回复按钮 PushButton(self.tr('Source'), self, FluentIcon.GITHUB)
        self.timeLabel = QLabel()
        self.timeLabel.setText(self.time)
        self.timeLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 10px 'Microsoft YaHei';
                padding: 0 0px;
                color: rgb(176, 153, 160)
            }
        """)
        self.horTimeReplyLayout.addWidget(self.timeLabel)
        self.horTimeReplyLayout.addStretch(1)
        self.replyButton = TransparentToolButton(self)
        self.replyButton.setIcon(FluentIcon.CHAT)
        self.horTimeReplyLayout.addWidget(self.replyButton)

        self.replyButton.clicked.connect(self.clickReplyButton)

    def clickReplyButton(self):
        # 弹出一个 回复某人的评论 的窗口
        self.replyWindow = ReplyWindow(self.parentWidget, self.username)  # 点击评论项的回复按钮的话, 传进去用户名, 如果点击的是标签的回复的话, 那就传进去空字符串
        self.replyWindow.show()


        # print(self.content)
        # a = 1

class CommentArea(ScrollArea):
    def __init__(self, title: str, subtitle: str, parent=None):
        super().__init__(parent=parent)
        self.commentItems = []
        self.view = QWidget(self)
        self.toolBar = ToolBar(title, subtitle, self)
        self.vBoxLayout = QVBoxLayout(self.view)  # 现在, 只需要往vBoxLayout这个垂直布局中加东西, 就是往滚动区中加东西了

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 90, 0, 0)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setAlignment(Qt.AlignTop)
        self.vBoxLayout.setContentsMargins(36, 20, 36, 36)

        self.view.setObjectName('view')
        # StyleSheet.GALLERY_INTERFACE.apply(self)
        self.addCommentItem('鸡哥', '2023-07-22 15:22', '如果你也可以!!', '')
        self.addCommentItem('wcw', '2023-07-22 01:02', '像我一样!!', '')
        self.addCommentItem('nyj', '2023-07-22 00:12', '那么!!', '')
        self.addCommentItem('nyf', '2023-07-22 02:33', '我觉得这件事情!!', '')
        self.addCommentItem('nme', '2023-07-22 09:34', '????????', '')

    def addCommentItem(self, username, time, content, replyUser):  # 某个用户在某个时间评论了某个内容
        item = CommentItem(username, time, content, replyUser, self)
        self.commentItems.append(item)
        # 加评论项
        self.vBoxLayout.addWidget(item)