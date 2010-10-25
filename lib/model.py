# Wanted list model for shopping list app
from PySide import QtCore
import logging

logger = logging.getLogger("model")

class WantedListModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self._things = []

    def rowCount(self, parent=QtCore.QModelIndex()):
        if not parent.isValid():
            return len(self._things)
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                logger.debug("Display data requested for row %d" % index.row())
                return self._things[index.row()]
        else:
            logger.debug("Invalid index: %s" % index)
        return None
    
    @QtCore.Slot(str)
    def addThing(self, thing):
        print("Add thing: %s" % (thing))
        self.beginInsertRows(QtCore.QModelIndex(), len(self._things), len(self._things))
        self._things.append(thing)
        self.endInsertRows()

if __name__=="__main__":
    import unittest
    class WantedListModelTest(unittest.TestCase):
        def testAddThing(self):
            model = WantedListModel()
            self.assertEqual(0, model.rowCount())
            model.addThing("foobar")
            self.assertEqual(1, model.rowCount())

        def testData(self):
            model = WantedListModel()
            model.addThing("bar baz")
            self.assertEqual("bar baz", model.data(model.index(0, 0)))

    unittest.main()
