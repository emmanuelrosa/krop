# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Jun  6 20:27:17 2020
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(949, 736)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabBasic = QtGui.QWidget()
        self.tabBasic.setObjectName(_fromUtf8("tabBasic"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabBasic)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupSaveTo = QtGui.QGroupBox(self.tabBasic)
        self.groupSaveTo.setObjectName(_fromUtf8("groupSaveTo"))
        self.gridLayout = QtGui.QGridLayout(self.groupSaveTo)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.editFile = QtGui.QLineEdit(self.groupSaveTo)
        self.editFile.setObjectName(_fromUtf8("editFile"))
        self.gridLayout.addWidget(self.editFile, 0, 0, 1, 1)
        self.buttonFileSelect = QtGui.QToolButton(self.groupSaveTo)
        self.buttonFileSelect.setText(_fromUtf8(""))
        self.buttonFileSelect.setAutoRaise(True)
        self.buttonFileSelect.setObjectName(_fromUtf8("buttonFileSelect"))
        self.gridLayout.addWidget(self.buttonFileSelect, 0, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupSaveTo)
        self.groupPDFOperations = QtGui.QGroupBox(self.tabBasic)
        self.groupPDFOperations.setFlat(False)
        self.groupPDFOperations.setObjectName(_fromUtf8("groupPDFOperations"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupPDFOperations)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.comboRotation = QtGui.QComboBox(self.groupPDFOperations)
        self.comboRotation.setObjectName(_fromUtf8("comboRotation"))
        self.comboRotation.addItem(_fromUtf8(""))
        self.comboRotation.addItem(_fromUtf8(""))
        self.comboRotation.addItem(_fromUtf8(""))
        self.comboRotation.addItem(_fromUtf8(""))
        self.verticalLayout_8.addWidget(self.comboRotation)
        self.checkGhostscript = QtGui.QCheckBox(self.groupPDFOperations)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkGhostscript.sizePolicy().hasHeightForWidth())
        self.checkGhostscript.setSizePolicy(sizePolicy)
        self.checkGhostscript.setChecked(True)
        self.checkGhostscript.setObjectName(_fromUtf8("checkGhostscript"))
        self.verticalLayout_8.addWidget(self.checkGhostscript)
        self.verticalLayout_4.addWidget(self.groupPDFOperations)
        self.groupWhichPages = QtGui.QGroupBox(self.tabBasic)
        self.groupWhichPages.setObjectName(_fromUtf8("groupWhichPages"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupWhichPages)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.editWhichPages = QtGui.QLineEdit(self.groupWhichPages)
        self.editWhichPages.setObjectName(_fromUtf8("editWhichPages"))
        self.verticalLayout.addWidget(self.editWhichPages)
        self.checkIncludePagesWithoutSelections = QtGui.QCheckBox(self.groupWhichPages)
        self.checkIncludePagesWithoutSelections.setChecked(True)
        self.checkIncludePagesWithoutSelections.setObjectName(_fromUtf8("checkIncludePagesWithoutSelections"))
        self.verticalLayout.addWidget(self.checkIncludePagesWithoutSelections)
        self.verticalLayout_4.addWidget(self.groupWhichPages)
        self.groupSelectionMode = QtGui.QGroupBox(self.tabBasic)
        self.groupSelectionMode.setFlat(False)
        self.groupSelectionMode.setObjectName(_fromUtf8("groupSelectionMode"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupSelectionMode)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.radioSelAll = QtGui.QRadioButton(self.groupSelectionMode)
        self.radioSelAll.setChecked(True)
        self.radioSelAll.setObjectName(_fromUtf8("radioSelAll"))
        self.gridLayout_2.addWidget(self.radioSelAll, 0, 0, 1, 2)
        self.radioSelEvenOdd = QtGui.QRadioButton(self.groupSelectionMode)
        self.radioSelEvenOdd.setObjectName(_fromUtf8("radioSelEvenOdd"))
        self.gridLayout_2.addWidget(self.radioSelEvenOdd, 1, 0, 1, 2)
        self.radioSelIndividual = QtGui.QRadioButton(self.groupSelectionMode)
        self.radioSelIndividual.setObjectName(_fromUtf8("radioSelIndividual"))
        self.gridLayout_2.addWidget(self.radioSelIndividual, 2, 0, 1, 2)
        self.labelSelExceptions = QtGui.QLabel(self.groupSelectionMode)
        self.labelSelExceptions.setObjectName(_fromUtf8("labelSelExceptions"))
        self.gridLayout_2.addWidget(self.labelSelExceptions, 3, 0, 1, 1)
        self.editSelExceptions = QtGui.QLineEdit(self.groupSelectionMode)
        self.editSelExceptions.setObjectName(_fromUtf8("editSelExceptions"))
        self.gridLayout_2.addWidget(self.editSelExceptions, 3, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupSelectionMode)
        spacerItem = QtGui.QSpacerItem(20, 484, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.tabWidget.addTab(self.tabBasic, _fromUtf8(""))
        self.tabAdvanced = QtGui.QWidget()
        self.tabAdvanced.setObjectName(_fromUtf8("tabAdvanced"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabAdvanced)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupCurrentSel = QtGui.QGroupBox(self.tabAdvanced)
        self.groupCurrentSel.setEnabled(False)
        self.groupCurrentSel.setObjectName(_fromUtf8("groupCurrentSel"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupCurrentSel)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.comboSelAspectRatioType = QtGui.QComboBox(self.groupCurrentSel)
        self.comboSelAspectRatioType.setEditable(False)
        self.comboSelAspectRatioType.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.comboSelAspectRatioType.setObjectName(_fromUtf8("comboSelAspectRatioType"))
        self.gridLayout_4.addWidget(self.comboSelAspectRatioType, 0, 0, 1, 2)
        self.editSelAspectRatio = QtGui.QLineEdit(self.groupCurrentSel)
        self.editSelAspectRatio.setObjectName(_fromUtf8("editSelAspectRatio"))
        self.gridLayout_4.addWidget(self.editSelAspectRatio, 1, 1, 1, 1)
        self.labelSelAspectRatio = QtGui.QLabel(self.groupCurrentSel)
        self.labelSelAspectRatio.setObjectName(_fromUtf8("labelSelAspectRatio"))
        self.gridLayout_4.addWidget(self.labelSelAspectRatio, 1, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupCurrentSel)
        self.groupTrimMargins = QtGui.QGroupBox(self.tabAdvanced)
        self.groupTrimMargins.setObjectName(_fromUtf8("groupTrimMargins"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupTrimMargins)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.checkTrimUseAllPages = QtGui.QCheckBox(self.groupTrimMargins)
        self.checkTrimUseAllPages.setChecked(True)
        self.checkTrimUseAllPages.setObjectName(_fromUtf8("checkTrimUseAllPages"))
        self.gridLayout_3.addWidget(self.checkTrimUseAllPages, 0, 0, 1, 2)
        self.labelPadding = QtGui.QLabel(self.groupTrimMargins)
        self.labelPadding.setObjectName(_fromUtf8("labelPadding"))
        self.gridLayout_3.addWidget(self.labelPadding, 1, 0, 1, 1)
        self.editPadding = QtGui.QLineEdit(self.groupTrimMargins)
        self.editPadding.setText(_fromUtf8(""))
        self.editPadding.setObjectName(_fromUtf8("editPadding"))
        self.gridLayout_3.addWidget(self.editPadding, 1, 1, 1, 1)
        self.labelAllowedChanges = QtGui.QLabel(self.groupTrimMargins)
        self.labelAllowedChanges.setEnabled(True)
        self.labelAllowedChanges.setObjectName(_fromUtf8("labelAllowedChanges"))
        self.gridLayout_3.addWidget(self.labelAllowedChanges, 2, 0, 1, 1)
        self.editAllowedChanges = QtGui.QLineEdit(self.groupTrimMargins)
        self.editAllowedChanges.setEnabled(True)
        self.editAllowedChanges.setObjectName(_fromUtf8("editAllowedChanges"))
        self.gridLayout_3.addWidget(self.editAllowedChanges, 2, 1, 1, 1)
        self.labelSensitivity = QtGui.QLabel(self.groupTrimMargins)
        self.labelSensitivity.setEnabled(True)
        self.labelSensitivity.setObjectName(_fromUtf8("labelSensitivity"))
        self.gridLayout_3.addWidget(self.labelSensitivity, 3, 0, 1, 1)
        self.editSensitivity = QtGui.QLineEdit(self.groupTrimMargins)
        self.editSensitivity.setEnabled(True)
        self.editSensitivity.setObjectName(_fromUtf8("editSensitivity"))
        self.gridLayout_3.addWidget(self.editSensitivity, 3, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.groupTrimMargins)
        self.groupDistribute = QtGui.QGroupBox(self.tabAdvanced)
        self.groupDistribute.setObjectName(_fromUtf8("groupDistribute"))
        self.formLayout = QtGui.QFormLayout(self.groupDistribute)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.comboDistributeDevice = QtGui.QComboBox(self.groupDistribute)
        self.comboDistributeDevice.setEditable(False)
        self.comboDistributeDevice.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.comboDistributeDevice.setObjectName(_fromUtf8("comboDistributeDevice"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.comboDistributeDevice)
        self.labelDistributeAspectRatio = QtGui.QLabel(self.groupDistribute)
        self.labelDistributeAspectRatio.setObjectName(_fromUtf8("labelDistributeAspectRatio"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelDistributeAspectRatio)
        self.editDistributeAspectRatio = QtGui.QLineEdit(self.groupDistribute)
        self.editDistributeAspectRatio.setObjectName(_fromUtf8("editDistributeAspectRatio"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.editDistributeAspectRatio)
        self.labelDistributeHelp = QtGui.QLabel(self.groupDistribute)
        self.labelDistributeHelp.setWordWrap(True)
        self.labelDistributeHelp.setObjectName(_fromUtf8("labelDistributeHelp"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.labelDistributeHelp)
        self.verticalLayout_5.addWidget(self.groupDistribute)
        spacerItem1 = QtGui.QSpacerItem(20, 339, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.tabWidget.addTab(self.tabAdvanced, _fromUtf8(""))
        self.tabHelp = QtGui.QWidget()
        self.tabHelp.setObjectName(_fromUtf8("tabHelp"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabHelp)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelHelp = QtGui.QLabel(self.tabHelp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHelp.sizePolicy().hasHeightForWidth())
        self.labelHelp.setSizePolicy(sizePolicy)
        self.labelHelp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelHelp.setBaseSize(QtCore.QSize(0, 0))
        self.labelHelp.setTextFormat(QtCore.Qt.AutoText)
        self.labelHelp.setWordWrap(True)
        self.labelHelp.setOpenExternalLinks(True)
        self.labelHelp.setObjectName(_fromUtf8("labelHelp"))
        self.verticalLayout_3.addWidget(self.labelHelp)
        spacerItem2 = QtGui.QSpacerItem(20, 524, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.frameHelpCopyright = QtGui.QFrame(self.tabHelp)
        self.frameHelpCopyright.setFrameShape(QtGui.QFrame.HLine)
        self.frameHelpCopyright.setObjectName(_fromUtf8("frameHelpCopyright"))
        self.verticalLayout_3.addWidget(self.frameHelpCopyright)
        self.labelHelpCopyright = QtGui.QLabel(self.tabHelp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHelpCopyright.sizePolicy().hasHeightForWidth())
        self.labelHelpCopyright.setSizePolicy(sizePolicy)
        self.labelHelpCopyright.setTextFormat(QtCore.Qt.AutoText)
        self.labelHelpCopyright.setWordWrap(True)
        self.labelHelpCopyright.setOpenExternalLinks(True)
        self.labelHelpCopyright.setObjectName(_fromUtf8("labelHelpCopyright"))
        self.verticalLayout_3.addWidget(self.labelHelpCopyright)
        self.tabWidget.addTab(self.tabHelp, _fromUtf8(""))
        self.frame = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setMargin(1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.documentView = QtGui.QGraphicsView(self.frame)
        self.documentView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.documentView.setFrameShadow(QtGui.QFrame.Sunken)
        self.documentView.setObjectName(_fromUtf8("documentView"))
        self.verticalLayout_2.addWidget(self.documentView)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.buttonFirst = QtGui.QPushButton(self.frame_2)
        self.buttonFirst.setMinimumSize(QtCore.QSize(24, 24))
        self.buttonFirst.setMaximumSize(QtCore.QSize(24, 24))
        self.buttonFirst.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonFirst.setText(_fromUtf8(""))
        self.buttonFirst.setFlat(True)
        self.buttonFirst.setObjectName(_fromUtf8("buttonFirst"))
        self.horizontalLayout_2.addWidget(self.buttonFirst)
        self.buttonPrevious = QtGui.QPushButton(self.frame_2)
        self.buttonPrevious.setMinimumSize(QtCore.QSize(24, 24))
        self.buttonPrevious.setMaximumSize(QtCore.QSize(24, 24))
        self.buttonPrevious.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonPrevious.setText(_fromUtf8(""))
        self.buttonPrevious.setFlat(True)
        self.buttonPrevious.setObjectName(_fromUtf8("buttonPrevious"))
        self.horizontalLayout_2.addWidget(self.buttonPrevious)
        self.editCurrentPage = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editCurrentPage.sizePolicy().hasHeightForWidth())
        self.editCurrentPage.setSizePolicy(sizePolicy)
        self.editCurrentPage.setMinimumSize(QtCore.QSize(40, 23))
        self.editCurrentPage.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editCurrentPage.setInputMask(_fromUtf8(""))
        self.editCurrentPage.setAlignment(QtCore.Qt.AlignCenter)
        self.editCurrentPage.setObjectName(_fromUtf8("editCurrentPage"))
        self.horizontalLayout_2.addWidget(self.editCurrentPage)
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.editMaxPage = QtGui.QLineEdit(self.frame_2)
        self.editMaxPage.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editMaxPage.sizePolicy().hasHeightForWidth())
        self.editMaxPage.setSizePolicy(sizePolicy)
        self.editMaxPage.setMinimumSize(QtCore.QSize(40, 23))
        self.editMaxPage.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editMaxPage.setAutoFillBackground(False)
        self.editMaxPage.setInputMask(_fromUtf8(""))
        self.editMaxPage.setFrame(True)
        self.editMaxPage.setAlignment(QtCore.Qt.AlignCenter)
        self.editMaxPage.setReadOnly(True)
        self.editMaxPage.setObjectName(_fromUtf8("editMaxPage"))
        self.horizontalLayout_2.addWidget(self.editMaxPage)
        self.buttonNext = QtGui.QPushButton(self.frame_2)
        self.buttonNext.setMinimumSize(QtCore.QSize(24, 24))
        self.buttonNext.setMaximumSize(QtCore.QSize(24, 24))
        self.buttonNext.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonNext.setText(_fromUtf8(""))
        self.buttonNext.setFlat(True)
        self.buttonNext.setObjectName(_fromUtf8("buttonNext"))
        self.horizontalLayout_2.addWidget(self.buttonNext)
        self.buttonLast = QtGui.QPushButton(self.frame_2)
        self.buttonLast.setMinimumSize(QtCore.QSize(24, 24))
        self.buttonLast.setMaximumSize(QtCore.QSize(24, 24))
        self.buttonLast.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonLast.setText(_fromUtf8(""))
        self.buttonLast.setFlat(True)
        self.buttonLast.setObjectName(_fromUtf8("buttonLast"))
        self.horizontalLayout_2.addWidget(self.buttonLast)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_7.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.toolBar.setMovable(True)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionZoomIn = QtGui.QAction(MainWindow)
        self.actionZoomIn.setObjectName(_fromUtf8("actionZoomIn"))
        self.actionZoomOut = QtGui.QAction(MainWindow)
        self.actionZoomOut.setObjectName(_fromUtf8("actionZoomOut"))
        self.actionPreviousPage = QtGui.QAction(MainWindow)
        self.actionPreviousPage.setObjectName(_fromUtf8("actionPreviousPage"))
        self.actionNextPage = QtGui.QAction(MainWindow)
        self.actionNextPage.setObjectName(_fromUtf8("actionNextPage"))
        self.actionOpenFile = QtGui.QAction(MainWindow)
        self.actionOpenFile.setObjectName(_fromUtf8("actionOpenFile"))
        self.actionFitInView = QtGui.QAction(MainWindow)
        self.actionFitInView.setCheckable(True)
        self.actionFitInView.setObjectName(_fromUtf8("actionFitInView"))
        self.actionKrop = QtGui.QAction(MainWindow)
        self.actionKrop.setEnabled(False)
        self.actionKrop.setObjectName(_fromUtf8("actionKrop"))
        self.actionDeleteSelection = QtGui.QAction(MainWindow)
        self.actionDeleteSelection.setObjectName(_fromUtf8("actionDeleteSelection"))
        self.actionFirstPage = QtGui.QAction(MainWindow)
        self.actionFirstPage.setObjectName(_fromUtf8("actionFirstPage"))
        self.actionLastPage = QtGui.QAction(MainWindow)
        self.actionLastPage.setObjectName(_fromUtf8("actionLastPage"))
        self.actionTrimMargins = QtGui.QAction(MainWindow)
        self.actionTrimMargins.setObjectName(_fromUtf8("actionTrimMargins"))
        self.actionSelectFile = QtGui.QAction(MainWindow)
        self.actionSelectFile.setObjectName(_fromUtf8("actionSelectFile"))
        self.actionTrimMarginsAll = QtGui.QAction(MainWindow)
        self.actionTrimMarginsAll.setEnabled(False)
        self.actionTrimMarginsAll.setObjectName(_fromUtf8("actionTrimMarginsAll"))
        self.actionNewSelection = QtGui.QAction(MainWindow)
        self.actionNewSelection.setObjectName(_fromUtf8("actionNewSelection"))
        self.actionNewSelectionGrid = QtGui.QAction(MainWindow)
        self.actionNewSelectionGrid.setObjectName(_fromUtf8("actionNewSelectionGrid"))
        self.toolBar.addAction(self.actionOpenFile)
        self.toolBar.addAction(self.actionKrop)
        self.toolBar.addAction(self.actionZoomIn)
        self.toolBar.addAction(self.actionZoomOut)
        self.toolBar.addAction(self.actionFitInView)
        self.toolBar.addAction(self.actionPreviousPage)
        self.toolBar.addAction(self.actionNextPage)
        self.toolBar.addAction(self.actionTrimMarginsAll)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonPrevious, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionPreviousPage.trigger)
        QtCore.QObject.connect(self.buttonNext, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionNextPage.trigger)
        QtCore.QObject.connect(self.buttonFirst, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionFirstPage.trigger)
        QtCore.QObject.connect(self.buttonLast, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionLastPage.trigger)
        QtCore.QObject.connect(self.buttonFileSelect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionSelectFile.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "krop: A tool to crop your PDFs", None))
        self.groupSaveTo.setTitle(_translate("MainWindow", "Save cropped PDF to", None))
        self.editFile.setToolTip(_translate("MainWindow", "<p>This is where the cropped PDF will be saved after you choose <i>Krop!</i> in the menu.</p>", None))
        self.buttonFileSelect.setToolTip(_translate("MainWindow", "<p>This is where the cropped PDF will be saved after you choose <i>Krop!</i> in the menu.</p>", None))
        self.groupPDFOperations.setTitle(_translate("MainWindow", "Extra operations on the final PDF", None))
        self.comboRotation.setItemText(0, _translate("MainWindow", "don\'t rotate", None))
        self.comboRotation.setItemText(1, _translate("MainWindow", "rotate left (90° counterclockwise)", None))
        self.comboRotation.setItemText(2, _translate("MainWindow", "rotate right (90° clockwise)", None))
        self.comboRotation.setItemText(3, _translate("MainWindow", "upside down", None))
        self.checkGhostscript.setToolTip(_translate("MainWindow", "<p>In order to use this option, Ghostscript must be installed and available as <i>gs</i>. Whether this option actually improves the file size depends on the PDF file.</p>", None))
        self.checkGhostscript.setText(_translate("MainWindow", "Use Ghostscript to optimize", None))
        self.groupWhichPages.setTitle(_translate("MainWindow", "Which pages to include", None))
        self.editWhichPages.setToolTip(_translate("MainWindow", "<p>Which pages to include in the output file.</p><p><i>Eg:</i> 1-5 for the first 5 pages\n"
"<br><i>Eg:</i> 2- for all but the first page\n"
"<br><i>Eg:</i> 1,4-5,7- to omit pages 2,3,6</p>", None))
        self.checkIncludePagesWithoutSelections.setToolTip(_translate("MainWindow", "<p>If checked, pages without selections will be included in the output unchanged. Otherwise, such pages will be removed from the output.</p>", None))
        self.checkIncludePagesWithoutSelections.setText(_translate("MainWindow", "Include pages without selections", None))
        self.groupSelectionMode.setToolTip(_translate("MainWindow", "<p>Should all pages be cropped based on the same selections? Maybe you want to treat even and odd pages differently? For full control you can crop each page using individual selections.</p>", None))
        self.groupSelectionMode.setTitle(_translate("MainWindow", "Selections apply to", None))
        self.radioSelAll.setText(_translate("MainWindow", "all pages", None))
        self.radioSelEvenOdd.setText(_translate("MainWindow", "even/odd pages", None))
        self.radioSelIndividual.setText(_translate("MainWindow", "individual page", None))
        self.labelSelExceptions.setToolTip(_translate("MainWindow", "<p>List pages which require individual selections.</p>", None))
        self.labelSelExceptions.setText(_translate("MainWindow", "Exceptions:", None))
        self.editSelExceptions.setToolTip(_translate("MainWindow", "<p>List pages which require individual selections.</p>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBasic), _translate("MainWindow", "Basic", None))
        self.groupCurrentSel.setToolTip(_translate("MainWindow", "<p>Click a selection to make it the current one. You can then set a fixed aspect ratio for this selection here.</p>", None))
        self.groupCurrentSel.setTitle(_translate("MainWindow", "Current Selection", None))
        self.comboSelAspectRatioType.setToolTip(_translate("MainWindow", "<p>If your favorite aspect ratio is missing here, you can add it by editing the config file.</p>", None))
        self.labelSelAspectRatio.setText(_translate("MainWindow", "Aspect ratio:", None))
        self.groupTrimMargins.setToolTip(_translate("MainWindow", "<p>Right-click a selection to automatically trim it.</p>", None))
        self.groupTrimMargins.setTitle(_translate("MainWindow", "Settings for trimming margins", None))
        self.checkTrimUseAllPages.setToolTip(_translate("MainWindow", "<p>If selected, all pages will be inspected (which can be very slow!) in order to determine the margins for auto trimming. Otherwise, only the current page is inspected.</p>", None))
        self.checkTrimUseAllPages.setText(_translate("MainWindow", "Use all pages (slow!)", None))
        self.labelPadding.setToolTip(_translate("MainWindow", "<p>How much padding to use when trimming.</p><p><i>Eg:</i> 2 or 5,2 or 5,2,5,5 (interpreted as in CSS)</p>", None))
        self.labelPadding.setText(_translate("MainWindow", "Padding:", None))
        self.editPadding.setToolTip(_translate("MainWindow", "<p>How much padding to use when trimming.</p><p><i>Eg:</i> 2 or 5,2 or 5,2,5,5 (interpreted as in CSS)</p>", None))
        self.labelAllowedChanges.setText(_translate("MainWindow", "Allowed changes:", None))
        self.labelSensitivity.setText(_translate("MainWindow", "Color sensitivity:", None))
        self.groupDistribute.setToolTip(_translate("MainWindow", "<p>Use this option if you want to break up each selection into pieces that exactly fit a certain aspect ratio. This is useful for displaying files on devices that don\'t support scrolling well.</p>", None))
        self.groupDistribute.setTitle(_translate("MainWindow", "Fit screen of device", None))
        self.labelDistributeAspectRatio.setText(_translate("MainWindow", "Aspect ratio:", None))
        self.labelDistributeHelp.setText(_translate("MainWindow", "<p><i>Eg:</i> 600:730 (ratio of width to height)</p>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAdvanced), _translate("MainWindow", "Advanced", None))
        self.labelHelp.setText(_translate("MainWindow", "<h3>Getting started</h3>\n"
"<p>Using your mouse, create one or more selections on the pdf document. These are the regions that will be included into the cropped file.</p>\n"
"<p>When you are done, click <i>Krop!</i> in the menu to create a cropped version of your document.</p>\n"
"<h3>Hints</h3>\n"
"<p>Right-click the page to create a selection for the full page (or a grid of selections).</p>\n"
"<p>Right-click a selection to delete it. Or simply press the Delete key.</p>\n"
"<p>You can choose to create individual selections for each page.</p>\n"
"<p>You can automatically trim the margins of your selections.</p>\n"
"<p>Examples and more information can be found at: <a href=\'http://arminstraub.com/software/krop\'>arminstraub.com</a></p>\n"
"", None))
        self.labelHelpCopyright.setToolTip(_translate("MainWindow", "<p>This program is free software and available to you in the hope that it will be useful; but without any warranty. It is distributed under the terms of the GNU General Public License (GPLv3+). See the accompanying files for more information.</p>", None))
        self.labelHelpCopyright.setText(_translate("MainWindow", "<p>Copyright (C) 2010-2020 Armin Straub\n"
"<br><a href=\'http://arminstraub.com\'>http://arminstraub.com</a></p>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHelp), _translate("MainWindow", "Help", None))
        self.label.setText(_translate("MainWindow", "of", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionZoomIn.setText(_translate("MainWindow", "Zoom In", None))
        self.actionZoomIn.setShortcut(_translate("MainWindow", "Ctrl+=", None))
        self.actionZoomOut.setText(_translate("MainWindow", "Zoom Out", None))
        self.actionZoomOut.setShortcut(_translate("MainWindow", "Ctrl+-", None))
        self.actionPreviousPage.setText(_translate("MainWindow", "Previous Page", None))
        self.actionPreviousPage.setShortcut(_translate("MainWindow", "PgUp", None))
        self.actionNextPage.setText(_translate("MainWindow", "Next Page", None))
        self.actionNextPage.setShortcut(_translate("MainWindow", "PgDown", None))
        self.actionOpenFile.setText(_translate("MainWindow", "Open", None))
        self.actionOpenFile.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionFitInView.setText(_translate("MainWindow", "Fit In View", None))
        self.actionKrop.setText(_translate("MainWindow", "Krop!", None))
        self.actionDeleteSelection.setText(_translate("MainWindow", "Delete Selection", None))
        self.actionDeleteSelection.setShortcut(_translate("MainWindow", "Del", None))
        self.actionFirstPage.setText(_translate("MainWindow", "First Page", None))
        self.actionFirstPage.setShortcut(_translate("MainWindow", "Home", None))
        self.actionLastPage.setText(_translate("MainWindow", "Last Page", None))
        self.actionLastPage.setShortcut(_translate("MainWindow", "End", None))
        self.actionTrimMargins.setText(_translate("MainWindow", "Trim Margins", None))
        self.actionSelectFile.setText(_translate("MainWindow", "Select File", None))
        self.actionTrimMarginsAll.setText(_translate("MainWindow", "Trim Margins", None))
        self.actionTrimMarginsAll.setToolTip(_translate("MainWindow", "Trim Margins", None))
        self.actionTrimMarginsAll.setShortcut(_translate("MainWindow", "Ctrl+T", None))
        self.actionNewSelection.setText(_translate("MainWindow", "New Selection", None))
        self.actionNewSelection.setToolTip(_translate("MainWindow", "New Selection", None))
        self.actionNewSelection.setShortcut(_translate("MainWindow", "Ins", None))
        self.actionNewSelectionGrid.setText(_translate("MainWindow", "New Selection Grid...", None))
        self.actionNewSelectionGrid.setToolTip(_translate("MainWindow", "New Selection Grid...", None))
        self.actionNewSelectionGrid.setShortcut(_translate("MainWindow", "Shift+Ins", None))

