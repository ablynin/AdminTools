#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QApplication, QMessageBox, QActionGroup, QTranslator, QObject, QTextCursor, QPalette, QColor, QPixmap, QKeySequence, QMenu, QEvent, QRegExp, QRegExpValidator


import MainWindow
from pass_gen import create_pass
import emailchecker
from options import Ui_Dialog

import os
import configparser

from history import History

from ipcalc import Ipaddress

import phonenormalizer
import toolstreemodel


_translate = QtCore.QCoreApplication.translate
appname = os.path.splitext(os.path.basename(sys.argv[0]))[0]
TabWidgetSectionName = 'tab_'
CurrentTabKeyName = 'CurrentTab'
TabPositionKeyName = 'TabPosition'
EnabledKeyName = 'Enabled'
MenuLaguageSectionName = 'MenuLaguage'
ColorsSectionName = 'Colors'
FontsSectionName = 'Fonts'
# ToolsTreeSectionName = 'Tools'

srcdir = 'source'
lang_dir = r'%s\languages' % srcdir
icon = r'%s\Spanner.ico' % srcdir
inidir = srcdir
langs = ['', 'ru_RU.qm']
# treemodel = toolstreemodel.TreeModel()


class AdminToolsWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icon))
        self.pushButton_passgen_generate.clicked.connect(self.passgen_generate)
        self.pushButton_passgen_clipboard.clicked.connect(self.toclipboard)
        self.pushButton_emailchecker_clipboard.clicked.connect(self.toclipboard)
        self.pushButton_other_transliteration_toclipboard.clicked.connect(self.toclipboard)
        self.textEdit_emailchecker.textChanged.connect(self.emailchecker_transform)
        # self.installEventFilter(self)
        self.textEdit_emailchecker.installEventFilter(self)
        self.textEdit_emailchecker.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.textEdit_emailchecker.customContextMenuRequested.connect(self.contextMenuEvent)
        for cb in self.groupBox_emailchecker_hilight.findChildren(QtWidgets.QCheckBox):
            cb.clicked.connect(self.emailchecker_transform)
        for cb in self.groupBox_emailchecker_edit.findChildren(QtWidgets.QCheckBox):
            cb.clicked.connect(self.emailchecker_transform)
        self.actionQuit.triggered.connect(QtWidgets.qApp.quit)
        self.actionQuit.setShortcut(QKeySequence(_translate('Application', 'Ctrl+Q')))
        self.actionAbout.triggered.connect(self.showAbout)
        self.menuLanguageGroup = QActionGroup(self)
        for act in self.menuLanguage.actions():
            self.menuLanguageGroup.addAction(act)
            act.triggered.connect(self.retranslate)
        self.menuLanguageGroup.actions()[0].setChecked(True)
        self.actionSettings.triggered.connect(self.showOptions)
        self.action_Undo.triggered.connect(self.undo)

        undo_keysequence = QKeySequence(_translate('Application', 'Ctrl+Z'))
        undo_shortcut = QtWidgets.QShortcut(undo_keysequence, self)
        undo_shortcut.activated.connect(self.undo)

        self.action_Undo.setShortcut(undo_keysequence)
        self.action_Redo.triggered.connect(self.redo)

        redo_keysequence = QKeySequence(_translate('Application', 'Ctrl+Shift+Z'))
        redo_shortcut = QtWidgets.QShortcut(redo_keysequence, self)
        redo_shortcut.activated.connect(self.redo)
        self.action_Redo.setShortcut(redo_keysequence)

        copyall_keysequence = QKeySequence(_translate('Application', 'Ctrl+Shift+C'))
        copyall_shortcut = QtWidgets.QShortcut(copyall_keysequence, self)
        copyall_shortcut.activated.connect(self.toclipboard)

        self.action_Copy_all.setShortcut(copyall_keysequence)
        self.action_Copy_all.triggered.connect(self.toclipboard)

        self.menubar.hovered.connect(self.main_menu_modifier)

        self.lineEdit_other_macformat.textChanged.connect(self.set_mac_format)
        self.checkBox_other_macformat_linux.clicked.connect(self.set_mac_format)
        self.checkBox_other_macformat_uppercase.clicked.connect(self.set_mac_format)
        self.pushButton_other_macformat_toclipboard.clicked.connect(self.toclipboard)
        self.pushButton_other_ipcalc_calculate.clicked.connect(self.calculate_network)

        self.lineEdit_other_phonenumber.textChanged.connect(self._normalize_number)
        self.pushButton_other_phonenumber_toclipboard.clicked.connect(self.toclipboard)
        self.checkBox_other_phonenumber.clicked.connect(self._normalize_number)

        self._ip = Ipaddress()

        cbis = ['%s (%s)' % (self._ip._masks.index(x), x) for x in self._ip._masks][::-1]
        self.comboBox_other_ipcalc_mask.addItems(cbis)

        # self.groupBox_other_macformat.show()
        # self.lineEdit_other_ipcalc_ipaddr.setText('192.168.0.5')

        self.tmp_colors = {}
        self.init_about()
        self._history = History()
        # self.tools = []
        self.tool_names = {}
        # self._set_tool_names()
        self.tabWidget.tabBar().tabMoved.connect(self._tool_tab_moved)
        self.tool_tabs = [self.tabWidget.widget(i) for i in range(self.tabWidget.count())]
        # for t in self.tool_tabs:
        #     print(t.isVisible())
        # for i in range(self.tabWidget.count()):
        #     self.tool_tabs[self.tabWidget.widget(i)] = i
        self.toolsModel = toolstreemodel.TreeModel()
        # print("Main window inited")

    def _set_tool_names(self):
        # print('Setting tool names: %s' % self.sender())
        # self.retranslate()
        self.tool_names = {self.tab_passgen: _translate('Application', 'Password generator'),
                           self.tab_emailchecker: _translate('Application', 'E-mail checker'),
                           self.tab_other: _translate('Application', 'Other')}

    def _tool_tab_moved(self, frm, to):
        self.tool_tabs.insert(to, self.tool_tabs.pop(frm))

    def _normalize_number(self):
        flag = ''
        if self.checkBox_other_phonenumber.isChecked():
            flag = phonenormalizer.flags['escape']

        pos = self.lineEdit_other_phonenumber.cursorPosition()
        self.lineEdit_other_phonenumber.blockSignals(True)
        self.lineEdit_other_phonenumber.setText(phonenormalizer.normalize(self.lineEdit_other_phonenumber.text(),
                                                                          flag))
        self.lineEdit_other_phonenumber.blockSignals(False)
        self.lineEdit_other_phonenumber.setCursorPosition(pos)

    def _validate_ip(self, ip):
        octets = ip.split('.')
        if len(octets) != 4:
            return False
        for octet in octets:
            oct = 0
            try:
                oct = int(octet)
            except ValueError:
                return False

            if oct > 255:
                return False

            if (octet.startswith('0') and oct > 0) or (octet == '0' * len(octet) and len(octet) > 1):
                return False
        return True

    def _map_combobox_mask_index(self):
        return abs(self.comboBox_other_ipcalc_mask.currentIndex() - 32)

    def calculate_network(self):
        try:
            ip = self.lineEdit_other_ipcalc_ipaddr.text() + '/%s' % self._map_combobox_mask_index()
            if not self._validate_ip(ip.split('/')[0]):
                raise ValueError
            self._ip.ip = ip
            self.label_other_ipcalc_network.setText(self._ip.hosts['network'])
            self.label_other_ipcalc_broadcast.setText(self._ip.hosts['broadcast'])
            self.label_other_ipcalc_hostcount.setText(str(self._ip.hosts['hostcount']))
            self.label_other_ipcalc_hostmin.setText(self._ip.hosts['hostmin'])
            self.label_other_ipcalc_hostmax.setText(self._ip.hosts['hostmax'])
        except Exception:
            QMessageBox.critical(self, appname, _translate('Application', 'Invalid IP-address.'))

    def set_mac_format(self):
        pos = self.lineEdit_other_macformat.cursorPosition()
        if self.checkBox_other_macformat_linux.isChecked():
            self.lineEdit_other_macformat.setInputMask('HH:HH:HH:HH:HH:HH;_')
        else:
            self.lineEdit_other_macformat.setInputMask('HH-HH-HH-HH-HH-HH;_')
        self.lineEdit_other_macformat.blockSignals(True)
        if self.checkBox_other_macformat_uppercase.isChecked():
            self.lineEdit_other_macformat.setText(self.lineEdit_other_macformat.text().upper())
        else:
            self.lineEdit_other_macformat.setText(self.lineEdit_other_macformat.text().lower())
        self.lineEdit_other_macformat.blockSignals(False)
        self.lineEdit_other_macformat.setCursorPosition(pos)
        self.lineEdit_other_macformat.setFocus()

    def main_menu_modifier(self):
        if self.tabWidget.currentIndex() == 0:
            self.action_Undo.setEnabled(False)
            self.action_Redo.setEnabled(False)
            self.action_Copy_all.setEnabled(True)
            # self.action_Copy_all.triggered.connect(self.pushButton_passgen_clipboard.clicked)
        elif self.tabWidget.currentIndex() == 1:
            # print('Got it')
            self.action_Undo.setEnabled(self._history.undo_available)
            self.action_Redo.setEnabled(self._history.redo_available)
            self.action_Copy_all.setEnabled(bool(self.textEdit_emailchecker.toPlainText()))

    def contextMenuEvent(self, point):
        menu = self.textEdit_emailchecker.createStandardContextMenu()
        #ContextMenu Undo
        menu.actions()[0].setEnabled(self._history.undo_available)
        menu.actions()[0].triggered.connect(self.undo)
        # ContextMenu Redo
        menu.actions()[1].setEnabled(self._history.redo_available)
        menu.actions()[1].triggered.connect(self.redo)
        menu.exec_(self.textEdit_emailchecker.mapToGlobal(point))

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.ShortcutOverride and event.modifiers() == 	QtCore.Qt.ControlModifier:
            if event.key() == QtCore.Qt.Key_Z:
                self.undo()
                return True
        if event.type() == QtCore.QEvent.ShortcutOverride and event.modifiers() == (QtCore.Qt.ControlModifier |
                                                                                    QtCore.Qt.ShiftModifier):
            if event.key() == QtCore.Qt.Key_Z:
                self.redo()
                return True
            elif event.key() == QtCore.Qt.Key_C:
                self.toclipboard()
                return True
        return super(AdminToolsWindow, self).eventFilter(source, event)

    def create_snapshot(self):
        snap = {}
        for o in self.tab_emailchecker.findChildren(QtWidgets.QCheckBox):
            snap[o.objectName()] = {}
            snap[o.objectName()]['setChecked'] = o.isChecked()

        ten = self.textEdit_emailchecker.objectName()
        snap[ten] = {}
        snap[ten]['setHtml'] = self.textEdit_emailchecker.toHtml()
        # print(self.textEdit_emailchecker.textCursor().position())
        snap[ten]['setPosition'] = self.textEdit_emailchecker.textCursor().position()
        # print(snap)
        return snap

    def load_snapshot(self, snapshot):
        if not snapshot:
            return

        for name in snapshot.keys():
            o_type = name.split('_')[0]

            if o_type == 'checkBox':
                obj = self.tab_emailchecker.findChild(QtWidgets.QCheckBox, name)
                for func, val in snapshot[name].items():
                    if func == 'setChecked':
                        obj.blockSignals(True)
                        obj.setChecked(val)
                        obj.blockSignals(False)
            if o_type == 'textEdit':
                obj = self.tab_emailchecker.findChild(QtWidgets.QTextEdit, name)
                for func, val in snapshot[name].items():
                    if func == 'setHtml':
                        obj.blockSignals(True)
                        obj.setHtml(val)
                        obj.blockSignals(False)
                    if func == 'setPosition':
                        obj.blockSignals(True)
                        tk = self.textEdit_emailchecker.textCursor()
                        tk.setPosition(val)
                        obj.setTextCursor(tk)
                        obj.blockSignals(False)

    def toHistory(self, obj):
        if type(obj) != QtWidgets.QCheckBox and type(obj) != QtWidgets.QTextEdit:
            return

        self._history.add(self.create_snapshot())

    def undo(self):
        snap = self._history.undo()
        # print(snap)
        # print(self._history.history_pos)
        self.load_snapshot(snap)
        # self.tabWidget.tabBar().moveTab(0,2)

    def redo(self):
        snap = self._history.redo()
        # print(snap)
        # print(self._history.history_pos)
        self.load_snapshot(snap)

    def init_about(self):
        self.about = QtWidgets.QDialog()
        self.about.setObjectName('AboutWindow')
        self.about.setWindowTitle(_translate('Application', 'About'))
        self.about.setWindowIcon(self.windowIcon())
        self.about.verticalLayout = QtWidgets.QVBoxLayout(self.about)
        self.about.verticalLayout.setObjectName('verticalLayout')
        self.about.label = QtWidgets.QLabel(self.about)
        self.about.label.setObjectName('label')
        self.about.label.setAlignment(QtCore.Qt.AlignCenter)
        self.about.label.setText(_translate('Application', '''Admin tools program.

Version: 1.0

Written by Alexander Ablynin for you.

You can do with this program anything you want.

Program is written on Python 3.6 and QT 5.'''))
        self.about.verticalLayout.addWidget(self.about.label)

    def showAbout(self):
        self.init_about()
        self.about.exec()

    def create_toolsmodel(self):
        # print('Creating model')
        self.toolsModel = toolstreemodel.TreeModel()

        for i in range(len(self.tool_tabs)):
            if i == self.tool_tabs.index(self.tab_other):
                ti, index = self.toolsModel.addItem(data=self.tool_names[self.tab_other], obj=self.tab_other)
                for gb in self.tab_other.findChildren(QtWidgets.QGroupBox):
                    tigb, index = self.toolsModel.addItem(gb.title()[:-1], ti, gb)
                    state = 0
                    if gb.isEnabled():
                        state = 2
                    self.toolsModel.setData(index, state, QtCore.Qt.CheckStateRole)
            else:
                ti, index = self.toolsModel.addItem(data=self.tool_names[self.tool_tabs[i]], obj=self.tool_tabs[i])
                state = 0
                if self.tool_tabs[i].isEnabled():
                    state = 2
                self.toolsModel.setData(index, state, QtCore.Qt.CheckStateRole)

    def set_tools_from_toolsmodel(self):
        objects = []
        for index in self.toolsModel.indexes:
            obj = self.toolsModel.data(index, QtCore.Qt.UserRole)
            obj.setEnabled(bool(self.toolsModel.data(index, QtCore.Qt.CheckStateRole)))
            objects.append(obj)

        to_remove = []
        for o in objects:
            if isinstance(o, QtWidgets.QGroupBox):
                o.setVisible(o.isEnabled())
            elif isinstance(o, QtWidgets.QWidget):
                if o.isEnabled():
                    if self.tabWidget.indexOf(o) < 0:
                        self.tabWidget.insertTab(self.tool_tabs.index(o), o, self.tool_names[o])
                        self.tabWidget.setCurrentIndex(self.tool_tabs.index(o))
                else:
                    to_remove.append(self.tool_tabs.index(o))

        to_remove.sort(reverse=True)
        for i in to_remove:
            self.tabWidget.removeTab(i)

    def init_options(self):
        self.optionsWindow = Ui_Dialog()
        self.options = QtWidgets.QDialog()
        self.optionsWindow.setupUi(self.options)
        self.optionsWindow.doubleSpinBox_fonts_emailchecker.setValue(emailchecker.font_size)
        self.optionsWindow.fontComboBox_fonts_emailchecker.setCurrentFont(QtGui.QFont(emailchecker.font_family))
        self.optionsWindow.doubleSpinBox_fonts_passgen.setValue(self.label_passgen_password.font().pointSize())
        self.optionsWindow.fontComboBox_fonts_passgen.setCurrentFont(QtGui.QFont(self.label_passgen_password.font().family()))
        for btn in self.optionsWindow.tabWidget.findChildren(QtWidgets.QPushButton):
            btn.clicked.connect(self.color_dialog)
            self.set_rectangle_colored(btn,
                                       emailchecker.colors_def[emailchecker.flags_def[btn.objectName().split('_')[-1]]])
        self.optionsWindow.checkBox_passgen_Bold.setChecked(self.label_passgen_password.font().bold())
        self.optionsWindow.checkBox_emailchecker_Bold.setChecked(emailchecker.bold)
        self.optionsWindow.ttwColumn = 0
        self.create_toolsmodel()
        self.optionsWindow.tools_treeView.setModel(self.toolsModel)
        self.optionsWindow.tools_treeView.setHeaderHidden(True)
        self.optionsWindow.tools_treeView.expandAll()
        # self._restore_tools(self.optionsWindow.tools_treeWidget.invisibleRootItem(), self.tools)
        # print('Options inited')
        # weight = [f.Thin, f.ExtraLight, f.Light, f.Normal, f.Medium, f.DemiBold, f.Bold, f.ExtraBold, f.Black]

    def showOptions(self):
        self.init_options()
        res = self.options.exec()
        if res:
            # print('showOptions if res', self.tmp_colors.items())
            for obj, color in self.tmp_colors.items():
                # print(obj)
                # print(obj.objectName())
                flag = emailchecker.flags_def[obj.objectName().split('_')[-1]]
                emailchecker.colors_def[flag] = color.name()
            # print('for obj, color in self.tmp_colors.items():')
            emailchecker.font_size = self.optionsWindow.doubleSpinBox_fonts_emailchecker.value()
            emailchecker.font_family = self.optionsWindow.fontComboBox_fonts_emailchecker.currentFont().family()
            font = QtGui.QFont(QtGui.QFont(self.optionsWindow.fontComboBox_fonts_passgen.currentFont().family(),
                                                            self.optionsWindow.doubleSpinBox_fonts_passgen.value()))
            font.setBold(self.optionsWindow.checkBox_passgen_Bold.isChecked())
            self.label_passgen_password.setFont(font)
            self.label_passgen_password.setStyleSheet('QLabel { color: %s; }' %
                                                      emailchecker.colors_def[emailchecker.flags_def['password']])
            emailchecker.bold = self.optionsWindow.checkBox_emailchecker_Bold.isChecked()
            self.textEdit_emailchecker.textChanged.emit()
            # self.tools = self._dump_tools(self.optionsWindow.tools_treeWidget.invisibleRootItem())
            # self.tools = self.toolsModel.dump_tree()
            # self.tools_set()
            self.set_tools_from_toolsmodel()

        self.tmp_colors = {}

    def set_rectangle_colored(self, obj, color):
        if type(color) != QColor:
            color = QColor(color)
        width = obj.width()
        height = obj.height()
        k = 1
        pixmap = QPixmap(width/k, height/k)
        painter = QtGui.QPainter(pixmap)
        painter.fillRect(0, 0, width/k, height/k, color)
        lighter = color.lighter()
        painter.setPen(lighter)
        # light frame
        painter.drawPolyline(QtCore.QPoint(0, height/k - 1), QtCore.QPoint(0, 0), QtCore.QPoint(width/k - 1, 0))
        painter.setPen(color.darker())
        # dark frame
        painter.drawPolyline(QtCore.QPoint(1, height/k - 1), QtCore.QPoint(width/k - 1, height/k - 1),
                             QtCore.QPoint(width/k - 1, 1))
        painter.end()
        obj.setIcon(QtGui.QIcon(pixmap))
        self.tmp_colors[obj] = color

    def color_dialog(self):
        color = QtWidgets.QColorDialog().getColor()
        if color.isValid():
            self.set_rectangle_colored(self.sender(), color)

    def retranslate(self):
        # print('Retranslating')
        load_language(self, self.menuLanguageGroup.actions().index(QObject.sender(self)))
        # self._set_tool_names()

    def passgen_generate(self):
        flags = self.get_passgen_flags()
        res = create_pass(self.spinBox_passgen.value(), flags)
        if not res[0] and res[1] > self.spinBox_passgen.value():
            msgres = QMessageBox.critical(self, appname, _translate('Application', 'Password length is not enough: ') +
                                          str(self.spinBox_passgen.value()) + _translate('Application',
                                                                                 '\nDo you want to increase it?'),
                                          QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
            if msgres == QMessageBox.Ok:
                self.spinBox_passgen.setValue(res[1])
                res = create_pass(self.spinBox_passgen.value(), flags)
            else:
                return
        self.label_passgen_password.setText(res[0])

    def toclipboard(self):
        if not QObject.sender(self):
            QApplication.clipboard().setText(self.textEdit_emailchecker.toPlainText())
            self.textEdit_emailchecker.setFocus()
            return
        text = ''
        if QObject.sender(self).objectName() == 'pushButton_passgen_clipboard' or\
                ('action_Copy_all' and self.tabWidget.currentIndex() == 0):
            text = self.label_passgen_password.text()
        elif QObject.sender(self).objectName() == 'pushButton_other_macformat_toclipboard' or\
                (QObject.sender(self).objectName() == 'action_Copy_all' and
                self.tabWidget.currentIndex() == 2 and self.lineEdit_other_macformat.hasFocus()):
            self.lineEdit_other_macformat.setFocus()
            self.lineEdit_other_macformat.setSelection(0, len(self.lineEdit_other_macformat.text()))
            text = self.lineEdit_other_macformat.text()
        elif QObject.sender(self).objectName() == 'pushButton_other_phonenumber_toclipboard' or\
                (QObject.sender(self).objectName() == 'action_Copy_all' and
                self.tabWidget.currentIndex() == 2 and self.lineEdit_other_phonenumber.hasFocus()):
            self.lineEdit_other_phonenumber.setFocus()
            self.lineEdit_other_phonenumber.setSelection(0, len(self.lineEdit_other_phonenumber.text()))
            text = self.lineEdit_other_phonenumber.text()
        elif QObject.sender(self).objectName() == 'pushButton_emailchecker_clipboard' or\
                ('action_Copy_all' and self.tabWidget.currentIndex() == 1):
            self.textEdit_emailchecker.setFocus()
            text = self.textEdit_emailchecker.toPlainText()

        QApplication.clipboard().setText(text)

    def get_passgen_flags(self):
        flag = ''
        if self.checkBox_passgen_luc.isChecked():
            flag += 'u'
        if self.checkBox_passgen_llc.isChecked():
            flag += 'l'
        if self.checkBox_passgen_cuc.isChecked():
            flag += 'p'
        if self.checkBox_passgen_clc.isChecked():
            flag += 'o'
        if self.checkBox_passgen_pretty.isChecked():
            flag += 'c'
        if self.checkBox_passgen_unique.isChecked():
            flag += 't'
        if self.checkBox_passgen_numbers.isChecked():
            flag += 'd'
        if self.checkBox_passgen_symbols.isChecked():
            flag += 's'
        if self.checkBox_passgen_spaces.isChecked():
            flag += 'r'
        if self.checkBox_passgen_csymbols.isChecked():
            flag += 'q'
        if self.checkBox_passgen_escape.isChecked():
            flag += 'e'
        if not flag:
            flag = 'a'
        return flag

    def remove_incorrect_lines(self):
        print(self.textEdit_emailchecker.textCursor().position())
        # test(self)

    def get_emailchecker_flags(self):
        flag = ''
        if self.checkBox_emailchecker_empty.isChecked():
            flag += emailchecker.flags_def['empty']
        if self.checkBox_emailchecker_latin.isChecked():
            flag += emailchecker.flags_def['latin']
        if self.checkBox_emailchecker_cyrillic.isChecked():
            flag += emailchecker.flags_def['cyrillic']
        if self.checkBox_emailchecker_numbers.isChecked():
            flag += emailchecker.flags_def['numbers']
        if self.checkBox_emailchecker_spaces.isChecked():
            flag += emailchecker.flags_def['spaces']
        if self.checkBox_emailchecker_punctuation.isChecked():
            flag += emailchecker.flags_def['punctuation']
        if self.checkBox_emailchecker_emails.isChecked():
            flag += emailchecker.flags_def['emails']
        if self.checkBox_emailchecker_replace.isChecked():
            flag += emailchecker.flags_def['replace']
        if self.checkBox_emailchecker_noemails.isChecked():
            flag += emailchecker.flags_def['noemails']
        return flag

    def emailchecker_transform(self):
        # print("Transform")
        # print('emailchecker_transform', self.textEdit_emailchecker.toHtml())
        cur = self.textEdit_emailchecker.textCursor()
        p = cur.position()

        self.textEdit_emailchecker.blockSignals(True)
        text = self.textEdit_emailchecker.toPlainText()
        flags = self.get_emailchecker_flags()
        self.textEdit_emailchecker.setHtml(emailchecker.transform_context(text, flags))
        self.textEdit_emailchecker.blockSignals(False)
        cur.setPosition(p)
        self.textEdit_emailchecker.setTextCursor(cur)

        self.toHistory(self.sender())
        self.textEdit_emailchecker.setFocus()


def test(wnd):
    srcText = wnd.textEdit_emailchecker.toHtml()
    # print(srcText)
    tgtText = emailchecker.transform_context(srcText)
    wnd.textEdit_emailchecker.setHtml(tgtText)
    # wnd.textEdit.setPlainText(text)

    # app.exec_()

def load_language(wnd, item=0):
    if item:
        if QtWidgets.QApplication.instance().trans_gui.load(langs[item], lang_dir):
            QtWidgets.QApplication.instance().installTranslator(QtWidgets.QApplication.instance().trans_gui)
        if QtWidgets.QApplication.instance().trans_qt.load('qt_ru.qm', lang_dir):
            QtWidgets.QApplication.instance().installTranslator(QtWidgets.QApplication.instance().trans_qt)
    else:
        QtWidgets.QApplication.instance().removeTranslator(QtWidgets.QApplication.instance().trans_qt)
        QtWidgets.QApplication.instance().removeTranslator(QtWidgets.QApplication.instance().trans_gui)
    wnd.retranslateUi(wnd)
    wnd._set_tool_names()

def save_settings(wnd, filename='%s\\%s.ini' % (inidir, appname)):
    cfg = configparser.ConfigParser()
    cfg.optionxform = str
    for i in range(len(wnd.tool_tabs)):
        tab = wnd.tool_tabs[i]
        # tabname = 'Tab_%s' % i
        tabname = tab.objectName()
        chkdict = {c.objectName():str(c.isChecked()) for c in tab.findChildren(QtWidgets.QCheckBox)}
        spndict = {c.objectName():str(c.value()) for c in tab.findChildren(QtWidgets.QSpinBox)}
        gbdict = {}
        if tab == wnd.tab_other:
            gbdict = {c.objectName():str(c.isEnabled()) for c in tab.findChildren(QtWidgets.QGroupBox)}
        # rbtndict = {c.objectName():str(c.isChecked()) for c in tab.findChildren(QtWidgets.QRadioButton)}
        cfg[tabname] = {}
        cfg[tabname].update(chkdict)
        cfg[tabname].update(spndict)
        cfg[tabname].update(gbdict)
        cfg[tabname][TabPositionKeyName] = str(wnd.tabWidget.indexOf(tab))
        cfg[tabname][EnabledKeyName] = str(tab.isEnabled())
        # cfg[tabname].update(rbtndict)

        if i == wnd.tabWidget.currentIndex():
            cfg[tabname][CurrentTabKeyName] = 'True'

    for i, act in enumerate(wnd.menuLanguageGroup.actions()):
        if act.isChecked():
            cfg[MenuLaguageSectionName] = {}
            cfg[MenuLaguageSectionName]['CheckedItem'] = str(i)
            break

    cfg[ColorsSectionName] = {}
    for k, v in emailchecker.colors_def.items():
        cfg[ColorsSectionName][k] = v

    cfg[FontsSectionName] = {}
    cfg[FontsSectionName]['label_passgen_password_size'] = str(wnd.label_passgen_password.font().pointSize())
    cfg[FontsSectionName]['label_passgen_password_family'] = wnd.label_passgen_password.font().family()
    cfg[FontsSectionName]['textEdit_emailchecker_size'] = str(emailchecker.font_size)
    cfg[FontsSectionName]['textEdit_emailchecker_family'] = emailchecker.font_family
    cfg[FontsSectionName]['checkBox_passgen_Bold'] = str(wnd.label_passgen_password.font().bold())
    cfg[FontsSectionName]['checkBox_emailchecker_Bold'] = str(emailchecker.bold)

    # cfg[ToolsTreeSectionName] = {}
    # cfg[ToolsTreeSectionName]['tree'] = json.dumps(wnd.tools)

    with open(filename, 'w') as f:
        cfg.write(f)

def load_settings(wnd, filename='%s\\%s.ini' % (inidir, appname)):
    if not os.path.exists(filename):
        return
    cfg = configparser.ConfigParser()
    cfg.optionxform = str
    cfg.read(filename)
    try:
        for sec in cfg.sections():
            if sec.startswith(TabWidgetSectionName):
                tab = wnd.tabWidget.findChild(QtWidgets.QWidget, sec)
                for key in cfg[sec]:
                    qtype = key.split('_')[0]
                    if qtype == 'checkBox':
                        tab.findChild(QtWidgets.QCheckBox, key).setChecked(cfg[sec][key] == 'True')
                    # if qtype == 'radioButton':
                    #     tab.findChild(QtWidgets.QRadioButton, key).setChecked(cfg[sec][key] == 'True')
                    if qtype == 'spinBox':
                        tab.findChild(QtWidgets.QSpinBox, key).setValue(int(cfg[sec][key]))
                    if qtype == 'groupBox':
                        tab.findChild(QtWidgets.QGroupBox, key).setEnabled(cfg[sec][key] == 'True')
                    if qtype == TabPositionKeyName:
                        wnd.tabWidget.tabBar().moveTab(wnd.tabWidget.indexOf(tab), int(cfg[sec][TabPositionKeyName]))
                    if qtype == CurrentTabKeyName:
                        wnd.tabWidget.setCurrentIndex(wnd.tabWidget.indexOf(tab))
                    if qtype == EnabledKeyName:
                        tab.setEnabled(cfg[sec][EnabledKeyName] == 'True')
            elif sec == ColorsSectionName:
                for key in cfg[sec]:
                    emailchecker.colors_def[key] = cfg[sec][key]
                wnd.label_passgen_password.setStyleSheet('QLabel { color: %s; }' %
                                                          emailchecker.colors_def[emailchecker.flags_def['password']])
            elif sec == MenuLaguageSectionName:
                item = int(cfg[sec]['CheckedItem'])
                wnd.menuLanguage.actions()[item].setChecked(True)
                if item:
                    load_language(wnd, item)
            elif sec == FontsSectionName:
                font = QtGui.QFont('MS Shell Dlg 2', 8)
                for key in cfg[sec]:
                    if key == 'textEdit_emailchecker_size':
                        emailchecker.font_size = float(cfg[sec][key])
                    elif key == 'textEdit_emailchecker_family':
                        emailchecker.font_family = cfg[sec][key]
                    elif key == 'checkBox_emailchecker_Bold':
                        emailchecker.bold = cfg[sec][key] == 'True'
                    elif key == 'label_passgen_password_family':
                        font.setFamily(cfg[sec][key])
                    elif key == 'label_passgen_password_size':
                        font.setPointSize(int(cfg[sec][key]))
                    elif key == 'checkBox_passgen_Bold':
                        font.setBold(cfg[sec][key] == 'True')
                wnd.label_passgen_password.setFont(font)
        wnd.create_toolsmodel()
        wnd.set_tools_from_toolsmodel()
    except Exception as e:
        QMessageBox.critical(wnd, appname, _translate('Application', 'Check or delete ') + filename +
                    _translate('Application', '. Error while reading: ') + str(e))
        # raise


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.trans_qt = QTranslator()
    app.trans_gui = QTranslator()
    window = AdminToolsWindow()
    load_settings(window)
    window.show()
    window.textEdit_emailchecker.textChanged.emit()
    window.set_mac_format()
    #
    # window.tools_set()
    window.lineEdit_other_macformat.setCursorPosition(0)
    # window.toolsModel.restore_tree(window.tools)
    # window.init_options()
    # window._restore_tools(window.optionsWindow.tools_treeWidget.invisibleRootItem(), window.tools)
    # window.init_about()
    # window.init_options()
    # window.showOptions()
    app.exec()
    save_settings(window)

if __name__ == '__main__':
    # test()
    # d = [(2, None), (2, None), (1, [(0, None), (2, None), (0, None)])]
    # print(json.dumps(d))
    # k, v = d[0].items()
    # print(k,v)
    main()
