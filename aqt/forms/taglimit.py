# -*- coding: utf-8 -*-
# pylint: disable=unsubscriptable-object,unused-import
from anki.lang import _
# Form implementation generated from reading ui file 'designer/taglimit.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 394)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.activeCheck = QtWidgets.QCheckBox(Dialog)
        self.activeCheck.setObjectName("activeCheck")
        self.verticalLayout.addWidget(self.activeCheck)
        self.activeList = QtWidgets.QListWidget(Dialog)
        self.activeList.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.activeList.sizePolicy().hasHeightForWidth())
        self.activeList.setSizePolicy(sizePolicy)
        self.activeList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.activeList.setObjectName("activeList")
        self.verticalLayout.addWidget(self.activeList)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.inactiveList = QtWidgets.QListWidget(Dialog)
        self.inactiveList.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.inactiveList.sizePolicy().hasHeightForWidth())
        self.inactiveList.setSizePolicy(sizePolicy)
        self.inactiveList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.inactiveList.setObjectName("inactiveList")
        self.verticalLayout.addWidget(self.inactiveList)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.activeCheck.toggled['bool'].connect(self.activeList.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_("Selective Study"))
        self.activeCheck.setText(_("Require one or more of these tags:"))
        self.label.setText(_("Select tags to exclude:"))

