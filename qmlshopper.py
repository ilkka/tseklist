#!/usr/bin/env python
import sys, os, logging
from PySide import QtGui, QtCore, QtDeclarative
from lib.viewer import QmlApplicationViewer
from lib.model import WantedListItem

logging.basicConfig(level=logging.DEBUG)

def addThing(thing):
    logging.debug("Would add thing \"%s\"" % thing)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    view = QmlApplicationViewer()

    items = [WantedListItem('This'), WantedListItem('That'), WantedListITem('Whatnot')]
    view.rootContext().setContextProperty("wantedlist", items)

    view.setMainQmlFile('qml/qmlshopper/main.qml')

    root = view.rootObject()
    QtCore.QObject.connect(root, QtCore.SIGNAL('addThing(QString)'),
                           addThing)

    view.show()
    sys.exit(app.exec_())
