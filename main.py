import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)

from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from UI_Frontend.Login_page import Ui_Login_Page
from Register import Register_window

class Main_window:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_Login_Page()
        self.ui.setupUi(self.main_win)
        
        # =========    Widgets Switching    ==========
        self.ui.stackedWidget.setCurrentWidget(self.ui.Faculty_Login_page)
        self.ui.Admin_login_btn.clicked.connect(self.Admin_page_login)
        self.ui.Faculty_login_btn.clicked.connect(self.Faculty_page_login)
        
        # ========     Button Functions      ==========
        self.ui.Reg_btn.clicked.connect(self.reg_page_display)
        
        
        
    
    
    def Admin_page_login(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Admin_login_page)
    def Faculty_page_login(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Faculty_Login_page)
    def reg_page_display(self):
        self.Register = Register_window()
        self.Register.show()
     
    def show(self):
        self.main_win.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = Main_window()
    window.show()
    sys.exit(app.exec_())