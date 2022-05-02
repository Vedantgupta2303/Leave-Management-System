# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Admin_pagedYIuNO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Admin_Page(object):
    def setupUi(self, Admin_Page):
        if not Admin_Page.objectName():
            Admin_Page.setObjectName(u"Admin_Page")
        Admin_Page.resize(900, 844)
        Admin_Page.setStyleSheet(u"background-color: rgb(233, 239, 192);")
        self.centralwidget = QWidget(Admin_Page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 0, 911, 81))
        self.line.setStyleSheet(u"background-color: rgb(78, 148, 79);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(240, 0, 461, 81))
        self.label_7.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:14pt \"Goudy Old Style\";\n"
"font: 75 26pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(60, 140, 791, 221))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 480, 111, 31))
        self.label_2.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 520, 111, 31))
        self.label_4.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.from_date = QDateEdit(self.centralwidget)
        self.from_date.setObjectName(u"from_date")
        self.from_date.setGeometry(QRect(410, 520, 301, 31))
        self.from_date.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 560, 111, 31))
        self.label_6.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 610, 171, 31))
        self.label_3.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Description = QTextBrowser(self.centralwidget)
        self.Description.setObjectName(u"Description")
        self.Description.setGeometry(QRect(410, 600, 301, 111))
        self.to_date = QDateEdit(self.centralwidget)
        self.to_date.setObjectName(u"to_date")
        self.to_date.setGeometry(QRect(410, 560, 301, 31))
        self.to_date.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.Leave_type_edt = QLineEdit(self.centralwidget)
        self.Leave_type_edt.setObjectName(u"Leave_type_edt")
        self.Leave_type_edt.setGeometry(QRect(410, 480, 301, 31))
        self.Leave_type_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 440, 111, 31))
        self.label_5.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Leave_type_edt_2 = QLineEdit(self.centralwidget)
        self.Leave_type_edt_2.setObjectName(u"Leave_type_edt_2")
        self.Leave_type_edt_2.setGeometry(QRect(410, 440, 301, 31))
        self.Leave_type_edt_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(240, 400, 111, 31))
        self.label_8.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Leave_type_edt_3 = QLineEdit(self.centralwidget)
        self.Leave_type_edt_3.setObjectName(u"Leave_type_edt_3")
        self.Leave_type_edt_3.setGeometry(QRect(410, 400, 301, 31))
        self.Leave_type_edt_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.Previous_btn = QPushButton(self.centralwidget)
        self.Previous_btn.setObjectName(u"Previous_btn")
        self.Previous_btn.setGeometry(QRect(300, 730, 281, 41))
        self.Previous_btn.setStyleSheet(u"QPushButton {\n"
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
        self.Previous_btn_2 = QPushButton(self.centralwidget)
        self.Previous_btn_2.setObjectName(u"Previous_btn_2")
        self.Previous_btn_2.setGeometry(QRect(300, 780, 281, 41))
        self.Previous_btn_2.setStyleSheet(u"QPushButton {\n"
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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 90, 171, 31))
        self.label.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        Admin_Page.setCentralWidget(self.centralwidget)

        self.retranslateUi(Admin_Page)

        QMetaObject.connectSlotsByName(Admin_Page)
    # setupUi

    def retranslateUi(self, Admin_Page):
        Admin_Page.setWindowTitle(QCoreApplication.translate("Admin_Page", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("Admin_Page", u"Leave Management System", None))
        self.label_2.setText(QCoreApplication.translate("Admin_Page", u"Leave type    :", None))
        self.label_4.setText(QCoreApplication.translate("Admin_Page", u"Date from    :", None))
        self.label_6.setText(QCoreApplication.translate("Admin_Page", u"Date to        :", None))
        self.label_3.setText(QCoreApplication.translate("Admin_Page", u"Leave Description    :", None))
        self.label_5.setText(QCoreApplication.translate("Admin_Page", u"Department   :", None))
        self.label_8.setText(QCoreApplication.translate("Admin_Page", u"Name         :", None))
        self.Previous_btn.setText(QCoreApplication.translate("Admin_Page", u"Approve Leave", None))
        self.Previous_btn_2.setText(QCoreApplication.translate("Admin_Page", u"Deny Leave Request", None))
        self.label.setText(QCoreApplication.translate("Admin_Page", u"Faculty Leave Requests", None))
    # retranslateUi

