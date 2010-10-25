#!/usr/bin/env python
import sys, os
from PySide import QtGui, QtCore, QtDeclarative
from lib.viewer import QmlApplicationViewer
from lib.model import WantedListModel

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    view = QmlApplicationViewer()

    model = WantedListModel()
    view.rootContext().setContextProperty("wantedlist", model)

    view.setMainQmlFile('qml/qmlshopper/main.qml')

    root = view.rootObject()
    QtCore.QObject.connect(root, QtCore.SIGNAL('addThing(QString)'),
                           model.addThing)

    view.show()
    sys.exit(app.exec_())
