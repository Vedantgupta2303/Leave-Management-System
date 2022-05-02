# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register_pageiKhnlu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Register_page(object):
    def setupUi(self, Register_page):
        if not Register_page.objectName():
            Register_page.setObjectName(u"Register_page")
        Register_page.resize(829, 561)
        Register_page.setStyleSheet(u"background-color: rgb(233, 239, 192);")
        self.centralwidget = QWidget(Register_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 0, 1621, 101))
        self.line.setStyleSheet(u"background-color: rgb(78, 148, 79);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 0, 811, 101))
        self.label_7.setStyleSheet(u"background-color: rgb(78, 148, 79);\n"
"font:18pt \"Goudy Old Style\";\n"
"font: 75 26pt \"Goudy Old Style\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 110, 161, 51))
        self.label.setStyleSheet(u"font: italic 20pt \"Goudy Old Style\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 190, 91, 41))
        self.label_2.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(480, 190, 91, 41))
        self.label_3.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 240, 91, 41))
        self.label_4.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(480, 240, 91, 41))
        self.label_5.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 290, 91, 41))
        self.label_6.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(480, 290, 111, 41))
        self.label_8.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.fac_name_edt = QLineEdit(self.centralwidget)
        self.fac_name_edt.setObjectName(u"fac_name_edt")
        self.fac_name_edt.setGeometry(QRect(280, 200, 141, 31))
        self.fac_name_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.fac_last_name_edt = QLineEdit(self.centralwidget)
        self.fac_last_name_edt.setObjectName(u"fac_last_name_edt")
        self.fac_last_name_edt.setGeometry(QRect(610, 200, 141, 31))
        self.fac_last_name_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(280, 250, 141, 31))
        self.comboBox.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.fac_id_edit = QLineEdit(self.centralwidget)
        self.fac_id_edit.setObjectName(u"fac_id_edit")
        self.fac_id_edit.setGeometry(QRect(610, 250, 141, 31))
        self.fac_id_edit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.fac_email_Edt = QLineEdit(self.centralwidget)
        self.fac_email_Edt.setObjectName(u"fac_email_Edt")
        self.fac_email_Edt.setGeometry(QRect(280, 300, 141, 31))
        self.fac_email_Edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.fac_phone_edt = QLineEdit(self.centralwidget)
        self.fac_phone_edt.setObjectName(u"fac_phone_edt")
        self.fac_phone_edt.setGeometry(QRect(610, 300, 141, 31))
        self.fac_phone_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(120, 340, 111, 41))
        self.label_9.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(480, 340, 91, 41))
        self.label_10.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(610, 350, 141, 31))
        self.comboBox_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.password_edt = QLineEdit(self.centralwidget)
        self.password_edt.setObjectName(u"password_edt")
        self.password_edt.setGeometry(QRect(280, 400, 141, 31))
        self.password_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(120, 390, 91, 41))
        self.label_11.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.fac_dep_id_edt = QLineEdit(self.centralwidget)
        self.fac_dep_id_edt.setObjectName(u"fac_dep_id_edt")
        self.fac_dep_id_edt.setGeometry(QRect(280, 350, 141, 31))
        self.fac_dep_id_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(470, 400, 131, 41))
        self.label_12.setStyleSheet(u"font: italic 14pt \"Goudy Old Style\";")
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.confiem_pass_edt = QLineEdit(self.centralwidget)
        self.confiem_pass_edt.setObjectName(u"confiem_pass_edt")
        self.confiem_pass_edt.setGeometry(QRect(610, 400, 141, 31))
        self.confiem_pass_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.Register_btn = QPushButton(self.centralwidget)
        self.Register_btn.setObjectName(u"Register_btn")
        self.Register_btn.setGeometry(QRect(350, 490, 181, 41))
        self.Register_btn.setStyleSheet(u"QPushButton {\n"
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
        Register_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(Register_page)

        QMetaObject.connectSlotsByName(Register_page)
    # setupUi

    def retranslateUi(self, Register_page):
        Register_page.setWindowTitle(QCoreApplication.translate("Register_page", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("Register_page", u"LEAVE MANAGEMENT SYSTEM", None))
        self.label.setText(QCoreApplication.translate("Register_page", u"Register", None))
        self.label_2.setText(QCoreApplication.translate("Register_page", u"First Name", None))
        self.label_3.setText(QCoreApplication.translate("Register_page", u"Last Name", None))
        self.label_4.setText(QCoreApplication.translate("Register_page", u"Designation", None))
        self.label_5.setText(QCoreApplication.translate("Register_page", u"UserName", None))
        self.label_6.setText(QCoreApplication.translate("Register_page", u"Email", None))
        self.label_8.setText(QCoreApplication.translate("Register_page", u"Phone Number", None))
        self.label_9.setText(QCoreApplication.translate("Register_page", u"Department id", None))
        self.label_10.setText(QCoreApplication.translate("Register_page", u"Gender", None))
        self.label_11.setText(QCoreApplication.translate("Register_page", u"Password", None))
        self.label_12.setText(QCoreApplication.translate("Register_page", u"Confirm Password", None))
        self.Register_btn.setText(QCoreApplication.translate("Register_page", u"Register", None))
    # retranslateUi

