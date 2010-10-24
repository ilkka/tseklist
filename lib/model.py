# Wanted list model for shopping list app
from PySide import QtCore

class WantedListModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self._things = []

    def rowCount(self, parent=QtCore.QModelIndex()):
        if not parent.isValid():
            return len(self._things)
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self._things[index.row])
        elif role == QtCore.Qt.BackgroundRole:
            return QVariant()
    
    @QtCore.Slot()
    def addThing(self, thing):
        print("Add thing: %s" % (thing))
        self.beginInsertRows(QtCore.QModelIndex(), len(self._things), len(self._things))
        self._things.append(thing)
        self.endInsertRows()

