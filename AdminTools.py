#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QApplication, QMessageBox, QActionGroup, QTranslator, QObject, QColor, QPixmap, QKeySequence

import MainWindow
from pass_gen import create_pass
import email_checker
from options import Ui_Dialog

import os
import configparser

from history import History

from ipcalc import Ipaddress

import phonenormalizer
import toolstreemodel
import translit


_translate = QtCore.QCoreApplication.translate
appname = os.path.splitext(os.path.basename(sys.argv[0]))[0]
TabWidgetSectionName = 'tab_'
CurrentTabKeyName = 'CurrentTab'
TabPositionKeyName = 'TabPosition'
EnabledKeyName = 'Enabled'
MenuLanguageSectionName = 'MenuLanguage'
ColorsSectionName = 'Colors'
FontsSectionName = 'Fonts'
# ToolsTreeSectionName = 'Tools'

src_dir = 'source'
lang_dir = r'%s\languages' % src_dir
icon = r'%s\Spanner.ico' % src_dir
ini_dir = src_dir
langs = ['', 'ru_RU.qm']


# noinspection PyArgumentList
class AdminToolsWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    about = None
    optionsWindow = None
    options = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(icon))
        self.pushButton_passgen_generate.clicked.connect(self.passgen_generate)
        self.pushButton_passgen_clipboard.clicked.connect(self.to_clipboard)
        self.pushButton_email_checker_clipboard.clicked.connect(self.to_clipboard)
        self.pushButton_other_transliteration_to_clipboard.clicked.connect(self.to_clipboard)
        self.textEdit_email_checker.textChanged.connect(self.email_checker_transform)
        # self.installEventFilter(self)
        self.textEdit_email_checker.installEventFilter(self)
        self.textEdit_email_checker.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.textEdit_email_checker.customContextMenuRequested.connect(self.contextMenuEvent)
        for cb in self.groupBox_email_checker_highlight.findChildren(QtWidgets.QCheckBox):
            cb.clicked.connect(self.email_checker_transform)
        for cb in self.groupBox_email_checker_edit.findChildren(QtWidgets.QCheckBox):
            cb.clicked.connect(self.email_checker_transform)
        self.actionQuit.triggered.connect(QtWidgets.qApp.quit)
        self.actionQuit.setShortcut(QKeySequence(_translate('Application', 'Ctrl+Q')))
        self.actionAbout.triggered.connect(self.show_about)
        self.menuLanguageGroup = QActionGroup(self)
        for act in self.menuLanguage.actions():
            self.menuLanguageGroup.addAction(act)
            act.triggered.connect(self.retranslate)
        self.menuLanguageGroup.actions()[0].setChecked(True)
        self.actionSettings.triggered.connect(self.show_options)
        self.action_Undo.triggered.connect(self.undo)

        undo_key_sequence = QKeySequence(_translate('Application', 'Ctrl+Z'))
        undo_shortcut = QtWidgets.QShortcut(undo_key_sequence, self)
        undo_shortcut.activated.connect(self.undo)

        self.action_Undo.setShortcut(undo_key_sequence)
        self.action_Redo.triggered.connect(self.redo)

        redo_key_sequence = QKeySequence(_translate('Application', 'Ctrl+Shift+Z'))
        redo_shortcut = QtWidgets.QShortcut(redo_key_sequence, self)
        redo_shortcut.activated.connect(self.redo)
        self.action_Redo.setShortcut(redo_key_sequence)

        copy_all_key_sequence = QKeySequence(_translate('Application', 'Ctrl+Shift+C'))
        copy_all_shortcut = QtWidgets.QShortcut(copy_all_key_sequence, self)
        copy_all_shortcut.activated.connect(self.to_clipboard)

        self.menubar.hovered.connect(self.main_menu_modifier)

        self.lineEdit_other_mac_format.textChanged.connect(self.set_mac_format)
        self.checkBox_other_mac_format_linux.clicked.connect(self.set_mac_format)
        self.checkBox_other_mac_format_uppercase.clicked.connect(self.set_mac_format)
        self.pushButton_other_mac_format_to_clipboard.clicked.connect(self.to_clipboard)
        self.pushButton_other_ipcalc_calculate.clicked.connect(self.calculate_network)

        self.lineEdit_other_phone_number.textChanged.connect(self._normalize_number)
        self.pushButton_other_phone_number_to_clipboard.clicked.connect(self.to_clipboard)
        self.checkBox_other_phone_number.clicked.connect(self._normalize_number)

        self.lineEdit_other_transliteration.textChanged.connect(self._transliterate)
        self.radioButton_other_transliteration_as_is.toggled.connect(self._transliterate)
        self.radioButton_other_transliteration_upper.toggled.connect(self._transliterate)
        self.radioButton_other_transliteration_lower.toggled.connect(self._transliterate)

        self._ip = Ipaddress()

        combo_box_items = ['%s (%s)' % (self._ip.masks.index(x), x) for x in self._ip.masks][::-1]
        self.comboBox_other_ipcalc_mask.addItems(combo_box_items)

        self.tmp_colors = {}
        self.init_about()
        self._history = History()
        self.tool_names = {}
        self.tabWidget.tabBar().tabMoved.connect(self._tool_tab_moved)
        self.tool_tabs = [self.tabWidget.widget(i) for i in range(self.tabWidget.count())]
        self.toolsModel = toolstreemodel.TreeModel()

    def _transliterate(self):
        self.label_other_transliteration.setText(translit.translit(self.lineEdit_other_transliteration.text()))
        if self.radioButton_other_transliteration_lower.isChecked():
            self.label_other_transliteration.setText(self.label_other_transliteration.text().lower())
        elif self.radioButton_other_transliteration_upper.isChecked():
            self.label_other_transliteration.setText(self.label_other_transliteration.text().upper())

    def set_tool_names(self):
        self.tool_names = {self.tab_passgen: _translate('Application', 'Password generator'),
                           self.tab_email_checker: _translate('Application', 'E-mail checker'),
                           self.tab_other: _translate('Application', 'Other')}

    def _tool_tab_moved(self, frm, to):
        self.tool_tabs.insert(to, self.tool_tabs.pop(frm))

    def _normalize_number(self):
        flag = ''
        if self.checkBox_other_phone_number.isChecked():
            flag = phonenormalizer.flags['escape']

        pos = self.lineEdit_other_phone_number.cursorPosition()
        self.lineEdit_other_phone_number.blockSignals(True)
        self.lineEdit_other_phone_number.setText(
            phonenormalizer.normalize(self.lineEdit_other_phone_number.text(), flag)
        )
        self.lineEdit_other_phone_number.blockSignals(False)
        self.lineEdit_other_phone_number.setCursorPosition(pos)

    @staticmethod
    def _validate_ip(ip):
        octets = ip.split('.')
        if len(octets) != 4:
            return False
        for octet in octets:
            try:
                number = int(octet)
            except ValueError:
                return False

            if number > 255:
                return False

            if (octet.startswith('0') and number > 0) or (octet == '0' * len(octet) and len(octet) > 1):
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
            self.label_other_ipcalc_hostcount.setText(str(self._ip.hosts['host_count']))
            self.label_other_ipcalc_hostmin.setText(self._ip.hosts['host_min'])
            self.label_other_ipcalc_hostmax.setText(self._ip.hosts['host_max'])
        except ValueError:
            QMessageBox.critical(self, appname, _translate('Application', 'Invalid IP-address.'))

    def set_mac_format(self):
        pos = self.lineEdit_other_mac_format.cursorPosition()
        if self.checkBox_other_mac_format_linux.isChecked():
            self.lineEdit_other_mac_format.setInputMask('HH:HH:HH:HH:HH:HH;_')
        else:
            self.lineEdit_other_mac_format.setInputMask('HH-HH-HH-HH-HH-HH;_')
        self.lineEdit_other_mac_format.blockSignals(True)
        if self.checkBox_other_mac_format_uppercase.isChecked():
            self.lineEdit_other_mac_format.setText(self.lineEdit_other_mac_format.text().upper())
        else:
            self.lineEdit_other_mac_format.setText(self.lineEdit_other_mac_format.text().lower())
        self.lineEdit_other_mac_format.blockSignals(False)
        self.lineEdit_other_mac_format.setCursorPosition(pos)
        self.lineEdit_other_mac_format.setFocus()

    def main_menu_modifier(self):
        if self.tabWidget.currentIndex() == 0:
            self.action_Undo.setEnabled(False)
            self.action_Redo.setEnabled(False)
        elif self.tabWidget.currentIndex() == 1:
            # print('Got it')
            self.action_Undo.setEnabled(self._history.undo_available)
            self.action_Redo.setEnabled(self._history.redo_available)

    def contextMenuEvent(self, point):
        menu = self.textEdit_email_checker.createStandardContextMenu()
        # ContextMenu Undo
        menu.actions()[0].setEnabled(self._history.undo_available)
        menu.actions()[0].triggered.connect(self.undo)
        # ContextMenu Redo
        menu.actions()[1].setEnabled(self._history.redo_available)
        menu.actions()[1].triggered.connect(self.redo)
        menu.exec_(self.textEdit_email_checker.mapToGlobal(point))

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.ShortcutOverride and event.modifiers() == QtCore.Qt.ControlModifier:
            if event.key() == QtCore.Qt.Key_Z:
                self.undo()
                return True
        if event.type() == QtCore.QEvent.ShortcutOverride and event.modifiers() == (QtCore.Qt.ControlModifier |
                                                                                    QtCore.Qt.ShiftModifier):
            if event.key() == QtCore.Qt.Key_Z:
                self.redo()
                return True
            elif event.key() == QtCore.Qt.Key_C:
                self.to_clipboard()
                return True
        return super(AdminToolsWindow, self).eventFilter(source, event)

    def create_snapshot(self):
        snap = {}
        for o in self.tab_email_checker.findChildren(QtWidgets.QCheckBox):
            snap[o.objectName()] = {}
            snap[o.objectName()]['setChecked'] = o.isChecked()

        ten = self.textEdit_email_checker.objectName()
        snap[ten] = {}
        snap[ten]['setHtml'] = self.textEdit_email_checker.toHtml()
        snap[ten]['setPosition'] = self.textEdit_email_checker.textCursor().position()
        # print(snap)
        return snap

    def load_snapshot(self, snapshot):
        if not snapshot:
            return

        for name in snapshot.keys():
            o_type = name.split('_')[0]

            if o_type == 'checkBox':
                obj = self.tab_email_checker.findChild(QtWidgets.QCheckBox, name)
                for func, val in snapshot[name].items():
                    if func == 'setChecked':
                        obj.blockSignals(True)
                        obj.setChecked(val)
                        obj.blockSignals(False)
            if o_type == 'textEdit':
                obj = self.tab_email_checker.findChild(QtWidgets.QTextEdit, name)
                for func, val in snapshot[name].items():
                    if func == 'setHtml':
                        obj.blockSignals(True)
                        obj.setHtml(val)
                        obj.blockSignals(False)
                    if func == 'setPosition':
                        obj.blockSignals(True)
                        tk = self.textEdit_email_checker.textCursor()
                        tk.setPosition(val)
                        obj.setTextCursor(tk)
                        obj.blockSignals(False)

    def to_history(self, obj):
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

    def show_about(self):
        self.init_about()
        self.about.exec()

    def create_tools_model(self):
        # print('Creating model')
        self.toolsModel = toolstreemodel.TreeModel()

        for i in range(len(self.tool_tabs)):
            if i == self.tool_tabs.index(self.tab_other):
                ti, index = self.toolsModel.addItem(data=self.tool_names[self.tab_other], obj=self.tab_other)
                for gb in self.tab_other.findChildren(QtWidgets.QGroupBox):
                    ti_gb, index = self.toolsModel.addItem(gb.title()[:-1], ti, gb)
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

    def set_tools_from_tools_model(self):
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
        self.optionsWindow.doubleSpinBox_fonts_email_checker.setValue(email_checker.font_size)
        self.optionsWindow.fontComboBox_fonts_email_checker.setCurrentFont(QtGui.QFont(email_checker.font_family))
        self.optionsWindow.doubleSpinBox_fonts_passgen.setValue(self.label_passgen_password.font().pointSize())
        self.optionsWindow.fontComboBox_fonts_passgen.setCurrentFont(
            QtGui.QFont(self.label_passgen_password.font().family())
        )
        for btn in self.optionsWindow.tabWidget.findChildren(QtWidgets.QPushButton):
            btn.clicked.connect(self.color_dialog)
            self.set_rectangle_colored(
                btn,
                email_checker.colors_def[email_checker.flags_def[btn.objectName().split('_')[-1]]]
            )
        self.optionsWindow.checkBox_passgen_Bold.setChecked(self.label_passgen_password.font().bold())
        self.optionsWindow.checkBox_email_checker_Bold.setChecked(email_checker.bold)
        self.optionsWindow.ttwColumn = 0
        self.create_tools_model()
        self.optionsWindow.tools_treeView.setModel(self.toolsModel)
        self.optionsWindow.tools_treeView.setHeaderHidden(True)
        self.optionsWindow.tools_treeView.expandAll()
        # self._restore_tools(self.optionsWindow.tools_treeWidget.invisibleRootItem(), self.tools)
        # print('Options inited')
        # weight = [f.Thin, f.ExtraLight, f.Light, f.Normal, f.Medium, f.DemiBold, f.Bold, f.ExtraBold, f.Black]

    def show_options(self):
        self.init_options()
        res = self.options.exec()
        if res:
            # print('showOptions if res', self.tmp_colors.items())
            for obj, color in self.tmp_colors.items():
                # print(obj)
                # print(obj.objectName())
                flag = email_checker.flags_def[obj.objectName().split('_')[-1]]
                email_checker.colors_def[flag] = color.name()
            # print('for obj, color in self.tmp_colors.items():')
            email_checker.font_size = self.optionsWindow.doubleSpinBox_fonts_email_checker.value()
            email_checker.font_family = self.optionsWindow.fontComboBox_fonts_email_checker.currentFont().family()
            font = QtGui.QFont(
                QtGui.QFont(
                    self.optionsWindow.fontComboBox_fonts_passgen.currentFont().family(),
                    self.optionsWindow.doubleSpinBox_fonts_passgen.value()
                )
            )
            font.setBold(self.optionsWindow.checkBox_passgen_Bold.isChecked())
            self.label_passgen_password.setFont(font)
            self.label_passgen_password.setStyleSheet('QLabel { color: %s; }' %
                                                      email_checker.colors_def[email_checker.flags_def['password']])
            email_checker.bold = self.optionsWindow.checkBox_email_checker_Bold.isChecked()
            self.textEdit_email_checker.textChanged.emit()
            # self.tools = self._dump_tools(self.optionsWindow.tools_treeWidget.invisibleRootItem())
            # self.tools = self.toolsModel.dump_tree()
            # self.tools_set()
            self.set_tools_from_tools_model()

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
        load_language(self, self.menuLanguageGroup.actions().index(QObject.sender(self)))

    def passgen_generate(self):
        flags = self.get_passgen_flags()
        res = create_pass(self.spinBox_passgen.value(), flags)
        if not res[0] and res[1] > self.spinBox_passgen.value():
            msg_res = QMessageBox.critical(
                self,
                appname,
                _translate('Application', 'Password length is not enough: ') +
                str(self.spinBox_passgen.value()) + _translate('Application', '\nDo you want to increase it?'),
                QMessageBox.Ok | QMessageBox.Cancel,
                QMessageBox.Ok
            )
            if msg_res == QMessageBox.Ok:
                self.spinBox_passgen.setValue(res[1])
                res = create_pass(self.spinBox_passgen.value(), flags)
            else:
                return
        self.label_passgen_password.setText(res[0])

    def to_clipboard(self):
        if not QObject.sender(self):
            QApplication.clipboard().setText(self.textEdit_email_checker.toPlainText())
            self.textEdit_email_checker.setFocus()
            return
        text = ''
        if QObject.sender(self).objectName() == 'pushButton_passgen_clipboard':
            text = self.label_passgen_password.text()
        elif QObject.sender(self).objectName() == 'pushButton_other_mac_format_to_clipboard':
            self.lineEdit_other_mac_format.setFocus()
            self.lineEdit_other_mac_format.setSelection(0, len(self.lineEdit_other_mac_format.text()))
            text = self.lineEdit_other_mac_format.text()
        elif QObject.sender(self).objectName() == 'pushButton_other_phone_number_to_clipboard':
            self.lineEdit_other_phone_number.setFocus()
            self.lineEdit_other_phone_number.setSelection(0, len(self.lineEdit_other_phone_number.text()))
            text = self.lineEdit_other_phone_number.text()
        elif QObject.sender(self).objectName() == 'pushButton_email_checker_clipboard':
            self.textEdit_email_checker.setFocus()
            text = self.textEdit_email_checker.toPlainText()
        elif QObject.sender(self).objectName() == 'pushButton_other_transliteration_to_clipboard':
            self.label_other_transliteration.setFocus()
            self.label_other_transliteration.setSelection(0, len(self.label_other_transliteration.text()))
            text = self.label_other_transliteration.text()

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
        print(self.textEdit_email_checker.textCursor().position())
        # test(self)

    def get_email_checker_flags(self):
        flag = ''
        if self.checkBox_email_checker_empty.isChecked():
            flag += email_checker.flags_def['empty']
        if self.checkBox_email_checker_latin.isChecked():
            flag += email_checker.flags_def['latin']
        if self.checkBox_email_checker_cyrillic.isChecked():
            flag += email_checker.flags_def['cyrillic']
        if self.checkBox_email_checker_numbers.isChecked():
            flag += email_checker.flags_def['numbers']
        if self.checkBox_email_checker_spaces.isChecked():
            flag += email_checker.flags_def['spaces']
        if self.checkBox_email_checker_punctuation.isChecked():
            flag += email_checker.flags_def['punctuation']
        if self.checkBox_email_checker_emails.isChecked():
            flag += email_checker.flags_def['emails']
        if self.checkBox_email_checker_replace.isChecked():
            flag += email_checker.flags_def['replace']
        if self.checkBox_email_checker_no_emails.isChecked():
            flag += email_checker.flags_def['no_emails']
        return flag

    def email_checker_transform(self):
        # print("Transform")
        # print('email_checker_transform', self.textEdit_email_checker.toHtml())
        cur = self.textEdit_email_checker.textCursor()
        p = cur.position()

        self.textEdit_email_checker.blockSignals(True)
        text = self.textEdit_email_checker.toPlainText()
        flags = self.get_email_checker_flags()
        self.textEdit_email_checker.setHtml(email_checker.transform_context(text, flags))
        self.textEdit_email_checker.blockSignals(False)
        cur.setPosition(p)
        self.textEdit_email_checker.setTextCursor(cur)

        self.to_history(self.sender())
        self.textEdit_email_checker.setFocus()


