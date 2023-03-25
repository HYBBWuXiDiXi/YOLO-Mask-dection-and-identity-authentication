# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Homepage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homePage_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1342, 745)
        MainWindow.setStyleSheet("#centralwidget{border-image: url(:/img/img/back.jpg)}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 0, 1141, 751))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.homepage = QtWidgets.QWidget()
        self.homepage.setObjectName("homepage")
        self.label_6 = QtWidgets.QLabel(self.homepage)
        self.label_6.setGeometry(QtCore.QRect(340, 50, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(self.homepage)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 210, 771, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.stackedWidget.addWidget(self.homepage)
        self.identify_page = QtWidgets.QWidget()
        self.identify_page.setObjectName("identify_page")
        self.vedio_label = QtWidgets.QLabel(self.identify_page)
        self.vedio_label.setGeometry(QtCore.QRect(90, 150, 640, 480))
        self.vedio_label.setObjectName("vedio_label")
        self.identify_start_button = QtWidgets.QPushButton(self.identify_page)
        self.identify_start_button.setGeometry(QtCore.QRect(820, 280, 110, 38))
        self.identify_start_button.setStyleSheet("QPushButton{\n"
                                                 "border-radius:15px;\n"
                                                 "font-weight:blod;\n"
                                                 "background-color: rgb(246, 170, 101);\n"
                                                 "}\n"
                                                 "QPushButton:pressed{\n"
                                                 "font-weight:blod;\n"
                                                 "padding-top:3px;\n"
                                                 "padding-left:3px;\n"
                                                 "}")
        self.identify_start_button.setObjectName("identify_start_button")
        self.identify_exit_button = QtWidgets.QPushButton(self.identify_page)
        self.identify_exit_button.setGeometry(QtCore.QRect(820, 480, 110, 38))
        self.identify_exit_button.setStyleSheet("QPushButton{\n"
                                                "border-radius:15px;\n"
                                                "font-weight:blod;\n"
                                                "background-color: rgb(246, 170, 101);\n"
                                                "}\n"
                                                "QPushButton:pressed{\n"
                                                "font-weight:blod;\n"
                                                "padding-top:3px;\n"
                                                "padding-left:3px;\n"
                                                "}")
        self.identify_exit_button.setObjectName("identify_exit_button")
        self.identify_compare_button = QtWidgets.QPushButton(self.identify_page)
        self.identify_compare_button.setGeometry(QtCore.QRect(820, 380, 110, 38))
        self.identify_compare_button.setStyleSheet("QPushButton{\n"
                                                   "border-radius:15px;\n"
                                                   "font-weight:blod;\n"
                                                   "background-color: rgb(246, 170, 101);\n"
                                                   "}\n"
                                                   "QPushButton:pressed{\n"
                                                   "font-weight:blod;\n"
                                                   "padding-top:3px;\n"
                                                   "padding-left:3px;\n"
                                                   "}")
        self.identify_compare_button.setObjectName("identify_compare_button")
        self.stackedWidget.addWidget(self.identify_page)
        self.information_page = QtWidgets.QWidget()
        self.information_page.setObjectName("information_page")
        self.label = QtWidgets.QLabel(self.information_page)
        self.label.setGeometry(QtCore.QRect(90, 230, 81, 31))
        self.label.setObjectName("label")
        self.uploaded_img = QtWidgets.QLabel(self.information_page)
        self.uploaded_img.setGeometry(QtCore.QRect(200, 120, 221, 250))
        self.uploaded_img.setStyleSheet(
            "*{background: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(214,249,255,100) , stop:1 rgba(158,232,250,100)); border: 2px solid rgba(205,92,92,255); border-radius:20px;}")
        self.uploaded_img.setObjectName("uploaded_img")
        self.upload_img = QtWidgets.QPushButton(self.information_page)
        self.upload_img.setGeometry(QtCore.QRect(460, 220, 110, 38))
        self.upload_img.setStyleSheet("QPushButton{\n"
                                      "border-radius:15px;\n"
                                      "font-weight:blod;\n"
                                      "background-color: rgb(246, 170, 101);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "font-weight:blod;\n"
                                      "padding-top:3px;\n"
                                      "padding-left:3px;\n"
                                      "}")
        self.upload_img.setObjectName("upload_img")
        self.label_2 = QtWidgets.QLabel(self.information_page)
        self.label_2.setGeometry(QtCore.QRect(80, 430, 81, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.information_page)
        self.lineEdit.setGeometry(QtCore.QRect(210, 430, 211, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.upload_button_ok = QtWidgets.QPushButton(self.information_page)
        self.upload_button_ok.setGeometry(QtCore.QRect(250, 520, 110, 38))
        self.upload_button_ok.setStyleSheet("QPushButton{\n"
                                            "border-radius:15px;\n"
                                            "font-weight:blod;\n"
                                            "background-color: rgb(246, 170, 101);\n"
                                            "}\n"
                                            "QPushButton:pressed{\n"
                                            "font-weight:blod;\n"
                                            "padding-top:3px;\n"
                                            "padding-left:3px;\n"
                                            "}")
        self.upload_button_ok.setObjectName("upload_button_ok")
        self.label_3 = QtWidgets.QLabel(self.information_page)
        self.label_3.setGeometry(QtCore.QRect(190, 380, 411, 16))
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.information_page)
        self.app_page = QtWidgets.QWidget()
        self.app_page.setObjectName("app_page")
        self.label_4 = QtWidgets.QLabel(self.app_page)
        self.label_4.setGeometry(QtCore.QRect(30, 60, 301, 31))
        self.label_4.setStyleSheet("font: 10pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.app_page)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 301, 31))
        self.label_5.setStyleSheet("font: 10pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.app_page)
        self.label_10.setGeometry(QtCore.QRect(30, 210, 681, 31))
        self.label_10.setStyleSheet("font: 10pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.app_page)
        self.identify_button = QtWidgets.QPushButton(self.centralwidget)
        self.identify_button.setGeometry(QtCore.QRect(40, 306, 110, 38))
        self.identify_button.setStyleSheet("QPushButton{\n"
                                           "border-radius:15px;\n"
                                           "font-weight:blod;\n"
                                           "background-color: rgb(246, 218, 217);\n"
                                           "}\n"
                                           "QPushButton:pressed{\n"
                                           "font-weight:blod;\n"
                                           "padding-top:3px;\n"
                                           "padding-left:3px;\n"
                                           "}")
        self.identify_button.setObjectName("identify_button")
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(40, 206, 110, 38))
        self.home_button.setStyleSheet("QPushButton{\n"
                                       "border-radius:15px;\n"
                                       "font-weight:blod;\n"
                                       "background-color: rgb(246, 218, 217);\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "font-weight:blod;\n"
                                       "padding-top:3px;\n"
                                       "padding-left:3px;\n"
                                       "}")
        self.home_button.setObjectName("home_button")
        self.information_button = QtWidgets.QPushButton(self.centralwidget)
        self.information_button.setGeometry(QtCore.QRect(40, 406, 110, 38))
        self.information_button.setStyleSheet("QPushButton{\n"
                                              "border-radius:15px;\n"
                                              "font-weight:blod;\n"
                                              "background-color: rgb(246, 218, 217);\n"
                                              "}\n"
                                              "QPushButton:pressed{\n"
                                              "font-weight:blod;\n"
                                              "padding-top:3px;\n"
                                              "padding-left:3px;\n"
                                              "}")
        self.information_button.setObjectName("information_button")
        self.app_button = QtWidgets.QPushButton(self.centralwidget)
        self.app_button.setGeometry(QtCore.QRect(40, 506, 110, 38))
        self.app_button.setStyleSheet("QPushButton{\n"
                                      "border-radius:15px;\n"
                                      "font-weight:blod;\n"
                                      "background-color: rgb(246, 218, 217);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "font-weight:blod;\n"
                                      "padding-top:3px;\n"
                                      "padding-left:3px;\n"
                                      "}")
        self.app_button.setObjectName("app_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "欢迎使用March人脸识别系统"))
        self.label_7.setText(_translate("MainWindow", "作者：江苏海洋大学大创团队（崔苏豪、郝佳乐、李姗、王紫程）"))
        self.label_8.setText(_translate("MainWindow", "技术栈：pyqt5+mysql+python3+卷积神经网络CNN+opencv2+YOLO+tensorflow"))
        self.label_9.setText(_translate("MainWindow", "如有技术问题，欢迎指正"))
        self.vedio_label.setText(_translate("MainWindow", "Waiting open your camera..."))
        self.identify_start_button.setText(_translate("MainWindow", "开始检测"))
        self.identify_exit_button.setText(_translate("MainWindow", "结束检测"))
        self.identify_compare_button.setText(_translate("MainWindow", "身份识别"))
        self.label.setText(_translate("MainWindow", "  头像"))
        self.uploaded_img.setText(_translate("MainWindow", "Waiting open your resource"))
        self.upload_img.setText(_translate("MainWindow", "上传图片"))
        self.label_2.setText(_translate("MainWindow", "  用户姓名"))
        self.upload_button_ok.setText(_translate("MainWindow", "确认"))
        self.label_3.setText(_translate("MainWindow", "温馨提示：上传的照片需要正脸照，保证光线充足,角度合理"))
        self.label_4.setText(_translate("MainWindow", "app-version:1.0.0"))
        self.label_5.setText(_translate("MainWindow", "app-create-time:2023.03"))
        self.label_10.setText(_translate("MainWindow", "app-content:March口罩人脸识别系统，可应用于面向打卡、签到等多种领域"))
        self.identify_button.setText(_translate("MainWindow", "人脸检测"))
        self.home_button.setText(_translate("MainWindow", "主页"))
        self.information_button.setText(_translate("MainWindow", "信息录入"))
        self.app_button.setText(_translate("MainWindow", "关于"))