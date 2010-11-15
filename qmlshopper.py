#!/usr/bin/env python
import sys, os, logging
from PySide import QtGui, QtCore, QtDeclarative
from lib.viewer import QmlApplicationViewer
from lib.model import WantedListItem, WantedListModel

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    view = QmlApplicationViewer()

    items = WantedListModel()
    view.rootContext().setContextProperty("wantedlist", items)

    view.setMainQmlFile('qml/qmlshopper/main.qml')

    root = view.rootObject()
    QtCore.QObject.connect(root, QtCore.SIGNAL('addThing(QString)'),
                           items.addThing)

    view.show()
    sys.exit(app.exec_())
