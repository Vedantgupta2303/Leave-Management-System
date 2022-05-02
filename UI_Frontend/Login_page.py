# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_pagezxsKZc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login_Page(object):
    def setupUi(self, Login_Page):
        if not Login_Page.objectName():
            Login_Page.setObjectName(u"Login_Page")
        Login_Page.resize(800, 500)
        Login_Page.setStyleSheet(u"background-color: rgb(233, 239, 192);")
        self.centralwidget = QWidget(Login_Page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-820, 0, 1621, 91))
        self.line.setStyleSheet(u"background-color: rgb(78, 148, 79);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.Faculty_login_btn = QPushButton(self.centralwidget)
        self.Faculty_login_btn.setObjectName(u"Faculty_login_btn")
        self.Faculty_login_btn.setGeometry(QRect(40, 120, 181, 41))
        self.Faculty_login_btn.setStyleSheet(u"QPushButton {\n"
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
        self.Admin_login_btn = QPushButton(self.centralwidget)
        self.Admin_login_btn.setObjectName(u"Admin_login_btn")
        self.Admin_login_btn.setGeometry(QRect(590, 120, 181, 41))
        self.Admin_login_btn.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 200, 801, 291))
        self.Faculty_Login_page = QWidget()
        self.Faculty_Login_page.setObjectName(u"Faculty_Login_page")
        self.label = QLabel(self.Faculty_Login_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 10, 151, 41))
        self.label.setStyleSheet(u"font: italic 18pt \"Goudy Old Style\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.Faculty_Login_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 80, 151, 41))
        self.label_2.setStyleSheet(u"font: italic 18pt \"Goudy Old Style\";")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.Faculty_Login_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 130, 151, 41))
        self.label_3.setStyleSheet(u"font: italic 18pt \"Goudy Old Style\";")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.Fac_user_edt = QLineEdit(self.Faculty_Login_page)
        self.Fac_user_edt.setObjectName(u"Fac_user_edt")
        self.Fac_user_edt.setGeometry(QRect(400, 90, 171, 31))
        self.Fac_user_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.Fac_password_edt = QLineEdit(self.Faculty_Login_page)
        self.Fac_password_edt.setObjectName(u"Fac_password_edt")
        self.Fac_password_edt.setGeometry(QRect(400, 140, 171, 31))
        self.Fac_password_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.log_btn_fac = QPushButton(self.Faculty_Login_page)
        self.log_btn_fac.setObjectName(u"log_btn_fac")
        self.log_btn_fac.setGeometry(QRect(320, 210, 181, 41))
        self.log_btn_fac.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget.addWidget(self.Faculty_Login_page)
        self.Admin_login_page = QWidget()
        self.Admin_login_page.setObjectName(u"Admin_login_page")
        self.label_4 = QLabel(self.Admin_login_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 20, 151, 41))
        self.label_4.setStyleSheet(u"font: italic 18pt \"Goudy Old Style\";")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.admin_password_edt = QLineEdit(self.Admin_login_page)
        self.admin_password_edt.setObjectName(u"admin_password_edt")
        self.admin_password_edt.setGeometry(QRect(460, 140, 171, 31))
        self.admin_password_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_5 = QLabel(self.Admin_login_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 140, 151, 41))
        self.label_5.setStyleSheet(u"font: italic 18pt \"Goudy Old Style\";")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.admin_user_edt = QLineEdit(self.Admin_login_page)
        self.admin_user_edt.setObjectName(u"admin_user_edt")
        self.admin_user_edt.setGeometry(QRect(460, 100, 171, 31))
        self.admin_user_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_6 = QLabel(self.Admin_login_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 90, 151, 41))
        self.label_6.setStyleSheet(u"font: italic 18pt \"Goudy Old Style\";")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.log_btn_admin = QPushButton(self.Admin_login_page)
        self.log_btn_admin.setObjectName(u"log_btn_admin")
        self.log_btn_admin.setGeometry(QRect(330, 220, 181, 41))
        self.log_btn_admin.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget.addWidget(self.Admin_login_page)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 10, 801, 61))
        self.label_7.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:18pt \"Goudy Old Style\";\n"
"font: 75 26pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.Reg_btn = QPushButton(self.centralwidget)
        self.Reg_btn.setObjectName(u"Reg_btn")
        self.Reg_btn.setGeometry(QRect(310, 120, 181, 41))
        self.Reg_btn.setStyleSheet(u"QPushButton {\n"
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
        Login_Page.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login_Page)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Login_Page)
    # setupUi

    def retranslateUi(self, Login_Page):
        Login_Page.setWindowTitle(QCoreApplication.translate("Login_Page", u"MainWindow", None))
        self.Faculty_login_btn.setText(QCoreApplication.translate("Login_Page", u"Faculty Login", None))
        self.Admin_login_btn.setText(QCoreApplication.translate("Login_Page", u"Admin Login", None))
        self.label.setText(QCoreApplication.translate("Login_Page", u"Faculty Login", None))
        self.label_2.setText(QCoreApplication.translate("Login_Page", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("Login_Page", u"Password", None))
        self.log_btn_fac.setText(QCoreApplication.translate("Login_Page", u"Login", None))
        self.label_4.setText(QCoreApplication.translate("Login_Page", u"Admin Login", None))
        self.label_5.setText(QCoreApplication.translate("Login_Page", u"Password", None))
        self.label_6.setText(QCoreApplication.translate("Login_Page", u"Username", None))
        self.log_btn_admin.setText(QCoreApplication.translate("Login_Page", u"Login", None))
        self.label_7.setText(QCoreApplication.translate("Login_Page", u"LEAVE MANAGEMENT SYSTEM", None))
        self.Reg_btn.setText(QCoreApplication.translate("Login_Page", u"Register", None))
    # retranslateUi

