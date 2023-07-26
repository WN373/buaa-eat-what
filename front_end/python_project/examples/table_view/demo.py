# coding: utf-8
import sys
from PyQt5.QtGui import QColor

from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QStyleOptionViewItem, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout

from qfluentwidgets import TableWidget, isDarkTheme, setTheme, Theme, TableView, TableItemDelegate


class CustomTableItemDelegate(TableItemDelegate):
    """ Custom table item delegate """

    def initStyleOption(self, option: QStyleOptionViewItem, index: QModelIndex):
        super().initStyleOption(option, index)
        if index.column() != 1:
            return

        if isDarkTheme():
            option.palette.setColor(QPalette.Text, Qt.white)
            option.palette.setColor(QPalette.HighlightedText, Qt.white)
        else:
            option.palette.setColor(QPalette.Text, Qt.red)
            option.palette.setColor(QPalette.HighlightedText, Qt.red)


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # setTheme(Theme.DARK)

        self.hBoxLayout = QHBoxLayout(self)
        self.tableView = TableWidget(self)

        # NOTE: use custom item delegate
        # self.tableView.setItemDelegate(CustomTableItemDelegate(self.tableView))

        self.tableView.setWordWrap(True)
        self.tableView.setRowCount(1)
        # self.tableView.editorDestroyed
        self.tableView.setColumnCount(6)
        # songInfos = [
        #     ['かばん', 'aiko', 'かばん', '2004', '5:04'],
        #     ['爱你', '王心凌', '爱你', '2004', '3:39'],
        #     ['星のない世界', 'aiko', '星のない世界/横顔', '2007', '5:30'],
        #     ['横顔', 'aiko', '星のない世界/横顔', '2007', '5:06'],
        #     ['秘密', 'aiko', '秘密', '2008', '6:27'],
        #     ['シアワセ', 'aiko', '秘密', '2008', '5:25'],
        #     ['二人', 'aiko', '二人', '2008', '5:00'],
        #     ['スパークル', 'RADWIMPS', '君の名は。', '2016', '8:54'],
        #     ['なんでもないや', 'RADWIMPS', '君の名は。', '2016', '3:16'],
        #     ['前前前世', 'RADWIMPS', '人間開花', '2016', '4:35'],
        #     ['恋をしたのは', 'aiko', '恋をしたのは', '2016', '6:02'],
        #     ['夏バテ', 'aiko', '恋をしたのは', '2016', '4:41'],
        #     ['もっと', 'aiko', 'もっと', '2016', '4:50'],
        #     ['問題集', 'aiko', 'もっと', '2016', '4:18'],
        #     ['半袖', 'aiko', 'もっと', '2016', '5:50'],
        #     ['ひねくれ', '鎖那', 'Hush a by little girl', '2017', '3:54'],
        #     ['シュテルン', '鎖那', 'Hush a by little girl', '2017', '3:16'],
        #     ['愛は勝手', 'aiko', '湿った夏の始まり', '2018', '5:31'],
        #     ['ドライブモード', 'aiko', '湿った夏の始まり', '2018', '3:37'],
        #     ['うん。', 'aiko', '湿った夏の始まり', '2018', '5:48'],
        #     ['キラキラ', 'aikoの詩。', '2019', '5:08', 'aiko'],
        #     ['恋のスーパーボール', 'aiko', 'aikoの詩。', '2019', '4:31'],
        #     ['磁石', 'aiko', 'どうしたって伝えられないから', '2021', '4:24'],
        #     ['食べた愛', 'aiko', '食べた愛/あたしたち', '2021', '5:17'],
        #     ['列車', 'aiko', '食べた愛/あたしたち', '2021', '4:18'],
        #     ['花の塔', 'さユり', '花の塔', '2022', '4:35'],
        #     ['夏恋のライフ', 'aiko', '夏恋のライフ', '2022', '5:03'],
        #     ['あかときリロード', 'aiko', 'あかときリロード', '2023', '4:04'],
        #     ['荒れた唇は恋を失くす', 'aiko', '今の二人をお互いが見てる', '2023', '4:07'],
        #     ['ワンツースリー', 'aiko', '今の二人をお互いが見てる', '2023', '4:47'],
        # ]
        songInfos = [
            ['1', '豆浆', '学二一层', '0.5元/碗', '13', '12']
        ]
        # songInfos += songInfos
        for i, songInfo in enumerate(songInfos):
            for j in range(6):
                tempItem = QTableWidgetItem(songInfo[j])
                if j == 0:            
                    tempItem.setForeground(QColor(241, 111, 133))
                elif j == 1:
                    tempItem.setForeground(QColor(84, 150, 205))
                self.tableView.setItem(i, j, tempItem)

        self.tableView.verticalHeader().hide()
        self.tableView.setHorizontalHeaderLabels(['序号', '菜品名', '售卖地', '价格', '购买量', '收藏量'])
        self.tableView.resizeColumnsToContents()
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setSortingEnabled(True)
        # self.tableView.resize(635, 700)


        self.setStyleSheet("Demo{background: rgb(249, 249, 249)} ")
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.tableView)
        self.resize(635, 700)


if __name__ == "__main__":
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()
