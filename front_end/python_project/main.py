import sys

from PyQt5.QtCore import Qt, QTranslator, QLocale
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, qApp, QFrame
from qframelesswindow import FramelessWindow, StandardTitleBar, AcrylicWindow

from MulClassShow import MulClassShow
from login_interface import *
from qfluentwidgets import setThemeColor, FluentTranslator, setTheme, Theme, SplitTitleBar, CardWidget, FluentIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from qfluentwidgets import PushButton

if __name__ == '__main__':
    a = 0
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    translator = FluentTranslator(QLocale())
    app.installTranslator(translator)

    # w = LoginWindow()
    w = MainWindow()
    # w = MulClassShow([])
    # w = AddBuyCard()
    # w = showTop15Window()
    # w = DishDetailWindow()
    # w = ReplyWindow()
    # w = testWindow()
    # w = RecommendCard(' ')
    # w = DishesListView('123', QIcon(':/images/logo.png'))
    # w = DishesListView.DishCard()
    w.show()

    app.exec_()