# noinspection PyArgumentList
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
    wnd.set_tool_names()


def save_settings(wnd, filename='%s\\%s.ini' % (ini_dir, appname)):
    cfg = configparser.ConfigParser()
    cfg.optionxform = str
    for i in range(len(wnd.tool_tabs)):
        tab = wnd.tool_tabs[i]
        tab_name = tab.objectName()
        chk_dict = {c.objectName(): str(c.isChecked()) for c in tab.findChildren(QtWidgets.QCheckBox)}
        spn_dict = {c.objectName(): str(c.value()) for c in tab.findChildren(QtWidgets.QSpinBox)}
        radio_btn_dict = {c.objectName(): str(c.isChecked()) for c in tab.findChildren(QtWidgets.QRadioButton)}
        gb_dict = {}
        if tab == wnd.tab_other:
            gb_dict = {c.objectName(): str(c.isEnabled()) for c in tab.findChildren(QtWidgets.QGroupBox)}
        cfg[tab_name] = {}
        cfg[tab_name].update(chk_dict)
        cfg[tab_name].update(spn_dict)
        cfg[tab_name].update(gb_dict)
        cfg[tab_name][TabPositionKeyName] = str(wnd.tabWidget.indexOf(tab))
        cfg[tab_name][EnabledKeyName] = str(tab.isEnabled())
        cfg[tab_name].update(radio_btn_dict)

        if i == wnd.tabWidget.currentIndex():
            cfg[tab_name][CurrentTabKeyName] = 'True'

    for i, act in enumerate(wnd.menuLanguageGroup.actions()):
        if act.isChecked():
            cfg[MenuLanguageSectionName] = {}
            cfg[MenuLanguageSectionName]['CheckedItem'] = str(i)
            break

    cfg[ColorsSectionName] = {}
    for k, v in email_checker.colors_def.items():
        cfg[ColorsSectionName][k] = v

    cfg[FontsSectionName] = {}
    cfg[FontsSectionName]['label_passgen_password_size'] = str(wnd.label_passgen_password.font().pointSize())
    cfg[FontsSectionName]['label_passgen_password_family'] = wnd.label_passgen_password.font().family()
    cfg[FontsSectionName]['textEdit_email_checker_size'] = str(email_checker.font_size)
    cfg[FontsSectionName]['textEdit_email_checker_family'] = email_checker.font_family
    cfg[FontsSectionName]['checkBox_passgen_Bold'] = str(wnd.label_passgen_password.font().bold())
    cfg[FontsSectionName]['checkBox_email_checker_Bold'] = str(email_checker.bold)

    # cfg[ToolsTreeSectionName] = {}
    # cfg[ToolsTreeSectionName]['tree'] = json.dumps(wnd.tools)

    with open(filename, 'w') as f:
        cfg.write(f)


