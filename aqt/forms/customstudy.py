# -*- coding: utf-8 -*-
# pylint: disable=unsubscriptable-object,unused-import
from anki.lang import _
# Form implementation generated from reading ui file 'designer/customstudy.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 380)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.radio4 = QtWidgets.QRadioButton(Dialog)
        self.radio4.setObjectName("radio4")
        self.gridLayout.addWidget(self.radio4, 3, 0, 1, 1)
        self.radio3 = QtWidgets.QRadioButton(Dialog)
        self.radio3.setObjectName("radio3")
        self.gridLayout.addWidget(self.radio3, 2, 0, 1, 1)
        self.radio1 = QtWidgets.QRadioButton(Dialog)
        self.radio1.setObjectName("radio1")
        self.gridLayout.addWidget(self.radio1, 0, 0, 1, 1)
        self.radio2 = QtWidgets.QRadioButton(Dialog)
        self.radio2.setObjectName("radio2")
        self.gridLayout.addWidget(self.radio2, 1, 0, 1, 1)
        self.radio6 = QtWidgets.QRadioButton(Dialog)
        self.radio6.setObjectName("radio6")
        self.gridLayout.addWidget(self.radio6, 5, 0, 1, 1)
        self.radio5 = QtWidgets.QRadioButton(Dialog)
        self.radio5.setObjectName("radio5")
        self.gridLayout.addWidget(self.radio5, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLabel(self.groupBox)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.preSpin = QtWidgets.QLabel(self.groupBox)
        self.preSpin.setObjectName("preSpin")
        self.horizontalLayout.addWidget(self.preSpin)
        self.spin = QtWidgets.QSpinBox(self.groupBox)
        self.spin.setObjectName("spin")
        self.horizontalLayout.addWidget(self.spin)
        self.postSpin = QtWidgets.QLabel(self.groupBox)
        self.postSpin.setObjectName("postSpin")
        self.horizontalLayout.addWidget(self.postSpin)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.cardType = QtWidgets.QListWidget(self.groupBox)
        self.cardType.setObjectName("cardType")
        item = QtWidgets.QListWidgetItem()
        self.cardType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cardType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cardType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.cardType.addItem(item)
        self.verticalLayout_2.addWidget(self.cardType)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.cardType.setCurrentRow(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.radio1, self.radio2)
        Dialog.setTabOrder(self.radio2, self.radio3)
        Dialog.setTabOrder(self.radio3, self.radio4)
        Dialog.setTabOrder(self.radio4, self.radio6)
        Dialog.setTabOrder(self.radio6, self.spin)
        Dialog.setTabOrder(self.spin, self.buttonBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_("Custom Study"))
        self.radio4.setText(_("Review ahead"))
        self.radio3.setText(_("Review forgotten cards"))
        self.radio1.setText(_("Increase today\'s new card limit"))
        self.radio2.setText(_("Increase today\'s review card limit"))
        self.radio6.setText(_("Study by card state or tag"))
        self.radio5.setText(_("Preview new cards"))
        self.title.setText(_("..."))
        self.preSpin.setText(_("..."))
        self.postSpin.setText(_("..."))
        __sortingEnabled = self.cardType.isSortingEnabled()
        self.cardType.setSortingEnabled(False)
        item = self.cardType.item(0)
        item.setText(_("New cards only"))
        item = self.cardType.item(1)
        item.setText(_("Due cards only"))
        item = self.cardType.item(2)
        item.setText(_("All review cards in random order"))
        item = self.cardType.item(3)
        item.setText(_("All cards in random order (don\'t reschedule)"))
        self.cardType.setSortingEnabled(__sortingEnabled)
