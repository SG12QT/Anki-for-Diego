# -*- coding: utf-8 -*-
# pylint: disable=unsubscriptable-object,unused-import
from anki.lang import _
# Form implementation generated from reading ui file 'designer/browser.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 493)
        Dialog.setMinimumSize(QtCore.QSize(400, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/anki.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(12, 6, 12, 12)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 12)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.searchEdit = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy)
        self.searchEdit.setEditable(True)
        self.searchEdit.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.searchEdit.setObjectName("searchEdit")
        self.gridLayout.addWidget(self.searchEdit, 0, 1, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 0, 2, 1, 1)
        self.previewButton = QtWidgets.QPushButton(self.widget)
        self.previewButton.setCheckable(True)
        self.previewButton.setObjectName("previewButton")
        self.gridLayout.addWidget(self.previewButton, 0, 3, 1, 1)
        self.filter = QtWidgets.QPushButton(self.widget)
        self.filter.setObjectName("filter")
        self.gridLayout.addWidget(self.filter, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tableView = QtWidgets.QTableView(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(0, 150))
        self.tableView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.horizontalHeader().setMinimumSectionSize(20)
        self.tableView.horizontalHeader().setSortIndicatorShown(True)
        self.verticalLayout_2.addWidget(self.tableView)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 1, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setSpacing(0)
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.fieldsArea = QtWidgets.QWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fieldsArea.sizePolicy().hasHeightForWidth())
        self.fieldsArea.setSizePolicy(sizePolicy)
        self.fieldsArea.setMinimumSize(QtCore.QSize(50, 200))
        self.fieldsArea.setObjectName("fieldsArea")
        self.horizontalLayout2.addWidget(self.fieldsArea)
        self.verticalLayout.addLayout(self.horizontalLayout2)
        self.verticalLayout_3.addWidget(self.splitter)
        Dialog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 22))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuJump = QtWidgets.QMenu(self.menubar)
        self.menuJump.setObjectName("menuJump")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Cards = QtWidgets.QMenu(self.menubar)
        self.menu_Cards.setObjectName("menu_Cards")
        self.menuFlag = QtWidgets.QMenu(self.menu_Cards)
        self.menuFlag.setObjectName("menuFlag")
        self.menu_Notes = QtWidgets.QMenu(self.menubar)
        self.menu_Notes.setObjectName("menu_Notes")
        Dialog.setMenuBar(self.menubar)
        self.actionReschedule = QtWidgets.QAction(Dialog)
        self.actionReschedule.setObjectName("actionReschedule")
        self.actionSelectAll = QtWidgets.QAction(Dialog)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionUndo = QtWidgets.QAction(Dialog)
        self.actionUndo.setObjectName("actionUndo")
        self.actionInvertSelection = QtWidgets.QAction(Dialog)
        self.actionInvertSelection.setObjectName("actionInvertSelection")
        self.actionFind = QtWidgets.QAction(Dialog)
        self.actionFind.setObjectName("actionFind")
        self.actionNote = QtWidgets.QAction(Dialog)
        self.actionNote.setObjectName("actionNote")
        self.actionNextCard = QtWidgets.QAction(Dialog)
        self.actionNextCard.setObjectName("actionNextCard")
        self.actionPreviousCard = QtWidgets.QAction(Dialog)
        self.actionPreviousCard.setObjectName("actionPreviousCard")
        self.actionGuide = QtWidgets.QAction(Dialog)
        self.actionGuide.setObjectName("actionGuide")
        self.actionChangeModel = QtWidgets.QAction(Dialog)
        self.actionChangeModel.setObjectName("actionChangeModel")
        self.actionSelectNotes = QtWidgets.QAction(Dialog)
        self.actionSelectNotes.setObjectName("actionSelectNotes")
        self.actionFindReplace = QtWidgets.QAction(Dialog)
        self.actionFindReplace.setObjectName("actionFindReplace")
        self.actionCram = QtWidgets.QAction(Dialog)
        self.actionCram.setObjectName("actionCram")
        self.actionTags = QtWidgets.QAction(Dialog)
        self.actionTags.setObjectName("actionTags")
        self.actionCardList = QtWidgets.QAction(Dialog)
        self.actionCardList.setObjectName("actionCardList")
        self.actionFindDuplicates = QtWidgets.QAction(Dialog)
        self.actionFindDuplicates.setObjectName("actionFindDuplicates")
        self.actionReposition = QtWidgets.QAction(Dialog)
        self.actionReposition.setObjectName("actionReposition")
        self.actionFirstCard = QtWidgets.QAction(Dialog)
        self.actionFirstCard.setObjectName("actionFirstCard")
        self.actionLastCard = QtWidgets.QAction(Dialog)
        self.actionLastCard.setObjectName("actionLastCard")
        self.actionClose = QtWidgets.QAction(Dialog)
        self.actionClose.setObjectName("actionClose")
        self.action_Info = QtWidgets.QAction(Dialog)
        self.action_Info.setObjectName("action_Info")
        self.actionAdd_Tags = QtWidgets.QAction(Dialog)
        self.actionAdd_Tags.setObjectName("actionAdd_Tags")
        self.actionRemove_Tags = QtWidgets.QAction(Dialog)
        self.actionRemove_Tags.setObjectName("actionRemove_Tags")
        self.actionToggle_Suspend = QtWidgets.QAction(Dialog)
        self.actionToggle_Suspend.setObjectName("actionToggle_Suspend")
        self.actionDelete = QtWidgets.QAction(Dialog)
        self.actionDelete.setObjectName("actionDelete")
        self.actionAdd = QtWidgets.QAction(Dialog)
        self.actionAdd.setObjectName("actionAdd")
        self.actionChange_Deck = QtWidgets.QAction(Dialog)
        self.actionChange_Deck.setObjectName("actionChange_Deck")
        self.actionRed_Flag = QtWidgets.QAction(Dialog)
        self.actionRed_Flag.setCheckable(True)
        self.actionRed_Flag.setObjectName("actionRed_Flag")
        self.actionOrange_Flag = QtWidgets.QAction(Dialog)
        self.actionOrange_Flag.setCheckable(True)
        self.actionOrange_Flag.setObjectName("actionOrange_Flag")
        self.actionGreen_Flag = QtWidgets.QAction(Dialog)
        self.actionGreen_Flag.setCheckable(True)
        self.actionGreen_Flag.setObjectName("actionGreen_Flag")
        self.actionBlue_Flag = QtWidgets.QAction(Dialog)
        self.actionBlue_Flag.setCheckable(True)
        self.actionBlue_Flag.setObjectName("actionBlue_Flag")
        self.actionSidebar = QtWidgets.QAction(Dialog)
        self.actionSidebar.setObjectName("actionSidebar")
        self.actionClear_Unused_Tags = QtWidgets.QAction(Dialog)
        self.actionClear_Unused_Tags.setObjectName("actionClear_Unused_Tags")
        self.actionManage_Note_Types = QtWidgets.QAction(Dialog)
        self.actionManage_Note_Types.setObjectName("actionManage_Note_Types")
        self.actionToggle_Mark = QtWidgets.QAction(Dialog)
        self.actionToggle_Mark.setObjectName("actionToggle_Mark")
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelectAll)
        self.menuEdit.addAction(self.actionSelectNotes)
        self.menuEdit.addAction(self.actionInvertSelection)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionClose)
        self.menuJump.addAction(self.actionFind)
        self.menuJump.addAction(self.actionTags)
        self.menuJump.addAction(self.actionSidebar)
        self.menuJump.addAction(self.actionNote)
        self.menuJump.addAction(self.actionCardList)
        self.menuJump.addSeparator()
        self.menuJump.addAction(self.actionFirstCard)
        self.menuJump.addAction(self.actionPreviousCard)
        self.menuJump.addAction(self.actionNextCard)
        self.menuJump.addAction(self.actionLastCard)
        self.menu_Help.addAction(self.actionGuide)
        self.menuFlag.addAction(self.actionRed_Flag)
        self.menuFlag.addAction(self.actionOrange_Flag)
        self.menuFlag.addAction(self.actionGreen_Flag)
        self.menuFlag.addAction(self.actionBlue_Flag)
        self.menu_Cards.addAction(self.actionChange_Deck)
        self.menu_Cards.addSeparator()
        self.menu_Cards.addAction(self.actionReschedule)
        self.menu_Cards.addAction(self.actionReposition)
        self.menu_Cards.addSeparator()
        self.menu_Cards.addAction(self.actionToggle_Suspend)
        self.menu_Cards.addSeparator()
        self.menu_Cards.addAction(self.menuFlag.menuAction())
        self.menu_Cards.addSeparator()
        self.menu_Cards.addAction(self.action_Info)
        self.menu_Notes.addAction(self.actionAdd)
        self.menu_Notes.addSeparator()
        self.menu_Notes.addAction(self.actionAdd_Tags)
        self.menu_Notes.addAction(self.actionRemove_Tags)
        self.menu_Notes.addAction(self.actionClear_Unused_Tags)
        self.menu_Notes.addAction(self.actionToggle_Mark)
        self.menu_Notes.addSeparator()
        self.menu_Notes.addAction(self.actionChangeModel)
        self.menu_Notes.addSeparator()
        self.menu_Notes.addAction(self.actionFindDuplicates)
        self.menu_Notes.addAction(self.actionFindReplace)
        self.menu_Notes.addSeparator()
        self.menu_Notes.addAction(self.actionManage_Note_Types)
        self.menu_Notes.addSeparator()
        self.menu_Notes.addAction(self.actionDelete)
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menu_Notes.menuAction())
        self.menubar.addAction(self.menu_Cards.menuAction())
        self.menubar.addAction(self.menuJump.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(Dialog)
        self.actionSelectAll.triggered.connect(self.tableView.selectAll)
        self.actionClose.triggered.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.searchButton.setText(_("Search"))
        self.previewButton.setText(_("Preview"))
        self.previewButton.setShortcut(_("Ctrl+Shift+P"))
        self.filter.setText(_("Filter..."))
        self.menuEdit.setTitle(_("&Edit"))
        self.menuJump.setTitle(_("&Go"))
        self.menu_Help.setTitle(_("&Help"))
        self.menu_Cards.setTitle(_("&Cards"))
        self.menuFlag.setTitle(_("Flag"))
        self.menu_Notes.setTitle(_("&Notes"))
        self.actionReschedule.setText(_("&Reschedule..."))
        self.actionReschedule.setShortcut(_("Ctrl+Alt+R"))
        self.actionSelectAll.setText(_("Select &All"))
        self.actionSelectAll.setShortcut(_("Ctrl+Alt+A"))
        self.actionUndo.setText(_("&Undo"))
        self.actionUndo.setShortcut(_("Ctrl+Alt+Z"))
        self.actionInvertSelection.setText(_("&Invert Selection"))
        self.actionInvertSelection.setShortcut(_("Ctrl+Alt+S"))
        self.actionFind.setText(_("&Find"))
        self.actionFind.setShortcut(_("Ctrl+F"))
        self.actionNote.setText(_("N&ote"))
        self.actionNote.setShortcut(_("Ctrl+Shift+N"))
        self.actionNextCard.setText(_("&Next Card"))
        self.actionNextCard.setShortcut(_("Ctrl+N"))
        self.actionPreviousCard.setText(_("&Previous Card"))
        self.actionPreviousCard.setShortcut(_("Ctrl+P"))
        self.actionGuide.setText(_("&Guide"))
        self.actionGuide.setShortcut(_("F1"))
        self.actionChangeModel.setText(_("Change Note Type..."))
        self.actionChangeModel.setShortcut(_("Ctrl+Shift+M"))
        self.actionSelectNotes.setText(_("Select &Notes"))
        self.actionFindReplace.setText(_("Find and Re&place..."))
        self.actionFindReplace.setShortcut(_("Ctrl+Alt+F"))
        self.actionCram.setText(_("&Cram..."))
        self.actionTags.setText(_("Fil&ter"))
        self.actionTags.setShortcut(_("Ctrl+Shift+F"))
        self.actionCardList.setText(_("Card List"))
        self.actionCardList.setShortcut(_("Ctrl+Shift+L"))
        self.actionFindDuplicates.setText(_("Find &Duplicates..."))
        self.actionReposition.setText(_("Reposition..."))
        self.actionReposition.setShortcut(_("Ctrl+Shift+S"))
        self.actionFirstCard.setText(_("First Card"))
        self.actionFirstCard.setShortcut(_("Home"))
        self.actionLastCard.setText(_("Last Card"))
        self.actionLastCard.setShortcut(_("End"))
        self.actionClose.setText(_("Close"))
        self.actionClose.setShortcut(_("Ctrl+W"))
        self.action_Info.setText(_("&Info..."))
        self.action_Info.setShortcut(_("Ctrl+Shift+I"))
        self.actionAdd_Tags.setText(_("Add Tags..."))
        self.actionAdd_Tags.setShortcut(_("Ctrl+Shift+A"))
        self.actionRemove_Tags.setText(_("Remove Tags..."))
        self.actionRemove_Tags.setShortcut(_("Ctrl+Shift+D"))
        self.actionToggle_Suspend.setText(_("Toggle Suspend"))
        self.actionToggle_Suspend.setShortcut(_("Ctrl+J"))
        self.actionDelete.setText(_("Delete"))
        self.actionDelete.setShortcut(_("Ctrl+Del"))
        self.actionAdd.setText(_("Add Notes..."))
        self.actionAdd.setShortcut(_("Ctrl+E"))
        self.actionChange_Deck.setText(_("Change Deck..."))
        self.actionChange_Deck.setShortcut(_("Ctrl+D"))
        self.actionRed_Flag.setText(_("Red Flag"))
        self.actionRed_Flag.setShortcut(_("Ctrl+1"))
        self.actionOrange_Flag.setText(_("Orange Flag"))
        self.actionOrange_Flag.setShortcut(_("Ctrl+2"))
        self.actionGreen_Flag.setText(_("Green Flag"))
        self.actionGreen_Flag.setShortcut(_("Ctrl+3"))
        self.actionBlue_Flag.setText(_("Blue Flag"))
        self.actionBlue_Flag.setShortcut(_("Ctrl+4"))
        self.actionSidebar.setText(_("Sidebar"))
        self.actionSidebar.setShortcut(_("Ctrl+Shift+R"))
        self.actionClear_Unused_Tags.setText(_("Clear Unused Tags"))
        self.actionManage_Note_Types.setText(_("Manage Note Types..."))
        self.actionToggle_Mark.setText(_("Toggle Mark"))
        self.actionToggle_Mark.setShortcut(_("Ctrl+K"))
from . import icons_rc
