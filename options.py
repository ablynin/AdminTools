# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(289, 282)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_colors = QtWidgets.QWidget()
        self.tab_colors.setObjectName("tab_colors")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_colors)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab_colors)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_colors_latin = QtWidgets.QPushButton(self.tab_colors)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_colors_latin.sizePolicy().hasHeightForWidth())
        self.pushButton_colors_latin.setSizePolicy(sizePolicy)
        self.pushButton_colors_latin.setMinimumSize(QtCore.QSize(50, 20))
        self.pushButton_colors_latin.setText("")
        self.pushButton_colors_latin.setIconSize(QtCore.QSize(50, 20))
        self.pushButton_colors_latin.setCheckable(False)
        self.pushButton_colors_latin.setChecked(False)
        self.pushButton_colors_latin.setObjectName("pushButton_colors_latin")
        self.horizontalLayout.addWidget(self.pushButton_colors_latin)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab_colors)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_colors_cyrillic = QtWidgets.QPushButton(self.tab_colors)
        self.pushButton_colors_cyrillic.setMinimumSize(QtCore.QSize(50, 20))
        self.pushButton_colors_cyrillic.setText("")
        self.pushButton_colors_cyrillic.setIconSize(QtCore.QSize(50, 20))
        self.pushButton_colors_cyrillic.setCheckable(False)
        self.pushButton_colors_cyrillic.setChecked(False)
        self.pushButton_colors_cyrillic.setObjectName("pushButton_colors_cyrillic")
        self.horizontalLayout_2.addWidget(self.pushButton_colors_cyrillic)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab_colors)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_colors_numbers = QtWidgets.QPushButton(self.tab_colors)
        self.pushButton_colors_numbers.setMinimumSize(QtCore.QSize(50, 20))
        self.pushButton_colors_numbers.setText("")
        self.pushButton_colors_numbers.setIconSize(QtCore.QSize(50, 20))
        self.pushButton_colors_numbers.setCheckable(False)
        self.pushButton_colors_numbers.setChecked(False)
        self.pushButton_colors_numbers.setObjectName("pushButton_colors_numbers")
        self.horizontalLayout_3.addWidget(self.pushButton_colors_numbers)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab_colors)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButton_colors_spaces = QtWidgets.QPushButton(self.tab_colors)
        self.pushButton_colors_spaces.setMinimumSize(QtCore.QSize(50, 20))
        self.pushButton_colors_spaces.setText("")
        self.pushButton_colors_spaces.setIconSize(QtCore.QSize(50, 20))
        self.pushButton_colors_spaces.setCheckable(False)
        self.pushButton_colors_spaces.setChecked(False)
        self.pushButton_colors_spaces.setObjectName("pushButton_colors_spaces")
        self.horizontalLayout_4.addWidget(self.pushButton_colors_spaces)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.tab_colors)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.pushButton_colors_punctuation = QtWidgets.QPushButton(self.tab_colors)
        self.pushButton_colors_punctuation.setMinimumSize(QtCore.QSize(50, 20))
        self.pushButton_colors_punctuation.setText("")
        self.pushButton_colors_punctuation.setIconSize(QtCore.QSize(50, 20))
        self.pushButton_colors_punctuation.setCheckable(False)
        self.pushButton_colors_punctuation.setChecked(False)
        self.pushButton_colors_punctuation.setObjectName("pushButton_colors_punctuation")
        self.horizontalLayout_5.addWidget(self.pushButton_colors_punctuation)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.tab_colors)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.pushButton_colors_emails = QtWidgets.QPushButton(self.tab_colors)
        self.pushButton_colors_emails.setMinimumSize(QtCore.QSize(50, 20))
        self.pushButton_colors_emails.setText("")
        self.pushButton_colors_emails.setIconSize(QtCore.QSize(50, 20))
        self.pushButton_colors_emails.setCheckable(False)
        self.pushButton_colors_emails.setChecked(False)
        self.pushButton_colors_emails.setObjectName("pushButton_colors_emails")
        self.horizontalLayout_6.addWidget(self.pushButton_colors_emails)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.tab_colors)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.pushButton_colors_replace = QtWidgets.QPushButton(self.tab_colors)
        self.pushButton_colors_replace.setMinimumSize(QtCore.QSize(50, 20))
        self.pushButton_colors_replace.setText("")
        self.pushButton_colors_replace.setIconSize(QtCore.QSize(50, 20))
        self.pushButton_colors_replace.setCheckable(False)
        self.pushButton_colors_replace.setChecked(False)
        self.pushButton_colors_replace.setObjectName("pushButton_colors_replace")
        self.horizontalLayout_7.addWidget(self.pushButton_colors_replace)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tab_colors, "")
        self.tab_fonts = QtWidgets.QWidget()
        self.tab_fonts.setObjectName("tab_fonts")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_fonts)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_fonts_passgen = QtWidgets.QGroupBox(self.tab_fonts)
        self.groupBox_fonts_passgen.setObjectName("groupBox_fonts_passgen")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_fonts_passgen)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_fonts_passgen)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.fontComboBox_fonts_passgen = QtWidgets.QFontComboBox(self.groupBox_fonts_passgen)
        self.fontComboBox_fonts_passgen.setObjectName("fontComboBox_fonts_passgen")
        self.horizontalLayout_8.addWidget(self.fontComboBox_fonts_passgen)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_fonts_passgen)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.doubleSpinBox_fonts_passgen = QtWidgets.QDoubleSpinBox(self.groupBox_fonts_passgen)
        self.doubleSpinBox_fonts_passgen.setMinimum(7.0)
        self.doubleSpinBox_fonts_passgen.setMaximum(100.0)
        self.doubleSpinBox_fonts_passgen.setSingleStep(1.0)
        self.doubleSpinBox_fonts_passgen.setProperty("value", 8.0)
        self.doubleSpinBox_fonts_passgen.setObjectName("doubleSpinBox_fonts_passgen")
        self.horizontalLayout_9.addWidget(self.doubleSpinBox_fonts_passgen)
        self.checkBox_passgen_Bold = QtWidgets.QCheckBox(self.groupBox_fonts_passgen)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_passgen_Bold.setFont(font)
        self.checkBox_passgen_Bold.setObjectName("checkBox_passgen_Bold")
        self.horizontalLayout_9.addWidget(self.checkBox_passgen_Bold)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.pushButton_fonts_password = QtWidgets.QPushButton(self.groupBox_fonts_passgen)
        self.pushButton_fonts_password.setMinimumSize(QtCore.QSize(50, 20))
        self.pushButton_fonts_password.setText("")
        self.pushButton_fonts_password.setIconSize(QtCore.QSize(50, 20))
        self.pushButton_fonts_password.setObjectName("pushButton_fonts_password")
        self.horizontalLayout_9.addWidget(self.pushButton_fonts_password)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addWidget(self.groupBox_fonts_passgen)
        self.groupBox_fonts_email_checker = QtWidgets.QGroupBox(self.tab_fonts)
        self.groupBox_fonts_email_checker.setObjectName("groupBox_fonts_email_checker")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_fonts_email_checker)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.groupBox_fonts_email_checker)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.fontComboBox_fonts_email_checker = QtWidgets.QFontComboBox(self.groupBox_fonts_email_checker)
        self.fontComboBox_fonts_email_checker.setObjectName("fontComboBox_fonts_email_checker")
        self.horizontalLayout_11.addWidget(self.fontComboBox_fonts_email_checker)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.groupBox_fonts_email_checker)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.doubleSpinBox_fonts_email_checker = QtWidgets.QDoubleSpinBox(self.groupBox_fonts_email_checker)
        self.doubleSpinBox_fonts_email_checker.setMaximum(100.0)
        self.doubleSpinBox_fonts_email_checker.setSingleStep(0.25)
        self.doubleSpinBox_fonts_email_checker.setProperty("value", 8.25)
        self.doubleSpinBox_fonts_email_checker.setObjectName("doubleSpinBox_fonts_email_checker")
        self.horizontalLayout_10.addWidget(self.doubleSpinBox_fonts_email_checker)
        self.checkBox_email_checker_Bold = QtWidgets.QCheckBox(self.groupBox_fonts_email_checker)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_email_checker_Bold.setFont(font)
        self.checkBox_email_checker_Bold.setObjectName("checkBox_email_checker_Bold")
        self.horizontalLayout_10.addWidget(self.checkBox_email_checker_Bold)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.pushButton_fonts_default = QtWidgets.QPushButton(self.groupBox_fonts_email_checker)
        self.pushButton_fonts_default.setMinimumSize(QtCore.QSize(50, 20))
        self.pushButton_fonts_default.setText("")
        self.pushButton_fonts_default.setIconSize(QtCore.QSize(50, 20))
        self.pushButton_fonts_default.setObjectName("pushButton_fonts_default")
        self.horizontalLayout_10.addWidget(self.pushButton_fonts_default)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.verticalLayout_3.addWidget(self.groupBox_fonts_email_checker)
        self.tabWidget.addTab(self.tab_fonts, "")
        self.tab_tools = QtWidgets.QWidget()
        self.tab_tools.setObjectName("tab_tools")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_tools)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tools_treeView = QtWidgets.QTreeView(self.tab_tools)
        self.tools_treeView.setObjectName("tools_treeView")
        self.verticalLayout_6.addWidget(self.tools_treeView)
        self.tabWidget.addTab(self.tab_tools, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Options"))
        self.label.setText(_translate("Dialog", "Latin"))
        self.label_2.setText(_translate("Dialog", "Cyrillic"))
        self.label_3.setText(_translate("Dialog", "Numbers"))
        self.label_4.setText(_translate("Dialog", "Spaces"))
        self.label_5.setText(_translate("Dialog", "Punctuation"))
        self.label_6.setText(_translate("Dialog", "Valid emails"))
        self.label_7.setText(_translate("Dialog", "Replaced"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_colors), _translate("Dialog", "Colors"))
        self.groupBox_fonts_passgen.setTitle(_translate("Dialog", "Password generator"))
        self.label_8.setText(_translate("Dialog", "Font:"))
        self.label_9.setText(_translate("Dialog", "Size:"))
        self.checkBox_passgen_Bold.setText(_translate("Dialog", "B"))
        self.groupBox_fonts_email_checker.setTitle(_translate("Dialog", "E-mail checker"))
        self.label_11.setText(_translate("Dialog", "Font:"))
        self.label_10.setText(_translate("Dialog", "Size:"))
        self.checkBox_email_checker_Bold.setText(_translate("Dialog", "B"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fonts), _translate("Dialog", "Fonts"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tools), _translate("Dialog", "Tools"))

