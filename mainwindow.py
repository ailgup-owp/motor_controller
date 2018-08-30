# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(320, 240))
        MainWindow.setMaximumSize(QtCore.QSize(320, 400))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.falcon_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.falcon_button.sizePolicy().hasHeightForWidth())
        self.falcon_button.setSizePolicy(sizePolicy)
        self.falcon_button.setMinimumSize(QtCore.QSize(0, 30))
        self.falcon_button.setMaximumSize(QtCore.QSize(999, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.falcon_button.setFont(font)
        self.falcon_button.setStyleSheet("QPushButton{color:blue};")
        self.falcon_button.setObjectName("falcon_button")
        self.gridLayout.addWidget(self.falcon_button, 0, 1, 1, 1)
        self.br_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.br_button.setMinimumSize(QtCore.QSize(0, 30))
        self.br_button.setMaximumSize(QtCore.QSize(999, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.br_button.setFont(font)
        self.br_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.br_button.setObjectName("br_button")
        self.gridLayout.addWidget(self.br_button, 0, 3, 1, 1)
        self.br2_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.br2_button.setMinimumSize(QtCore.QSize(0, 30))
        self.br2_button.setMaximumSize(QtCore.QSize(999, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.br2_button.setFont(font)
        self.br2_button.setObjectName("br2_button")
        self.gridLayout.addWidget(self.br2_button, 0, 5, 1, 1)
        self.savox_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.savox_button.setMinimumSize(QtCore.QSize(0, 30))
        self.savox_button.setMaximumSize(QtCore.QSize(999, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.savox_button.setFont(font)
        self.savox_button.setObjectName("savox_button")
        self.gridLayout.addWidget(self.savox_button, 0, 2, 1, 1)
        self.maxon_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.maxon_button.setMinimumSize(QtCore.QSize(0, 30))
        self.maxon_button.setMaximumSize(QtCore.QSize(999, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.maxon_button.setFont(font)
        self.maxon_button.setObjectName("maxon_button")
        self.gridLayout.addWidget(self.maxon_button, 0, 4, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 33, 321, 131))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.forward_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forward_button.sizePolicy().hasHeightForWidth())
        self.forward_button.setSizePolicy(sizePolicy)
        self.forward_button.setMinimumSize(QtCore.QSize(0, 0))
        self.forward_button.setMaximumSize(QtCore.QSize(16777215, 999))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.forward_button.setFont(font)
        self.forward_button.setObjectName("forward_button")
        self.verticalLayout_5.addWidget(self.forward_button)
        self.reverse_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reverse_button.sizePolicy().hasHeightForWidth())
        self.reverse_button.setSizePolicy(sizePolicy)
        self.reverse_button.setMaximumSize(QtCore.QSize(16777215, 999))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.reverse_button.setFont(font)
        self.reverse_button.setObjectName("reverse_button")
        self.verticalLayout_5.addWidget(self.reverse_button)
        self.stop_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        self.stop_button.setMaximumSize(QtCore.QSize(16777215, 999))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.stop_button.setFont(font)
        self.stop_button.setStyleSheet("QPushButton{color:red};")
        self.stop_button.setCheckable(False)
        self.stop_button.setObjectName("stop_button")
        self.verticalLayout_5.addWidget(self.stop_button)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.motor_name = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.motor_name.setFont(font)
        self.motor_name.setAlignment(QtCore.Qt.AlignCenter)
        self.motor_name.setObjectName("motor_name")
        self.verticalLayout_2.addWidget(self.motor_name)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.measured_velocity = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.measured_velocity.setFont(font)
        self.measured_velocity.setAlignment(QtCore.Qt.AlignCenter)
        self.measured_velocity.setObjectName("measured_velocity")
        self.verticalLayout_2.addWidget(self.measured_velocity)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.set_velocity_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.set_velocity_label.setMaximumSize(QtCore.QSize(16777215, 99999))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.set_velocity_label.setFont(font)
        self.set_velocity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.set_velocity_label.setObjectName("set_velocity_label")
        self.verticalLayout_3.addWidget(self.set_velocity_label)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vel_up = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vel_up.sizePolicy().hasHeightForWidth())
        self.vel_up.setSizePolicy(sizePolicy)
        self.vel_up.setMinimumSize(QtCore.QSize(0, 0))
        self.vel_up.setMaximumSize(QtCore.QSize(16777215, 999))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.vel_up.setFont(font)
        self.vel_up.setObjectName("vel_up")
        self.verticalLayout.addWidget(self.vel_up)
        self.vel_up_10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vel_up_10.sizePolicy().hasHeightForWidth())
        self.vel_up_10.setSizePolicy(sizePolicy)
        self.vel_up_10.setMaximumSize(QtCore.QSize(16777215, 999))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.vel_up_10.setFont(font)
        self.vel_up_10.setObjectName("vel_up_10")
        self.verticalLayout.addWidget(self.vel_up_10)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.vel_down = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vel_down.sizePolicy().hasHeightForWidth())
        self.vel_down.setSizePolicy(sizePolicy)
        self.vel_down.setMaximumSize(QtCore.QSize(16777215, 999))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.vel_down.setFont(font)
        self.vel_down.setObjectName("vel_down")
        self.verticalLayout_4.addWidget(self.vel_down)
        self.vel_down_10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vel_down_10.sizePolicy().hasHeightForWidth())
        self.vel_down_10.setSizePolicy(sizePolicy)
        self.vel_down_10.setMaximumSize(QtCore.QSize(16777215, 999))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.vel_down_10.setFont(font)
        self.vel_down_10.setObjectName("vel_down_10")
        self.verticalLayout_4.addWidget(self.vel_down_10)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.vel_down.pressed.connect(MainWindow.down_velocity)
        self.reverse_button.pressed.connect(MainWindow.set_motor_state)
        self.vel_up.pressed.connect(MainWindow.up_velocity)
        self.forward_button.pressed.connect(MainWindow.set_motor_state)
        self.stop_button.pressed.connect(MainWindow.set_motor_state)
        self.falcon_button.pressed.connect(MainWindow.button_handler)
        self.br_button.pressed.connect(MainWindow.button_handler)
        self.br2_button.pressed.connect(MainWindow.button_handler)
        self.maxon_button.pressed.connect(MainWindow.button_handler)
        self.savox_button.pressed.connect(MainWindow.button_handler)
        self.vel_up_10.pressed.connect(MainWindow.up_velocity_10)
        self.vel_down_10.pressed.connect(MainWindow.down_velocity_10)
        self.pushButton.pressed.connect(MainWindow.open_var_win)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.falcon_button.setText(_translate("MainWindow", "Falcon\n"
"Pump"))
        self.br_button.setText(_translate("MainWindow", "Blue\n"
"Robotics"))
        self.br2_button.setText(_translate("MainWindow", "Blue \n"
"Robotics 2"))
        self.savox_button.setText(_translate("MainWindow", "Falcon\n"
"Savox"))
        self.maxon_button.setText(_translate("MainWindow", "Maxon\n"
"Sensorless"))
        self.forward_button.setText(_translate("MainWindow", "Forward"))
        self.reverse_button.setText(_translate("MainWindow", "Reverse"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.motor_name.setText(_translate("MainWindow", "Falcon"))
        self.label_3.setText(_translate("MainWindow", "Measured Velocity:"))
        self.measured_velocity.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Set Velocity:"))
        self.set_velocity_label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "More Stats"))
        self.vel_up.setText(_translate("MainWindow", "⇈ (+100)"))
        self.vel_up_10.setText(_translate("MainWindow", "↑ (+10)"))
        self.vel_down.setText(_translate("MainWindow", "⇊ (-100)"))
        self.vel_down_10.setText(_translate("MainWindow", "↓ (-10)"))

