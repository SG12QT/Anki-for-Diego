# -*- coding: utf-8 -*-
# pylint: disable=unsubscriptable-object,unused-import
from anki.lang import _
# Form implementation generated from reading ui file 'designer/stats.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(607, 556)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.web = AnkiWebView(Dialog)
        self.web.setProperty("url", QtCore.QUrl("about:blank"))
        self.web.setObjectName("web")
        self.verticalLayout.addWidget(self.web)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groups = QtWidgets.QRadioButton(self.groupBox_2)
        self.groups.setChecked(True)
        self.groups.setObjectName("groups")
        self.horizontalLayout_2.addWidget(self.groups)
        self.all = QtWidgets.QRadioButton(self.groupBox_2)
        self.all.setObjectName("all")
        self.horizontalLayout_2.addWidget(self.all)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.month = QtWidgets.QRadioButton(self.groupBox)
        self.month.setChecked(True)
        self.month.setObjectName("month")
        self.horizontalLayout.addWidget(self.month)
        self.year = QtWidgets.QRadioButton(self.groupBox)
        self.year.setObjectName("year")
        self.horizontalLayout.addWidget(self.year)
        self.life = QtWidgets.QRadioButton(self.groupBox)
        self.life.setObjectName("life")
        self.horizontalLayout.addWidget(self.life)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_("Statistics"))
        self.groups.setText(_("deck"))
        self.all.setText(_("collection"))
        self.month.setText(_("1 month"))
        self.year.setText(_("1 year"))
        self.life.setText(_("deck life"))

from aqt.webview import AnkiWebView