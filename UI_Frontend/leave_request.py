# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Leave_request_form_PageOpvRDM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Leave_request_page(object):
    def setupUi(self, Leave_request_page):
        if not Leave_request_page.objectName():
            Leave_request_page.setObjectName(u"Leave_request_page")
        Leave_request_page.resize(861, 555)
        Leave_request_page.setStyleSheet(u"background-color: rgb(233, 239, 192);")
        self.centralwidget = QWidget(Leave_request_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-350, -20, 651, 581))
        self.line.setStyleSheet(u"background-color: rgb(78, 148, 79);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 170, 301, 61))
        self.label_7.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:14pt \"Goudy Old Style\";\n"
"font: 75 26pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(-10, 230, 291, 61))
        self.label_8.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:14pt \"Goudy Old Style\";\n"
"font: 75 26pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(510, 30, 131, 31))
        self.label.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 120, 111, 31))
        self.label_2.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 200, 111, 31))
        self.label_6.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 160, 111, 31))
        self.label_4.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 250, 171, 31))
        self.label_3.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Leave_type_edt = QLineEdit(self.centralwidget)
        self.Leave_type_edt.setObjectName(u"Leave_type_edt")
        self.Leave_type_edt.setGeometry(QRect(540, 120, 301, 31))
        self.Leave_type_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.from_date = QDateEdit(self.centralwidget)
        self.from_date.setObjectName(u"from_date")
        self.from_date.setGeometry(QRect(540, 160, 301, 31))
        self.from_date.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.to_date = QDateEdit(self.centralwidget)
        self.to_date.setObjectName(u"to_date")
        self.to_date.setGeometry(QRect(540, 200, 301, 31))
        self.to_date.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.Description = QTextBrowser(self.centralwidget)
        self.Description.setObjectName(u"Description")
        self.Description.setGeometry(QRect(540, 250, 301, 171))
        self.Createrequest_btn = QPushButton(self.centralwidget)
        self.Createrequest_btn.setObjectName(u"Createrequest_btn")
        self.Createrequest_btn.setGeometry(QRect(490, 470, 181, 41))
        self.Createrequest_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 14pt \"Goudy Old Style\";\n"
"background-color: rgb(78, 148, 79);\n"
"color:rgb(255,255,255);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(233, 239, 192);\n"
"color: rgb(0,0,0);\n"
"}\n"
"")
        Leave_request_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(Leave_request_page)

        QMetaObject.connectSlotsByName(Leave_request_page)
    # setupUi

    def retranslateUi(self, Leave_request_page):
        Leave_request_page.setWindowTitle(QCoreApplication.translate("Leave_request_page", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("Leave_request_page", u"Leave Management", None))
        self.label_8.setText(QCoreApplication.translate("Leave_request_page", u"System", None))
        self.label.setText(QCoreApplication.translate("Leave_request_page", u"Leave Request ", None))
        self.label_2.setText(QCoreApplication.translate("Leave_request_page", u"Leave type    :", None))
        self.label_6.setText(QCoreApplication.translate("Leave_request_page", u"Date to        :", None))
        self.label_4.setText(QCoreApplication.translate("Leave_request_page", u"Date from    :", None))
        self.label_3.setText(QCoreApplication.translate("Leave_request_page", u"Leave Description    :", None))
        self.Createrequest_btn.setText(QCoreApplication.translate("Leave_request_page", u"Create Request", None))
    # retranslateUi

