# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlgSettings(object):
    def setupUi(self, DlgSettings):
        DlgSettings.setObjectName("DlgSettings")
        DlgSettings.resize(231, 131)
        DlgSettings.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout = QtWidgets.QGridLayout(DlgSettings)
        self.gridLayout.setObjectName("gridLayout")
        self.lblFontSize = QtWidgets.QLabel(DlgSettings)
        self.lblFontSize.setObjectName("lblFontSize")
        self.gridLayout.addWidget(self.lblFontSize, 0, 0, 1, 1)
        self.sldFontSize = QtWidgets.QSlider(DlgSettings)
        self.sldFontSize.setMinimum(1)
        self.sldFontSize.setOrientation(QtCore.Qt.Horizontal)
        self.sldFontSize.setObjectName("sldFontSize")
        self.gridLayout.addWidget(self.sldFontSize, 0, 2, 1, 2)
        self.lblLineSize = QtWidgets.QLabel(DlgSettings)
        self.lblLineSize.setObjectName("lblLineSize")
        self.gridLayout.addWidget(self.lblLineSize, 1, 0, 1, 1)
        self.sldLineSize = QtWidgets.QSlider(DlgSettings)
        self.sldLineSize.setOrientation(QtCore.Qt.Horizontal)
        self.sldLineSize.setObjectName("sldLineSize")
        self.gridLayout.addWidget(self.sldLineSize, 1, 2, 1, 2)
        self.lblTransparency = QtWidgets.QLabel(DlgSettings)
        self.lblTransparency.setObjectName("lblTransparency")
        self.gridLayout.addWidget(self.lblTransparency, 2, 0, 1, 2)
        self.sldTransparency = QtWidgets.QSlider(DlgSettings)
        self.sldTransparency.setMinimum(1)
        self.sldTransparency.setMaximum(255)
        self.sldTransparency.setOrientation(QtCore.Qt.Horizontal)
        self.sldTransparency.setObjectName("sldTransparency")
        self.gridLayout.addWidget(self.sldTransparency, 2, 2, 1, 2)
        self.sldLblIndent = QtWidgets.QSlider(DlgSettings)
        self.sldLblIndent.setOrientation(QtCore.Qt.Horizontal)
        self.sldLblIndent.setObjectName("sldLblIndent")
        self.gridLayout.addWidget(self.sldLblIndent, 3, 2, 1, 2)
        self.btnOK = QtWidgets.QPushButton(DlgSettings)
        self.btnOK.setObjectName("btnOK")
        self.gridLayout.addWidget(self.btnOK, 4, 1, 1, 2)
        self.btnCancel = QtWidgets.QPushButton(DlgSettings)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout.addWidget(self.btnCancel, 4, 3, 1, 1)
        self.lblIndent = QtWidgets.QLabel(DlgSettings)
        self.lblIndent.setObjectName("lblIndent")
        self.gridLayout.addWidget(self.lblIndent, 3, 0, 1, 2)

        self.retranslateUi(DlgSettings)
        QtCore.QMetaObject.connectSlotsByName(DlgSettings)

    def retranslateUi(self, DlgSettings):
        _translate = QtCore.QCoreApplication.translate
        DlgSettings.setWindowTitle(_translate("DlgSettings", "Settings"))
        self.lblFontSize.setText(_translate("DlgSettings", "Font size:"))
        self.lblLineSize.setText(_translate("DlgSettings", "Line size:"))
        self.lblTransparency.setText(_translate("DlgSettings", "Transparency:"))
        self.btnOK.setText(_translate("DlgSettings", "OK"))
        self.btnCancel.setText(_translate("DlgSettings", "Cancel"))
        self.lblIndent.setText(_translate("DlgSettings", "Label indent:"))

