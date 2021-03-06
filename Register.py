import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)

from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from fun_dbms import Database
from UI_Frontend.register_page import Ui_Register_page
class Register_window:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_Register_page()
        self.ui.setupUi(self.main_win)
        
        self.ui.Register_btn.clicked.connect(self.Register)
    
    def Register(self):
        self.db = Database()
        msg = self.db.Register(self.ui.fac_name_edt.text(),)
        
      
    def show(self):
        self.main_win.show()