#!/usr/bin/env python
import sys, os, logging
from PySide import QtGui, QtCore, QtDeclarative
from lib.viewer import QmlApplicationViewer
from lib.model import WantedListItem

logging.basicConfig(level=logging.DEBUG)

items = []

def addThing(thing):
    logging.debug("Add thing \"%s\"" % thing)
    items.append(WantedListItem(thing))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    view = QmlApplicationViewer()

    view.rootContext().setContextProperty("wantedlist", items)

    view.setMainQmlFile('qml/qmlshopper/main.qml')

    root = view.rootObject()
    QtCore.QObject.connect(root, QtCore.SIGNAL('addThing(QString)'),
                           addThing)

    view.show()
    sys.exit(app.exec_())
