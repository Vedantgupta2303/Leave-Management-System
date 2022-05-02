# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'History_pageuPQHUc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_History_Page(object):
    def setupUi(self, History_Page):
        if not History_Page.objectName():
            History_Page.setObjectName(u"History_Page")
        History_Page.resize(941, 540)
        History_Page.setStyleSheet(u"background-color: rgb(233, 239, 192);")
        self.centralwidget = QWidget(History_Page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-410, -20, 821, 581))
        self.line.setStyleSheet(u"background-color: rgb(78, 148, 79);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 80, 331, 61))
        self.label_7.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:14pt \"Goudy Old Style\";\n"
"font: 75 26pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 130, 331, 61))
        self.label_8.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:14pt \"Goudy Old Style\";\n"
"font: 75 26pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 220, 111, 31))
        self.label_9.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:bold 14pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(60, 340, 111, 31))
        self.label_15.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:bold 14pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Name_lbl = QLabel(self.centralwidget)
        self.Name_lbl.setObjectName(u"Name_lbl")
        self.Name_lbl.setGeometry(QRect(200, 220, 211, 31))
        self.Name_lbl.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:bold 14pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.Name_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 260, 111, 31))
        self.label_11.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:bold 14pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mail_lbl = QLabel(self.centralwidget)
        self.mail_lbl.setObjectName(u"mail_lbl")
        self.mail_lbl.setGeometry(QRect(200, 260, 211, 31))
        self.mail_lbl.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:bold 14pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.mail_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.dep_lbl = QLabel(self.centralwidget)
        self.dep_lbl.setObjectName(u"dep_lbl")
        self.dep_lbl.setGeometry(QRect(200, 300, 71, 31))
        self.dep_lbl.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:bold 14pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.dep_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.remaining_lbl = QLabel(self.centralwidget)
        self.remaining_lbl.setObjectName(u"remaining_lbl")
        self.remaining_lbl.setGeometry(QRect(200, 340, 71, 31))
        self.remaining_lbl.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:bold 14pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.remaining_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(60, 300, 141, 31))
        self.label_13.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:bold 14pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(410, 70, 531, 201))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(610, 20, 131, 31))
        self.label.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.to_date = QDateEdit(self.centralwidget)
        self.to_date.setObjectName(u"to_date")
        self.to_date.setGeometry(QRect(610, 360, 301, 31))
        self.to_date.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(440, 410, 171, 31))
        self.label_3.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(440, 320, 111, 31))
        self.label_4.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(440, 280, 111, 31))
        self.label_2.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(440, 360, 111, 31))
        self.label_6.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.from_date = QDateEdit(self.centralwidget)
        self.from_date.setObjectName(u"from_date")
        self.from_date.setGeometry(QRect(610, 320, 301, 31))
        self.from_date.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.Description = QTextBrowser(self.centralwidget)
        self.Description.setObjectName(u"Description")
        self.Description.setGeometry(QRect(610, 400, 301, 111))
        self.Leave_type_edt = QLineEdit(self.centralwidget)
        self.Leave_type_edt.setObjectName(u"Leave_type_edt")
        self.Leave_type_edt.setGeometry(QRect(610, 280, 301, 31))
        self.Leave_type_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        History_Page.setCentralWidget(self.centralwidget)

        self.retranslateUi(History_Page)

        QMetaObject.connectSlotsByName(History_Page)
    # setupUi

    def retranslateUi(self, History_Page):
        History_Page.setWindowTitle(QCoreApplication.translate("History_Page", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("History_Page", u"Leave Management", None))
        self.label_8.setText(QCoreApplication.translate("History_Page", u"System", None))
        self.label_9.setText(QCoreApplication.translate("History_Page", u"Name            :", None))
        self.label_15.setText(QCoreApplication.translate("History_Page", u"Days Left       :", None))
        self.Name_lbl.setText(QCoreApplication.translate("History_Page", u"Pavan Kumar", None))
        self.label_11.setText(QCoreApplication.translate("History_Page", u"Email            :", None))
        self.mail_lbl.setText(QCoreApplication.translate("History_Page", u"pavan@gmail.com", None))
        self.dep_lbl.setText(QCoreApplication.translate("History_Page", u"CS", None))
        self.remaining_lbl.setText(QCoreApplication.translate("History_Page", u"23", None))
        self.label_13.setText(QCoreApplication.translate("History_Page", u"Department  :", None))
        self.label.setText(QCoreApplication.translate("History_Page", u"Previous Requests", None))
        self.label_3.setText(QCoreApplication.translate("History_Page", u"Leave Description    :", None))
        self.label_4.setText(QCoreApplication.translate("History_Page", u"Date from    :", None))
        self.label_2.setText(QCoreApplication.translate("History_Page", u"Leave type    :", None))
        self.label_6.setText(QCoreApplication.translate("History_Page", u"Date to        :", None))
    # retranslateUi

