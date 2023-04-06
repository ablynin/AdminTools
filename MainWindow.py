# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_passgen = QtWidgets.QWidget()
        self.tab_passgen.setObjectName("tab_passgen")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_passgen)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_passgen_password = QtWidgets.QLabel(self.tab_passgen)
        self.label_passgen_password.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_passgen_password.setObjectName("label_passgen_password")
        self.verticalLayout_2.addWidget(self.label_passgen_password)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.tab_passgen)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.spinBox_passgen = QtWidgets.QSpinBox(self.tab_passgen)
        self.spinBox_passgen.setMinimum(1)
        self.spinBox_passgen.setMaximum(999)
        self.spinBox_passgen.setProperty("value", 8)
        self.spinBox_passgen.setObjectName("spinBox_passgen")
        self.horizontalLayout_3.addWidget(self.spinBox_passgen)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(self.tab_passgen)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_passgen_cuc = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_passgen_cuc.setObjectName("checkBox_passgen_cuc")
        self.gridLayout.addWidget(self.checkBox_passgen_cuc, 2, 0, 1, 1)
        self.checkBox_passgen_spaces = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_passgen_spaces.setObjectName("checkBox_passgen_spaces")
        self.gridLayout.addWidget(self.checkBox_passgen_spaces, 2, 1, 1, 1)
        self.checkBox_passgen_llc = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_passgen_llc.setChecked(True)
        self.checkBox_passgen_llc.setObjectName("checkBox_passgen_llc")
        self.gridLayout.addWidget(self.checkBox_passgen_llc, 1, 0, 1, 1)
        self.checkBox_passgen_escape = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_passgen_escape.setObjectName("checkBox_passgen_escape")
        self.gridLayout.addWidget(self.checkBox_passgen_escape, 4, 1, 1, 1)
        self.checkBox_passgen_luc = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_passgen_luc.setChecked(True)
        self.checkBox_passgen_luc.setObjectName("checkBox_passgen_luc")
        self.gridLayout.addWidget(self.checkBox_passgen_luc, 0, 0, 1, 1)
        self.checkBox_passgen_clc = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_passgen_clc.setObjectName("checkBox_passgen_clc")
        self.gridLayout.addWidget(self.checkBox_passgen_clc, 3, 0, 1, 1)
        self.checkBox_passgen_pretty = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_passgen_pretty.setObjectName("checkBox_passgen_pretty")
        self.gridLayout.addWidget(self.checkBox_passgen_pretty, 4, 0, 1, 1)
        self.checkBox_passgen_csymbols = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_passgen_csymbols.setObjectName("checkBox_passgen_csymbols")
        self.gridLayout.addWidget(self.checkBox_passgen_csymbols, 3, 1, 1, 1)
        self.checkBox_passgen_numbers = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_passgen_numbers.setChecked(True)
        self.checkBox_passgen_numbers.setObjectName("checkBox_passgen_numbers")
        self.gridLayout.addWidget(self.checkBox_passgen_numbers, 0, 1, 1, 1)
        self.checkBox_passgen_symbols = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_passgen_symbols.setChecked(True)
        self.checkBox_passgen_symbols.setObjectName("checkBox_passgen_symbols")
        self.gridLayout.addWidget(self.checkBox_passgen_symbols, 1, 1, 1, 1)
        self.checkBox_passgen_unique = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_passgen_unique.setObjectName("checkBox_passgen_unique")
        self.gridLayout.addWidget(self.checkBox_passgen_unique, 6, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_passgen_generate = QtWidgets.QPushButton(self.tab_passgen)
        self.pushButton_passgen_generate.setObjectName("pushButton_passgen_generate")
        self.horizontalLayout_2.addWidget(self.pushButton_passgen_generate)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_passgen_clipboard = QtWidgets.QPushButton(self.tab_passgen)
        self.pushButton_passgen_clipboard.setObjectName("pushButton_passgen_clipboard")
        self.horizontalLayout_2.addWidget(self.pushButton_passgen_clipboard)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_passgen, "")
        self.tab_emailchecker = QtWidgets.QWidget()
        self.tab_emailchecker.setObjectName("tab_emailchecker")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_emailchecker)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.tab_emailchecker)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textEdit_emailchecker = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.textEdit_emailchecker.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_emailchecker.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_emailchecker.setObjectName("textEdit_emailchecker")
        self.horizontalLayout_4.addWidget(self.textEdit_emailchecker)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_emailchecker_hilight = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_emailchecker_hilight.setObjectName("groupBox_emailchecker_hilight")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_emailchecker_hilight)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_emailchecker_latin = QtWidgets.QCheckBox(self.groupBox_emailchecker_hilight)
        self.checkBox_emailchecker_latin.setObjectName("checkBox_emailchecker_latin")
        self.verticalLayout_5.addWidget(self.checkBox_emailchecker_latin)
        self.checkBox_emailchecker_cyrillic = QtWidgets.QCheckBox(self.groupBox_emailchecker_hilight)
        self.checkBox_emailchecker_cyrillic.setObjectName("checkBox_emailchecker_cyrillic")
        self.verticalLayout_5.addWidget(self.checkBox_emailchecker_cyrillic)
        self.checkBox_emailchecker_numbers = QtWidgets.QCheckBox(self.groupBox_emailchecker_hilight)
        self.checkBox_emailchecker_numbers.setObjectName("checkBox_emailchecker_numbers")
        self.verticalLayout_5.addWidget(self.checkBox_emailchecker_numbers)
        self.checkBox_emailchecker_spaces = QtWidgets.QCheckBox(self.groupBox_emailchecker_hilight)
        self.checkBox_emailchecker_spaces.setObjectName("checkBox_emailchecker_spaces")
        self.verticalLayout_5.addWidget(self.checkBox_emailchecker_spaces)
        self.checkBox_emailchecker_punctuation = QtWidgets.QCheckBox(self.groupBox_emailchecker_hilight)
        self.checkBox_emailchecker_punctuation.setObjectName("checkBox_emailchecker_punctuation")
        self.verticalLayout_5.addWidget(self.checkBox_emailchecker_punctuation)
        self.checkBox_emailchecker_emails = QtWidgets.QCheckBox(self.groupBox_emailchecker_hilight)
        self.checkBox_emailchecker_emails.setObjectName("checkBox_emailchecker_emails")
        self.verticalLayout_5.addWidget(self.checkBox_emailchecker_emails)
        self.verticalLayout_3.addWidget(self.groupBox_emailchecker_hilight)
        self.groupBox_emailchecker_edit = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_emailchecker_edit.setObjectName("groupBox_emailchecker_edit")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_emailchecker_edit)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox_emailchecker_empty = QtWidgets.QCheckBox(self.groupBox_emailchecker_edit)
        self.checkBox_emailchecker_empty.setObjectName("checkBox_emailchecker_empty")
        self.verticalLayout_6.addWidget(self.checkBox_emailchecker_empty)
        self.checkBox_emailchecker_replace = QtWidgets.QCheckBox(self.groupBox_emailchecker_edit)
        self.checkBox_emailchecker_replace.setObjectName("checkBox_emailchecker_replace")
        self.verticalLayout_6.addWidget(self.checkBox_emailchecker_replace)
        self.checkBox_emailchecker_noemails = QtWidgets.QCheckBox(self.groupBox_emailchecker_edit)
        self.checkBox_emailchecker_noemails.setObjectName("checkBox_emailchecker_noemails")
        self.verticalLayout_6.addWidget(self.checkBox_emailchecker_noemails)
        self.verticalLayout_3.addWidget(self.groupBox_emailchecker_edit)
        self.pushButton_emailchecker_clipboard = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_emailchecker_clipboard.setObjectName("pushButton_emailchecker_clipboard")
        self.verticalLayout_3.addWidget(self.pushButton_emailchecker_clipboard)
        self.verticalLayout_4.addWidget(self.splitter)
        self.tabWidget.addTab(self.tab_emailchecker, "")
        self.tab_other = QtWidgets.QWidget()
        self.tab_other.setObjectName("tab_other")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_other)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_other_macformat = QtWidgets.QGroupBox(self.tab_other)
        self.groupBox_other_macformat.setObjectName("groupBox_other_macformat")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_other_macformat)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_other_macformat = QtWidgets.QLineEdit(self.groupBox_other_macformat)
        self.lineEdit_other_macformat.setReadOnly(False)
        self.lineEdit_other_macformat.setObjectName("lineEdit_other_macformat")
        self.horizontalLayout_5.addWidget(self.lineEdit_other_macformat)
        self.checkBox_other_macformat_linux = QtWidgets.QCheckBox(self.groupBox_other_macformat)
        self.checkBox_other_macformat_linux.setObjectName("checkBox_other_macformat_linux")
        self.horizontalLayout_5.addWidget(self.checkBox_other_macformat_linux)
        self.checkBox_other_macformat_uppercase = QtWidgets.QCheckBox(self.groupBox_other_macformat)
        self.checkBox_other_macformat_uppercase.setObjectName("checkBox_other_macformat_uppercase")
        self.horizontalLayout_5.addWidget(self.checkBox_other_macformat_uppercase)
        self.pushButton_other_macformat_toclipboard = QtWidgets.QPushButton(self.groupBox_other_macformat)
        self.pushButton_other_macformat_toclipboard.setObjectName("pushButton_other_macformat_toclipboard")
        self.horizontalLayout_5.addWidget(self.pushButton_other_macformat_toclipboard)
        self.verticalLayout_7.addWidget(self.groupBox_other_macformat)
        self.groupBox_other_phonenumber = QtWidgets.QGroupBox(self.tab_other)
        self.groupBox_other_phonenumber.setObjectName("groupBox_other_phonenumber")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_other_phonenumber)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_other_phonenumber = QtWidgets.QLineEdit(self.groupBox_other_phonenumber)
        self.lineEdit_other_phonenumber.setObjectName("lineEdit_other_phonenumber")
        self.horizontalLayout_7.addWidget(self.lineEdit_other_phonenumber)
        self.checkBox_other_phonenumber = QtWidgets.QCheckBox(self.groupBox_other_phonenumber)
        self.checkBox_other_phonenumber.setObjectName("checkBox_other_phonenumber")
        self.horizontalLayout_7.addWidget(self.checkBox_other_phonenumber)
        self.pushButton_other_phonenumber_toclipboard = QtWidgets.QPushButton(self.groupBox_other_phonenumber)
        self.pushButton_other_phonenumber_toclipboard.setObjectName("pushButton_other_phonenumber_toclipboard")
        self.horizontalLayout_7.addWidget(self.pushButton_other_phonenumber_toclipboard)
        self.verticalLayout_7.addWidget(self.groupBox_other_phonenumber)
        self.groupBox_other_transliteration = QtWidgets.QGroupBox(self.tab_other)
        self.groupBox_other_transliteration.setObjectName("groupBox_other_transliteration")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_other_transliteration)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lineEdit_other_transliteration = QtWidgets.QLineEdit(self.groupBox_other_transliteration)
        self.lineEdit_other_transliteration.setObjectName("lineEdit_other_transliteration")
        self.verticalLayout_9.addWidget(self.lineEdit_other_transliteration)
        self.label_other_transliteration = QtWidgets.QLabel(self.groupBox_other_transliteration)
        self.label_other_transliteration.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_other_transliteration.setMouseTracking(True)
        self.label_other_transliteration.setTabletTracking(True)
        self.label_other_transliteration.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_other_transliteration.setObjectName("label_other_transliteration")
        self.verticalLayout_9.addWidget(self.label_other_transliteration)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.radioButton_other_transliteration_as_is = QtWidgets.QRadioButton(self.groupBox_other_transliteration)
        self.radioButton_other_transliteration_as_is.setChecked(True)
        self.radioButton_other_transliteration_as_is.setObjectName("radioButton_other_transliteration_as_is")
        self.verticalLayout_10.addWidget(self.radioButton_other_transliteration_as_is)
        self.radioButton_other_transliteration_upper = QtWidgets.QRadioButton(self.groupBox_other_transliteration)
        self.radioButton_other_transliteration_upper.setObjectName("radioButton_other_transliteration_upper")
        self.verticalLayout_10.addWidget(self.radioButton_other_transliteration_upper)
        self.radioButton_other_transliteration_lower = QtWidgets.QRadioButton(self.groupBox_other_transliteration)
        self.radioButton_other_transliteration_lower.setObjectName("radioButton_other_transliteration_lower")
        self.verticalLayout_10.addWidget(self.radioButton_other_transliteration_lower)
        self.horizontalLayout_8.addLayout(self.verticalLayout_10)
        self.pushButton_other_transliteration_toclipboard = QtWidgets.QPushButton(self.groupBox_other_transliteration)
        self.pushButton_other_transliteration_toclipboard.setObjectName("pushButton_other_transliteration_toclipboard")
        self.horizontalLayout_8.addWidget(self.pushButton_other_transliteration_toclipboard)
        self.verticalLayout_7.addWidget(self.groupBox_other_transliteration)
        self.groupBox_other_ipcalc = QtWidgets.QGroupBox(self.tab_other)
        self.groupBox_other_ipcalc.setObjectName("groupBox_other_ipcalc")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_other_ipcalc)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_other_ipcalc_ipaddr = QtWidgets.QLineEdit(self.groupBox_other_ipcalc)
        self.lineEdit_other_ipcalc_ipaddr.setInputMask("")
        self.lineEdit_other_ipcalc_ipaddr.setObjectName("lineEdit_other_ipcalc_ipaddr")
        self.horizontalLayout_6.addWidget(self.lineEdit_other_ipcalc_ipaddr)
        self.comboBox_other_ipcalc_mask = QtWidgets.QComboBox(self.groupBox_other_ipcalc)
        self.comboBox_other_ipcalc_mask.setObjectName("comboBox_other_ipcalc_mask")
        self.horizontalLayout_6.addWidget(self.comboBox_other_ipcalc_mask)
        self.pushButton_other_ipcalc_calculate = QtWidgets.QPushButton(self.groupBox_other_ipcalc)
        self.pushButton_other_ipcalc_calculate.setObjectName("pushButton_other_ipcalc_calculate")
        self.horizontalLayout_6.addWidget(self.pushButton_other_ipcalc_calculate)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_other_ipcalc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_other_ipcalc_network = QtWidgets.QLabel(self.groupBox_other_ipcalc)
        self.label_other_ipcalc_network.setFrameShape(QtWidgets.QFrame.Box)
        self.label_other_ipcalc_network.setText("")
        self.label_other_ipcalc_network.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_other_ipcalc_network.setObjectName("label_other_ipcalc_network")
        self.gridLayout_2.addWidget(self.label_other_ipcalc_network, 0, 1, 1, 1)
        self.label_other_ipcalc_hostcount = QtWidgets.QLabel(self.groupBox_other_ipcalc)
        self.label_other_ipcalc_hostcount.setFrameShape(QtWidgets.QFrame.Box)
        self.label_other_ipcalc_hostcount.setText("")
        self.label_other_ipcalc_hostcount.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_other_ipcalc_hostcount.setObjectName("label_other_ipcalc_hostcount")
        self.gridLayout_2.addWidget(self.label_other_ipcalc_hostcount, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_other_ipcalc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_other_ipcalc_broadcast = QtWidgets.QLabel(self.groupBox_other_ipcalc)
        self.label_other_ipcalc_broadcast.setFrameShape(QtWidgets.QFrame.Box)
        self.label_other_ipcalc_broadcast.setText("")
        self.label_other_ipcalc_broadcast.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_other_ipcalc_broadcast.setObjectName("label_other_ipcalc_broadcast")
        self.gridLayout_2.addWidget(self.label_other_ipcalc_broadcast, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_other_ipcalc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_other_ipcalc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_other_ipcalc_hostmin = QtWidgets.QLabel(self.groupBox_other_ipcalc)
        self.label_other_ipcalc_hostmin.setFrameShape(QtWidgets.QFrame.Box)
        self.label_other_ipcalc_hostmin.setText("")
        self.label_other_ipcalc_hostmin.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_other_ipcalc_hostmin.setObjectName("label_other_ipcalc_hostmin")
        self.gridLayout_2.addWidget(self.label_other_ipcalc_hostmin, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_other_ipcalc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_other_ipcalc_hostmax = QtWidgets.QLabel(self.groupBox_other_ipcalc)
        self.label_other_ipcalc_hostmax.setFrameShape(QtWidgets.QFrame.Box)
        self.label_other_ipcalc_hostmax.setText("")
        self.label_other_ipcalc_hostmax.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_other_ipcalc_hostmax.setObjectName("label_other_ipcalc_hostmax")
        self.gridLayout_2.addWidget(self.label_other_ipcalc_hostmax, 4, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_2)
        self.verticalLayout_7.addWidget(self.groupBox_other_ipcalc)
        self.tabWidget.addTab(self.tab_other, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuLanguage = QtWidgets.QMenu(self.menuOptions)
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setChecked(True)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionRussian = QtWidgets.QAction(MainWindow)
        self.actionRussian.setCheckable(True)
        self.actionRussian.setChecked(False)
        self.actionRussian.setObjectName("actionRussian")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setMenuRole(QtWidgets.QAction.AboutRole)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.action_Undo = QtWidgets.QAction(MainWindow)
        self.action_Undo.setObjectName("action_Undo")
        self.action_Redo = QtWidgets.QAction(MainWindow)
        self.action_Redo.setObjectName("action_Redo")
        self.action_Copy_all = QtWidgets.QAction(MainWindow)
        self.action_Copy_all.setObjectName("action_Copy_all")
        self.menuFile.addAction(self.actionQuit)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionRussian)
        self.menuOptions.addAction(self.menuLanguage.menuAction())
        self.menuOptions.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionAbout)
        self.menu_Edit.addAction(self.action_Undo)
        self.menu_Edit.addAction(self.action_Redo)
        self.menu_Edit.addAction(self.action_Copy_all)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.checkBox_passgen_luc)
        MainWindow.setTabOrder(self.checkBox_passgen_luc, self.checkBox_passgen_llc)
        MainWindow.setTabOrder(self.checkBox_passgen_llc, self.checkBox_passgen_cuc)
        MainWindow.setTabOrder(self.checkBox_passgen_cuc, self.checkBox_passgen_clc)
        MainWindow.setTabOrder(self.checkBox_passgen_clc, self.checkBox_passgen_pretty)
        MainWindow.setTabOrder(self.checkBox_passgen_pretty, self.checkBox_passgen_unique)
        MainWindow.setTabOrder(self.checkBox_passgen_unique, self.checkBox_passgen_numbers)
        MainWindow.setTabOrder(self.checkBox_passgen_numbers, self.checkBox_passgen_symbols)
        MainWindow.setTabOrder(self.checkBox_passgen_symbols, self.checkBox_passgen_spaces)
        MainWindow.setTabOrder(self.checkBox_passgen_spaces, self.checkBox_passgen_csymbols)
        MainWindow.setTabOrder(self.checkBox_passgen_csymbols, self.checkBox_passgen_escape)
        MainWindow.setTabOrder(self.checkBox_passgen_escape, self.pushButton_passgen_generate)
        MainWindow.setTabOrder(self.pushButton_passgen_generate, self.pushButton_passgen_clipboard)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AdminTools"))
        self.label_passgen_password.setText(_translate("MainWindow", "Password"))
        self.label.setText(_translate("MainWindow", "Length:"))
        self.groupBox.setTitle(_translate("MainWindow", "Characters:"))
        self.checkBox_passgen_cuc.setText(_translate("MainWindow", "Cyrillic upper case"))
        self.checkBox_passgen_spaces.setText(_translate("MainWindow", "Spaces"))
        self.checkBox_passgen_llc.setText(_translate("MainWindow", "Latin lower case"))
        self.checkBox_passgen_escape.setText(_translate("MainWindow", "Escape all symbols"))
        self.checkBox_passgen_luc.setText(_translate("MainWindow", "Latin upper case"))
        self.checkBox_passgen_clc.setText(_translate("MainWindow", "Cyrillic lower case"))
        self.checkBox_passgen_pretty.setText(_translate("MainWindow", "Pretty symbols"))
        self.checkBox_passgen_csymbols.setText(_translate("MainWindow", "Cyrillic symbols"))
        self.checkBox_passgen_numbers.setText(_translate("MainWindow", "Numbers"))
        self.checkBox_passgen_symbols.setText(_translate("MainWindow", "Symbols"))
        self.checkBox_passgen_unique.setText(_translate("MainWindow", "Unique string"))
        self.pushButton_passgen_generate.setText(_translate("MainWindow", "Generate"))
        self.pushButton_passgen_clipboard.setText(_translate("MainWindow", "To clipboard"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_passgen), _translate("MainWindow", "Password generator"))
        self.groupBox_emailchecker_hilight.setTitle(_translate("MainWindow", "Hilight:"))
        self.checkBox_emailchecker_latin.setText(_translate("MainWindow", "Latin"))
        self.checkBox_emailchecker_cyrillic.setText(_translate("MainWindow", "Cyrillic"))
        self.checkBox_emailchecker_numbers.setText(_translate("MainWindow", "Numbers"))
        self.checkBox_emailchecker_spaces.setText(_translate("MainWindow", "Spaces"))
        self.checkBox_emailchecker_punctuation.setText(_translate("MainWindow", "Punctuation"))
        self.checkBox_emailchecker_emails.setText(_translate("MainWindow", "Valid e-mails"))
        self.groupBox_emailchecker_edit.setTitle(_translate("MainWindow", "Edit:"))
        self.checkBox_emailchecker_empty.setText(_translate("MainWindow", "Remove empty lines"))
        self.checkBox_emailchecker_replace.setText(_translate("MainWindow", "Replace cyrillic"))
        self.checkBox_emailchecker_noemails.setText(_translate("MainWindow", "Remove non e-mail"))
        self.pushButton_emailchecker_clipboard.setText(_translate("MainWindow", "To clipboard"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_emailchecker), _translate("MainWindow", "E-mail checker"))
        self.groupBox_other_macformat.setTitle(_translate("MainWindow", "MAC format:"))
        self.lineEdit_other_macformat.setInputMask(_translate("MainWindow", "HH:HH:HH:HH:HH:HH;_"))
        self.checkBox_other_macformat_linux.setText(_translate("MainWindow", "Linux"))
        self.checkBox_other_macformat_uppercase.setText(_translate("MainWindow", "Upper case"))
        self.pushButton_other_macformat_toclipboard.setText(_translate("MainWindow", "To clipboard"))
        self.groupBox_other_phonenumber.setTitle(_translate("MainWindow", "Phone number normalizer:"))
        self.checkBox_other_phonenumber.setText(_translate("MainWindow", "Escape by *"))
        self.pushButton_other_phonenumber_toclipboard.setText(_translate("MainWindow", "To clipboard"))
        self.groupBox_other_transliteration.setTitle(_translate("MainWindow", "Transliteration"))
        self.label_other_transliteration.setText(_translate("MainWindow", "Result"))
        self.radioButton_other_transliteration_as_is.setText(_translate("MainWindow", "As is"))
        self.radioButton_other_transliteration_upper.setText(_translate("MainWindow", "UPPER CASE"))
        self.radioButton_other_transliteration_lower.setText(_translate("MainWindow", "lower case"))
        self.pushButton_other_transliteration_toclipboard.setText(_translate("MainWindow", "To clipboard"))
        self.groupBox_other_ipcalc.setTitle(_translate("MainWindow", "IP calculator:"))
        self.pushButton_other_ipcalc_calculate.setText(_translate("MainWindow", "Calculate"))
        self.label_2.setText(_translate("MainWindow", "Network:"))
        self.label_6.setText(_translate("MainWindow", "Host count:"))
        self.label_4.setText(_translate("MainWindow", "Broadcast:"))
        self.label_8.setText(_translate("MainWindow", "Host min:"))
        self.label_10.setText(_translate("MainWindow", "Host max:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_other), _translate("MainWindow", "Other"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.actionRussian.setText(_translate("MainWindow", "Russian"))
        self.actionAbout.setText(_translate("MainWindow", "About..."))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.action_Undo.setText(_translate("MainWindow", "&Undo"))
        self.action_Redo.setText(_translate("MainWindow", "&Redo"))
        self.action_Copy_all.setText(_translate("MainWindow", "&Copy all"))

