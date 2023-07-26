import sys

from PyQt5.QtCore import Qt, QTranslator, QLocale
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication
from qframelesswindow import FramelessWindow, StandardTitleBar, AcrylicWindow
from qfluentwidgets import setThemeColor, FluentTranslator, setTheme, Theme, SplitTitleBar
from Ui_LoginWindow import Ui_Form


class LoginWindow(AcrylicWindow, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # setTheme(Theme.DARK)
        setThemeColor('#28afe9')  # 背景颜色

        self.setTitleBar(SplitTitleBar(self))  # titleBar 标题栏
        self.titleBar.raise_()

        self.label.setScaledContents(False)  # 图片缩放内容属性
        # self.setWindowTitle('PyQt-Fluent-Widget')  
        self.setWindowTitle('BUAA delicious Food') # 窗口标题
        self.setWindowIcon(QIcon(":/images/logo.png"))  # 窗口标题图标
        self.resize(1000, 650)  # 设置窗口的大小

        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=False)  # 窗口特效
        self.setStyleSheet("LoginWindow{background: rgba(242, 242, 242, 0.8)}")
        # QLabel{
        #         background: transparent;  
        #         font: 13px 'Segoe UI';  设置文字的大小和字体(consolas...)
        #         padding: 0 4px;  边距
        #         color: white  颜色
        #     }
        
        self.titleBar.titleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 13px 'Segoe UI';
                padding: 0 4px;
                color: white
            }
        """)
        # 这三行代码将窗口移动到屏幕中央
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap(":/images/background.jpg").scaled(
            self.label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)  # 1号label就是存左边的图片的


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)

    # Internationalization
    translator = FluentTranslator(QLocale())
    app.installTranslator(translator)

    w = LoginWindow()
    w.show()
    app.exec_()