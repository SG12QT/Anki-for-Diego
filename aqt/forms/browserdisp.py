# -*- coding: utf-8 -*-
# pylint: disable=unsubscriptable-object,unused-import
from anki.lang import _
# Form implementation generated from reading ui file 'designer/browserdisp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 241)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.qfmt = QtWidgets.QLineEdit(Dialog)
        self.qfmt.setObjectName("qfmt")
        self.verticalLayout.addWidget(self.qfmt)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.afmt = QtWidgets.QLineEdit(Dialog)
        self.afmt.setObjectName("afmt")
        self.verticalLayout.addWidget(self.afmt)
        self.overrideFont = QtWidgets.QCheckBox(Dialog)
        self.overrideFont.setObjectName("overrideFont")
        self.verticalLayout.addWidget(self.overrideFont)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.font = QtWidgets.QFontComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font.sizePolicy().hasHeightForWidth())
        self.font.setSizePolicy(sizePolicy)
        self.font.setObjectName("font")
        self.horizontalLayout.addWidget(self.font)
        self.fontSize = QtWidgets.QSpinBox(Dialog)
        self.fontSize.setMinimum(6)
        self.fontSize.setObjectName("fontSize")
        self.horizontalLayout.addWidget(self.fontSize)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.qfmt, self.afmt)
        Dialog.setTabOrder(self.afmt, self.font)
        Dialog.setTabOrder(self.font, self.fontSize)
        Dialog.setTabOrder(self.fontSize, self.buttonBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_("Browser Appearance"))
        self.label.setText(_("Override front template:"))
        self.label_2.setText(_("Override back template:"))
        self.overrideFont.setText(_("Override font:"))
