import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)

from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from UI_Frontend.dashboard import Ui_Dashboard_fac_page
class Dashboard_window:
    def __init__(self,details):
        self.main_win = QMainWindow()
        self.ui = Ui_Dashboard_fac_page()
        self.ui.setupUi(self.main_win)
        self.details = details
        
    def show(self):
        self.main_win.show()