# noinspection PyArgumentList
def load_settings(wnd, filename='%s\\%s.ini' % (ini_dir, appname)):
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
                    qt_type = key.split('_')[0]
                    if qt_type == 'checkBox':
                        tab.findChild(QtWidgets.QCheckBox, key).setChecked(cfg[sec][key] == 'True')
                    if qt_type == 'radioButton':
                        tab.findChild(QtWidgets.QRadioButton, key).setChecked(cfg[sec][key] == 'True')
                    if qt_type == 'spinBox':
                        tab.findChild(QtWidgets.QSpinBox, key).setValue(int(cfg[sec][key]))
                    if qt_type == 'groupBox':
                        tab.findChild(QtWidgets.QGroupBox, key).setEnabled(cfg[sec][key] == 'True')
                    if qt_type == TabPositionKeyName:
                        wnd.tabWidget.tabBar().moveTab(wnd.tabWidget.indexOf(tab), int(cfg[sec][TabPositionKeyName]))
                    if qt_type == CurrentTabKeyName:
                        wnd.tabWidget.setCurrentIndex(wnd.tabWidget.indexOf(tab))
                    if qt_type == EnabledKeyName:
                        tab.setEnabled(cfg[sec][EnabledKeyName] == 'True')
            elif sec == ColorsSectionName:
                for key in cfg[sec]:
                    email_checker.colors_def[key] = cfg[sec][key]
                wnd.label_passgen_password.setStyleSheet(
                    'QLabel { color: %s; }' % email_checker.colors_def[email_checker.flags_def['password']]
                )
            elif sec == MenuLanguageSectionName:
                item = int(cfg[sec]['CheckedItem'])
                wnd.menuLanguage.actions()[item].setChecked(True)
                if item:
                    load_language(wnd, item)
            elif sec == FontsSectionName:
                font = QtGui.QFont('MS Shell Dlg 2', 8)
                for key in cfg[sec]:
                    if key == 'textEdit_email_checker_size':
                        email_checker.font_size = float(cfg[sec][key])
                    elif key == 'textEdit_email_checker_family':
                        email_checker.font_family = cfg[sec][key]
                    elif key == 'checkBox_email_checker_Bold':
                        email_checker.bold = cfg[sec][key] == 'True'
                    elif key == 'label_passgen_password_family':
                        font.setFamily(cfg[sec][key])
                    elif key == 'label_passgen_password_size':
                        font.setPointSize(int(cfg[sec][key]))
                    elif key == 'checkBox_passgen_Bold':
                        font.setBold(cfg[sec][key] == 'True')
                wnd.label_passgen_password.setFont(font)
        wnd.create_tools_model()
        wnd.set_tools_from_tools_model()
    except Exception as e:
        QMessageBox.critical(
            wnd,
            appname,
            _translate('Application', 'Check or delete ') +
            filename + _translate('Application', '. Error while reading: ') + str(e)
        )
        # raise


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.trans_qt = QTranslator()
    app.trans_gui = QTranslator()
    window = AdminToolsWindow()
    load_settings(window)
    window.show()
    window.textEdit_email_checker.textChanged.emit()
    window.set_mac_format()
    #
    # window.tools_set()
    window.lineEdit_other_mac_format.setCursorPosition(0)
    # window.toolsModel.restore_tree(window.tools)
    # window.init_options()
    # window._restore_tools(window.optionsWindow.tools_treeWidget.invisibleRootItem(), window.tools)
    # window.init_about()
    # window.init_options()
    # window.showOptions()
    app.exec()
    save_settings(window)


if __name__ == '__main__':
    main()
