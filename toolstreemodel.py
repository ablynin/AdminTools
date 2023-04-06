#!/usr/bin/env python

from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt
from PyQt5.QtWidgets import QApplication, QTreeView


defColumnCount = 1

class TreeItem(object):
    def __init__(self, data, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []
        self._checkState = Qt.Unchecked
        self._linkedObject = None

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return defColumnCount

    def data(self, column=defColumnCount - 1):
        try:
            return self.itemData
        except IndexError:
            return None

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)

        return 0

    @property
    def checkState(self):
        return self._checkState

    @checkState.setter
    def checkState(self, state):
        self._checkState = state

    @property
    def linkedObject(self):
        return self._linkedObject

    @linkedObject.setter
    def linkedObject(self, obj):
        self._linkedObject = obj

class TreeModel(QAbstractItemModel):
    def __init__(self, parent=None):
        super(TreeModel, self).__init__(parent)
        self.rootItem = TreeItem("")
        self.indexes = []

    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def addItem(self, data, parent=None, obj=None):
        if not parent:
            parent = self.rootItem

        ti = TreeItem(data, parent)
        ti.linkedObject = obj
        parent.appendChild(ti)
        index = self.createIndex(parent.childItems.index(ti), defColumnCount -1 , ti)
        self.indexes.append(index)

        return ti, index

    def data(self, index, role):
        if not index.isValid():
            return None

        if role == Qt.CheckStateRole:
            return index.internalPointer().checkState

        if role == Qt.UserRole:
            return index.internalPointer().linkedObject

        if role != Qt.DisplayRole:
            return None

        item = index.internalPointer()

        return item.data(index.column())

    def setData(self, index, value, role):
        if not index.isValid():
            return None

        if role == Qt.CheckStateRole:
            # print(index, value, role)
            item = index.internalPointer()
            item.checkState = value
            if item.childCount():
                self.checkStateForCildren(index)
            self.checkStateForParent(index)
            self.dataChanged.emit(index, index)
            self.emitDataChangedForParents(index)
            return True

        if role == Qt.UserRole:
            item = index.internalPointer()
            item.linkedObject = value

    def checkStateForCildren(self, index):
        item = index.internalPointer()
        if item.checkState == Qt.PartiallyChecked:
            return
        for child in item.childItems:
            child.checkState = item.checkState

    def checkStateForParent(self, index):
        item = index.internalPointer()
        if item.parent() is self.rootItem:
            return

        states = [c.checkState for c in item.parent().childItems]

        if not all(states) and any(states):
            item.parent().checkState = Qt.PartiallyChecked
        else:
            item.parent().checkState = item.checkState

    def emitDataChangedForParents(self, index):
        self.dataChanged.emit(index.parent(), index.parent())

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsAutoTristate | Qt.ItemIsUserCheckable

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def dump_tree(self, parent=None):
        if not parent:
            parent = self.rootItem
        l = list(range(parent.childCount()))
        for i in l:
            if not parent.child(i).childCount():
                l[i] = [parent.child(i).data(), parent.child(i).checkState, None]
            else:
                l[i] = [parent.child(i).data(), parent.child(i).checkState, self.dump_tree(parent.child(i))]
        return l

    def restore_tree(self, childs, parent=None):
        if not parent:
            parent = self.rootItem

        for i, item in enumerate(childs):
            it, index = self.addItem(item[0], parent)

            if not item[2]:
                self.setData(index, item[1], Qt.CheckStateRole)
            else:
                self.restore_tree(item[2], it)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    model = TreeModel()
    dump = [['test1', 0, None], ['test2', 0, None], ['test3', 0, [['test31', 2, None], ['test32', 0, None], ['test33', 0, None]]]]
    import json
    d = json.dumps(dump)
    s = json.loads(d)
    model.restore_tree(s)
    view = QTreeView()
    view.setModel(model)
    view.setWindowTitle("Simple Tree Model")
    view.setHeaderHidden(True)
    view.show()
    view.expandAll()
    sys.exit(app.exec_())
