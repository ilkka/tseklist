# Wanted list model for shopping list app
from PySide import QtCore
import logging

logger = logging.getLogger("model")

class WantedListItem(QtCore.QObject):
    statusChanged = QtCore.Signal()
    titleChanged = QtCore.Signal()

    def __init__(self, title, parent=None):
        super(WantedListItem, self).__init__(parent)
        self._title = title
        self._status = False

    def get_title(self):
        return self._title

    def set_title(self, title):
        if self._title != title:
            self._title = title
            self.titleChanged.emit()

    title = QtCore.Property(str, get_title, set_title, titleChanged)

    def get_status(self):
        return self._status

    def set_status(self, status):
        if self._status != status:
            self._status = status
            self.statusChanged.emit()

    status = QtCore.Property(bool, get_status, set_status, statusChanged)

class WantedListModel(QtCore.QAbstractListModel):
    """Wanted List Model

    This is a model class that inherits QAbstractListModel.
    It unfortunately does not work in a QML ListView right now.
    See http://stackoverflow.com/questions/4013615/how-to-provide-data-from-pyside-qabstractitemmodel-subclass-to-qml-listview
    """
    def __init__(self, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self._things = []

    def rowCount(self, parent=QtCore.QModelIndex()):
        logger.debug("rowCount() called")
        logger.debug("Have %d rows" % len(self._things))
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
        logger.debug("addThing: %s" % thing)
        self.beginInsertRows(QtCore.QModelIndex(), len(self._things), len(self._things))
        self._things.append(thing)
        self.endInsertRows()

if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
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

    class WantedListItemTest(unittest.TestCase):
        def testSetTitle(self):
            i = WantedListItem("asdf")
            self.assertEqual("asdf", i.get_title())
            i.set_title("qwer")
            self.assertEqual("qwer", i.get_title())

        def testSetStatus(self):
            i = WantedListItem("zxcv")
            self.assertEqual(False, i.get_status())
            i.set_status(True)
            self.assertEqual(True, i.get_status())

        def testHasNamedProperties(self):
            i = WantedListItem("plapla")
            self.assertEqual("plapla", i.property("title"))
            self.assertEqual(False, i.property("status"))

    unittest.main()
