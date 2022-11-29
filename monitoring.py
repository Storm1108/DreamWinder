# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitoring.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 605)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.mainFrame = QtWidgets.QWidget(MainWindow)
        self.mainFrame.setStyleSheet("background-color: rgb(228, 251, 255);\n"
                                     "color: rgb(0, 0, 0);")
        self.mainFrame.setObjectName("mainFrame")
        self.mainLayout = QtWidgets.QVBoxLayout(self.mainFrame)
        self.mainLayout.setObjectName("mainLayout")
        self.progressWidget = QtWidgets.QWidget(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressWidget.sizePolicy().hasHeightForWidth())
        self.progressWidget.setSizePolicy(sizePolicy)
        self.progressWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.progressWidget.setObjectName("progressWidget")
        self.progressLayout = QtWidgets.QHBoxLayout(self.progressWidget)
        self.progressLayout.setContentsMargins(-1, -1, 15, -1)
        self.progressLayout.setSpacing(20)
        self.progressLayout.setObjectName("progressLayout")
        self.progressBar = QtWidgets.QProgressBar(self.progressWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressLayout.addWidget(self.progressBar)
        self.pauseButton = QtWidgets.QPushButton(self.progressWidget)
        self.pauseButton.setMinimumSize(QtCore.QSize(100, 30))
        self.pauseButton.setObjectName("pauseButton")
        self.pauseButton.setStyleSheet("QPushButton {background-color: rgba(51, 102, 153, 50);"
                                       "font: 75 15pt \"PT Mono\";}"
                                       "QPushButton:pressed {background-color: rgba(51, 102, 153, 100);}")
        self.progressLayout.addWidget(self.pauseButton)
        self.mainLayout.addWidget(self.progressWidget)
        self.submainFrame = QtWidgets.QFrame(self.mainFrame)
        self.submainFrame.setStyleSheet("font: 75 15pt \"PT Mono\";")
        self.submainFrame.setObjectName("submainFrame")
        self.submainLayout = QtWidgets.QHBoxLayout(self.submainFrame)
        self.submainLayout.setObjectName("submainLayout")
        self.leftWidget = QtWidgets.QWidget(self.submainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftWidget.sizePolicy().hasHeightForWidth())
        self.leftWidget.setSizePolicy(sizePolicy)
        self.leftWidget.setObjectName("leftWidget")
        self.leftLayout = QtWidgets.QVBoxLayout(self.leftWidget)
        self.leftLayout.setObjectName("leftLayout")
        self.rotorTitle = QtWidgets.QLabel(self.leftWidget)
        self.rotorTitle.setStyleSheet("color: rgb(51, 102, 153);\n"
                                      "font: 1200  20pt \"Helvetica Neue\";")
        self.rotorTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.rotorTitle.setObjectName("rotorTitle")
        self.leftLayout.addWidget(self.rotorTitle)
        self.rotorPosition = QtWidgets.QDial(self.leftWidget)
        self.rotorPosition.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotorPosition.sizePolicy().hasHeightForWidth())
        self.rotorPosition.setSizePolicy(sizePolicy)
        self.rotorPosition.setMinimumSize(QtCore.QSize(270, 270))
        self.rotorPosition.setStyleSheet("background-color: rgb(0, 51, 102);")
        self.rotorPosition.setObjectName("rotorPosition")
        self.leftLayout.addWidget(self.rotorPosition)
        self.rotorDataWidget = QtWidgets.QWidget(self.leftWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotorDataWidget.sizePolicy().hasHeightForWidth())
        self.rotorDataWidget.setSizePolicy(sizePolicy)
        self.rotorDataWidget.setObjectName("rotorDataWidget")
        self.rotorDataLayout = QtWidgets.QHBoxLayout(self.rotorDataWidget)
        self.rotorDataLayout.setObjectName("rotorDataLayout")
        self.currentDegreeLabel = QtWidgets.QLabel(self.rotorDataWidget)
        self.currentDegreeLabel.setStyleSheet("font: 18pt \"PT Mono\";")
        self.currentDegreeLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.currentDegreeLabel.setObjectName("currentDegreeLabel")
        self.rotorDataLayout.addWidget(self.currentDegreeLabel)
        self.currentDegreeLCD = QtWidgets.QLCDNumber(self.rotorDataWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentDegreeLCD.sizePolicy().hasHeightForWidth())
        self.currentDegreeLCD.setSizePolicy(sizePolicy)
        self.currentDegreeLCD.setMinimumSize(QtCore.QSize(50, 30))
        self.currentDegreeLCD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.currentDegreeLCD.setFrameShape(QtWidgets.QFrame.Box)
        self.currentDegreeLCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.currentDegreeLCD.setDigitCount(3)
        self.currentDegreeLCD.setMode(QtWidgets.QLCDNumber.Dec)
        self.currentDegreeLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.currentDegreeLCD.setProperty("intValue", 360)
        self.currentDegreeLCD.setObjectName("currentDegreeLCD")
        self.currentDegreeLCD.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border: 1px solid gray;"
                                            "border-radius: 4px;"
                                            "padding: 0 8px;")
        self.rotorDataLayout.addWidget(self.currentDegreeLCD)
        self.currenRPMLabel = QtWidgets.QLabel(self.rotorDataWidget)
        self.currenRPMLabel.setStyleSheet("font: 18pt \"PT Mono\";")
        self.currenRPMLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.currenRPMLabel.setObjectName("currenRPMLabel")
        self.rotorDataLayout.addWidget(self.currenRPMLabel)
        self.currentRPM_LCD = QtWidgets.QLCDNumber(self.rotorDataWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentRPM_LCD.sizePolicy().hasHeightForWidth())
        self.currentRPM_LCD.setSizePolicy(sizePolicy)
        self.currentRPM_LCD.setMinimumSize(QtCore.QSize(50, 30))
        self.currentRPM_LCD.setFrameShape(QtWidgets.QFrame.Box)
        self.currentRPM_LCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.currentRPM_LCD.setSmallDecimalPoint(False)
        self.currentRPM_LCD.setDigitCount(2)
        self.currentRPM_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.currentRPM_LCD.setProperty("value", 56.0)
        self.currentRPM_LCD.setObjectName("currentRPM_LCD")
        self.currentRPM_LCD.setStyleSheet("background-color: rgb(255, 255, 255);"
                                          "border: 1px solid gray;"
                                          "border-radius: 4px;"
                                          "padding: 0 8px;")
        self.rotorDataLayout.addWidget(self.currentRPM_LCD)
        self.leftLayout.addWidget(self.rotorDataWidget)
        self.rotorSliderLine = QtWidgets.QFrame(self.leftWidget)
        self.rotorSliderLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rotorSliderLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.rotorSliderLine.setObjectName("rotorSliderLine")
        self.leftLayout.addWidget(self.rotorSliderLine)
        self.sliderTitle = QtWidgets.QLabel(self.leftWidget)
        self.sliderTitle.setStyleSheet("color: rgb(51, 102, 153);\n"
                                       "font: 1200  20pt \"Helvetica Neue\";")
        self.sliderTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.sliderTitle.setObjectName("sliderTitle")
        self.leftLayout.addWidget(self.sliderTitle)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.leftLayout.addItem(spacerItem)
        self.sliderPosition = QtWidgets.QSlider(self.leftWidget)
        self.sliderPosition.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderPosition.sizePolicy().hasHeightForWidth())
        self.sliderPosition.setSizePolicy(sizePolicy)
        self.sliderPosition.setMinimumSize(QtCore.QSize(0, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 51, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 51, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 51, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 51, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 51, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 51, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 51, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 51, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 51, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 251, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.sliderPosition.setPalette(palette)
        self.sliderPosition.setStyleSheet("color: rgb(0, 51, 102);")
        self.sliderPosition.setOrientation(QtCore.Qt.Horizontal)
        self.sliderPosition.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sliderPosition.setTickInterval(5)
        self.sliderPosition.setObjectName("sliderPosition")
        self.leftLayout.addWidget(self.sliderPosition)
        self.sliderDataWidget = QtWidgets.QWidget(self.leftWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderDataWidget.sizePolicy().hasHeightForWidth())
        self.sliderDataWidget.setSizePolicy(sizePolicy)
        self.sliderDataWidget.setObjectName("sliderDataWidget")
        self.sliderDataLayout = QtWidgets.QHBoxLayout(self.sliderDataWidget)
        self.sliderDataLayout.setObjectName("sliderDataLayout")
        self.currentPosLabel = QtWidgets.QLabel(self.sliderDataWidget)
        self.currentPosLabel.setStyleSheet("font: 18pt \"PT Mono\";\n"
                                           "")
        self.currentPosLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.currentPosLabel.setObjectName("currentPosLabel")
        self.sliderDataLayout.addWidget(self.currentPosLabel)
        self.currentPosLCD = QtWidgets.QLCDNumber(self.sliderDataWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentPosLCD.sizePolicy().hasHeightForWidth())
        self.currentPosLCD.setSizePolicy(sizePolicy)
        self.currentPosLCD.setMinimumSize(QtCore.QSize(50, 30))
        self.currentPosLCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.currentPosLCD.setDigitCount(4)
        self.currentPosLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.currentPosLCD.setObjectName("currentPosLCD")
        self.currentPosLCD.setStyleSheet("background-color: rgb(255, 255, 255);"
                                         "border: 1px solid gray;"
                                         "border-radius: 4px;"
                                         "padding: 0 8px;")
        self.sliderDataLayout.addWidget(self.currentPosLCD)
        self.currenSpeedLabel = QtWidgets.QLabel(self.sliderDataWidget)
        self.currenSpeedLabel.setStyleSheet("font: 18pt \"PT Mono\";")
        self.currenSpeedLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.currenSpeedLabel.setObjectName("currenSpeedLabel")
        self.sliderDataLayout.addWidget(self.currenSpeedLabel)
        self.currenSpeedLCD = QtWidgets.QLCDNumber(self.sliderDataWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currenSpeedLCD.sizePolicy().hasHeightForWidth())
        self.currenSpeedLCD.setSizePolicy(sizePolicy)
        self.currenSpeedLCD.setMinimumSize(QtCore.QSize(50, 30))
        self.currenSpeedLCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.currenSpeedLCD.setDigitCount(2)
        self.currenSpeedLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.currenSpeedLCD.setObjectName("currenSpeedLCD")
        self.currenSpeedLCD.setStyleSheet("background-color: rgb(255, 255, 255);"
                                          "border: 1px solid gray;"
                                          "border-radius: 4px;"
                                          "padding: 0 8px;")
        self.sliderDataLayout.addWidget(self.currenSpeedLCD)
        self.leftLayout.addWidget(self.sliderDataWidget)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.leftLayout.addItem(spacerItem1)
        self.submainLayout.addWidget(self.leftWidget)
        self.middleLine = QtWidgets.QFrame(self.submainFrame)
        self.middleLine.setStyleSheet("background-color: rgb(102, 102, 102);")
        self.middleLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.middleLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.middleLine.setObjectName("middleLine")
        self.submainLayout.addWidget(self.middleLine)
        self.rightWidget = QtWidgets.QWidget(self.submainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightWidget.sizePolicy().hasHeightForWidth())
        self.rightWidget.setSizePolicy(sizePolicy)
        self.rightWidget.setObjectName("rightWidget")
        self.rightLayout = QtWidgets.QVBoxLayout(self.rightWidget)
        self.rightLayout.setObjectName("rightLayout")
        self.label = QtWidgets.QLabel(self.rightWidget)
        self.label.setStyleSheet("color: rgb(51, 102, 153);\n"
                                 "font: 1200  20pt \"Helvetica Neue\";\n"
                                 "")
        self.label.setObjectName("label")
        self.rightLayout.addWidget(self.label)
        self.dataLayout = QtWidgets.QFormLayout()
        self.dataLayout.setObjectName("dataLayout")
        self.layer_NC = QtWidgets.QLabel(self.rightWidget)
        self.layer_NC.setObjectName("layer_NC")
        self.dataLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.layer_NC)
        self.layerLeftTime_NC = QtWidgets.QLabel(self.rightWidget)
        self.layerLeftTime_NC.setObjectName("layerLeftTime_NC")
        self.dataLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.layerLeftTime_NC)
        self.timeEnding_NC = QtWidgets.QLabel(self.rightWidget)
        self.timeEnding_NC.setObjectName("timeEnding_NC")
        self.dataLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.timeEnding_NC)
        self.timeLeft_NC = QtWidgets.QLabel(self.rightWidget)
        self.timeLeft_NC.setObjectName("timeLeft_NC")
        self.dataLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.timeLeft_NC)
        self.force_NC = QtWidgets.QLabel(self.rightWidget)
        self.force_NC.setObjectName("force_NC")
        self.dataLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.force_NC)
        self.layer_C = QtWidgets.QLineEdit(self.rightWidget)
        self.layer_C.setObjectName("layer_C")
        self.layer_C.setStyleSheet("background-color: rgb(255, 255, 255);"
                                   "border: 1px solid gray;"
                                   "border-radius: 4px;"
                                   "padding: 0 8px;")
        self.layer_C.setReadOnly(True)
        self.dataLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.layer_C)
        self.layerLeftTime_C = QtWidgets.QLineEdit(self.rightWidget)
        self.layerLeftTime_C.setObjectName("layerLeftTime_C")
        self.layerLeftTime_C.setStyleSheet("background-color: rgb(255, 255, 255);"
                                           "border: 1px solid gray;"
                                           "border-radius: 4px;"
                                           "padding: 0 8px;")
        self.layerLeftTime_C.setReadOnly(True)
        self.dataLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.layerLeftTime_C)
        self.timeLeft_C = QtWidgets.QLineEdit(self.rightWidget)
        self.timeLeft_C.setObjectName("timeLeft_C")
        self.timeLeft_C.setStyleSheet("background-color: rgb(255, 255, 255);"
                                      "border: 1px solid gray;"
                                      "border-radius: 4px;"
                                      "padding: 0 8px;")
        self.timeLeft_C.setReadOnly(True)
        self.dataLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.timeLeft_C)
        self.force_C = QtWidgets.QLineEdit(self.rightWidget)
        self.force_C.setObjectName("force_C")
        self.force_C.setStyleSheet("background-color: rgb(255, 255, 255);"
                                   "border: 1px solid gray;"
                                   "border-radius: 4px;"
                                   "padding: 0 8px;")
        self.force_C.setReadOnly(True)
        self.dataLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.force_C)
        self.timeEnding_C = QtWidgets.QLineEdit(self.rightWidget)
        self.timeEnding_C.setObjectName("timeEnding_C")
        self.timeEnding_C.setStyleSheet("background-color: rgb(255, 255, 255);"
                                        "border: 1px solid gray;"
                                        "border-radius: 4px;"
                                        "padding: 0 8px;")
        self.timeEnding_C.setReadOnly(True)
        self.dataLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.timeEnding_C)
        self.rightLayout.addLayout(self.dataLayout)
        self.commandsLine = QtWidgets.QFrame(self.rightWidget)
        self.commandsLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.commandsLine.setObjectName("commandsLine")
        self.rightLayout.addWidget(self.commandsLine)
        self.commandsTitle = QtWidgets.QLabel(self.rightWidget)
        self.commandsTitle.setStyleSheet("color: rgb(51, 102, 153);\n"
                                         "font: 1200  20pt \"Helvetica Neue\";\n"
                                         "\n"
                                         "")
        self.commandsTitle.setObjectName("commandsTitle")
        self.rightLayout.addWidget(self.commandsTitle)
        self.listWidget = QtWidgets.QListWidget(self.rightWidget)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.rightLayout.addWidget(self.listWidget)
        self.submainLayout.addWidget(self.rightWidget)
        self.mainLayout.addWidget(self.submainFrame)
        MainWindow.setCentralWidget(self.mainFrame)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pauseButton.setText(_translate("MainWindow", "Пауза/Пуск"))
        self.rotorTitle.setText(_translate("MainWindow", "Положение ротора"))
        self.currentDegreeLabel.setText(_translate("MainWindow", "Текущий угол, град.: "))
        self.currenRPMLabel.setText(_translate("MainWindow", "RPM: "))
        self.sliderTitle.setText(_translate("MainWindow", "Положение каретки"))
        self.currentPosLabel.setText(_translate("MainWindow", "Текущая координата, мм:"))
        self.currenSpeedLabel.setText(_translate("MainWindow", "Скорость, мм/с:"))
        self.label.setText(_translate("MainWindow", "Текущие данные намотки"))
        self.layer_NC.setText(_translate("MainWindow", "Слой в работе:"))
        self.layerLeftTime_NC.setText(_translate("MainWindow", "Осталось до намотки слоя:"))
        self.timeEnding_NC.setText(_translate("MainWindow", "Время окончания:"))
        self.timeLeft_NC.setText(_translate("MainWindow", "Осталось всего:"))
        self.force_NC.setText(_translate("MainWindow", "Текущее натяжение нити:"))
        self.commandsTitle.setText(_translate("MainWindow", "Команды G-code"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Команда 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Команда 2"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Команда 3"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Команда 4"))
        self.listWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
