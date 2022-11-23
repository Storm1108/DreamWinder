# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configPreviewNew.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfigElement(object):
    def setupUi(self, ConfigElement):
        ConfigElement.setObjectName("ConfigElement")
        ConfigElement.resize(903, 179)
        ConfigElement.setStyleSheet("")
        self.mainlLayout = QtWidgets.QVBoxLayout(ConfigElement)
        self.mainlLayout.setContentsMargins(0, 0, 0, 0)
        self.mainlLayout.setSpacing(0)
        self.mainlLayout.setObjectName("mainlLayout")
        self.lineUpper = QtWidgets.QFrame(ConfigElement)
        self.lineUpper.setStyleSheet("background-color: rgb(98, 98, 98);")
        self.lineUpper.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineUpper.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineUpper.setObjectName("lineUpper")
        self.mainFrame = QtWidgets.QFrame(ConfigElement)
        self.mainFrame.setAutoFillBackground(True)
        self.mainFrame.setStyleSheet(
            ".QFrame {background-image: url(lightTexture2.png);}")
        self.mainFrame.setObjectName("mainFrame")
        self.submainLayout = QtWidgets.QVBoxLayout(self.mainFrame)
        self.submainLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.submainLayout.setContentsMargins(0, 0, 0, 0)
        self.submainLayout.setSpacing(0)
        self.submainLayout.setObjectName("submainLayout")
        self.title = QtWidgets.QLabel(self.mainFrame)
        self.title.setMouseTracking(False)
        self.title.setStyleSheet("font: 18pt \"Andale Mono\";\n"
                                 "color: rgb(0, 102, 153);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.submainLayout.addWidget(self.title)
        self.submainLayout.addWidget(self.lineUpper)
        self.textWidgetMain = QtWidgets.QWidget(self.mainFrame)
        self.textWidgetMain.setAutoFillBackground(False)
        self.textWidgetMain.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "font: 150 14pt \"PT Mono\";")
        self.textWidgetMain.setObjectName("textWidgetMain")
        self.textLayoutMain = QtWidgets.QHBoxLayout(self.textWidgetMain)
        self.textLayoutMain.setContentsMargins(20, 0, 30, 0)
        self.textLayoutMain.setSpacing(0)
        self.textLayoutMain.setObjectName("textLayoutMain")
        self.textLayoutLeft = QtWidgets.QFormLayout()
        self.textLayoutLeft.setContentsMargins(-1, -1, 10, -1)
        self.textLayoutLeft.setVerticalSpacing(8)
        self.textLayoutLeft.setHorizontalSpacing(8)
        self.textLayoutLeft.setObjectName("formLayout")
        self.materialNC = QtWidgets.QLabel(self.textWidgetMain)
        self.materialNC.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "font: 75 14pt \"PT Mono\";")
        self.materialNC.setObjectName("materialNC_2")
        self.textLayoutLeft.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.materialNC)
        self.materialC = QtWidgets.QLabel(self.textWidgetMain)
        self.materialC.setObjectName("materialC")
        self.textLayoutLeft.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.materialC)
        self.diamNC = QtWidgets.QLabel(self.textWidgetMain)
        self.diamNC.setIndent(17)
        self.diamNC.setObjectName("diamNC")
        self.textLayoutLeft.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.diamNC)
        self.diamC = QtWidgets.QLabel(self.textWidgetMain)
        self.diamC.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "font: 75 14pt \"PT Mono\";")
        self.diamC.setObjectName("diamC")
        self.textLayoutLeft.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.diamC)
        self.lengthNC = QtWidgets.QLabel(self.textWidgetMain)
        self.lengthNC.setIndent(32)
        self.lengthNC.setObjectName("lengthNC")
        self.textLayoutLeft.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lengthNC)
        self.lengthC = QtWidgets.QLabel(self.textWidgetMain)
        self.lengthC.setObjectName("lengthC")
        self.textLayoutLeft.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lengthC)
        self.textLayoutMain.addLayout(self.textLayoutLeft)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.textLayoutMain.addItem(spacerItem)
        self.lineMiddle = QtWidgets.QFrame(self.textWidgetMain)
        self.lineMiddle.setStyleSheet("background-color: rgb(98, 98, 98);")
        self.lineMiddle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lineMiddle.setLineWidth(0)
        self.lineMiddle.setMidLineWidth(1)
        self.lineMiddle.setFrameShape(QtWidgets.QFrame.VLine)
        self.lineMiddle.setObjectName("lineMiddle")
        self.textLayoutMain.addWidget(self.lineMiddle)
        self.textLayoutRight = QtWidgets.QFormLayout()
        self.textLayoutRight.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.textLayoutRight.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.textLayoutRight.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.textLayoutRight.setLabelAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.textLayoutRight.setFormAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.textLayoutRight.setObjectName("textLayoutRight")
        self.textLayoutRight.setContentsMargins(15, 0, 0, 0)
        self.textLayoutRight.setVerticalSpacing(8)
        self.textLayoutRight.setHorizontalSpacing(8)
        self.layerCountNC = QtWidgets.QLabel(self.textWidgetMain)
        self.layerCountNC.setObjectName("layerCountNC")
        self.textLayoutRight.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.layerCountNC)
        self.layerCountC = QtWidgets.QLabel(self.textWidgetMain)
        self.layerCountC.setObjectName("layerCountC")
        self.textLayoutRight.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.layerCountC)
        self.isPrevNC = QtWidgets.QLabel(self.textWidgetMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isPrevNC.sizePolicy().hasHeightForWidth())
        self.isPrevNC.setSizePolicy(sizePolicy)
        self.isPrevNC.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.isPrevNC.setIndent(60)
        self.isPrevNC.setObjectName("isPrevNC")
        self.textLayoutRight.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.isPrevNC)
        self.isPrevC = QtWidgets.QLabel(self.textWidgetMain)
        self.isPrevC.setObjectName("isPrevC")
        self.textLayoutRight.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.isPrevC)
        self.degreeNC = QtWidgets.QLabel(self.textWidgetMain)
        self.degreeNC.setIndent(15)
        self.degreeNC.setObjectName("degreeNC")
        self.textLayoutRight.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.degreeNC)
        self.degreeC = QtWidgets.QLabel(self.textWidgetMain)
        self.degreeC.setObjectName("degreeC")
        self.textLayoutRight.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.degreeC)
        self.textLayoutMain.addLayout(self.textLayoutRight)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.textLayoutMain.addItem(spacerItem1)
        self.edit_btn = QtWidgets.QPushButton(self.textWidgetMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_btn.sizePolicy().hasHeightForWidth())
        self.edit_btn.setSizePolicy(sizePolicy)
        self.edit_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.edit_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("PT Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(18)
        self.edit_btn.setFont(font)
        self.edit_btn.setStyleSheet("background-color: rgb(240, 240, 240);\n"
                                    "color: rgb(0,0,0)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("free-icon-edit-info-7033287.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_btn.setIcon(icon)
        self.edit_btn.setIconSize(QtCore.QSize(48, 48))
        self.edit_btn.setDefault(True)
        self.edit_btn.setObjectName("edit_btn")
        self.textLayoutMain.addWidget(self.edit_btn)
        self.submainLayout.addWidget(self.textWidgetMain)
        self.mainlLayout.addWidget(self.mainFrame)
        self.lineBottom = QtWidgets.QFrame(ConfigElement)
        self.lineBottom.setStyleSheet("background-color: rgb(98, 98, 98);")
        self.lineBottom.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineBottom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineBottom.setObjectName("lineBottom")
        self.mainlLayout.addWidget(self.lineBottom)
        spacerItem2 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainlLayout.addItem(spacerItem2)

        self.retranslateUi(ConfigElement)
        QtCore.QMetaObject.connectSlotsByName(ConfigElement)

    def retranslateUi(self, ConfigElement):
        _translate = QtCore.QCoreApplication.translate
        ConfigElement.setWindowTitle(_translate("ConfigElement", "Form"))
        self.title.setText(_translate("ConfigElement", "Имя конфигурации"))
        self.materialNC.setText(_translate("ConfigElement", "Намоточный материал:"))
        self.materialC.setText(_translate("ConfigElement", "TextLabel"))
        self.diamNC.setText(_translate("ConfigElement", "Диаметр заготовки:"))
        self.diamC.setText(_translate("ConfigElement", "TextLabel"))
        self.lengthNC.setText(_translate("ConfigElement", "Длина заготовки:"))
        self.lengthC.setText(_translate("ConfigElement", "TextLabel"))
        self.layerCountNC.setText(_translate("ConfigElement", "Количество слоев намотки:"))
        self.layerCountC.setText(_translate("ConfigElement", "TextLabel"))
        self.isPrevNC.setText(_translate("ConfigElement", "Первичная обмотка:"))
        self.isPrevC.setText(_translate("ConfigElement", "TextLabel"))
        self.degreeNC.setText(_translate("ConfigElement", "Угол первичной намотки:"))
        self.degreeC.setText(_translate("ConfigElement", "TextLabel"))
        self.edit_btn.setText(_translate("ConfigElement", " Изменить"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ConfigElement = QtWidgets.QWidget()
    ui = Ui_ConfigElement()
    ui.setupUi(ConfigElement)
    ConfigElement.show()
    sys.exit(app.exec_())
