#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import PyQt5.Qt


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent=parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.line = QtWidgets.QTextEdit()
        self.button = QtWidgets.QPushButton("Button")
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.line)
        shortcut = QtWidgets.QShortcut(PyQt5.Qt.QKeySequence("Ctrl+Shift+O"), self)
        shortcut.activated.connect(self.test)

    def test(self):
        self.button.setText('TEST')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())