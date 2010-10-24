#!/usr/bin/env python
import sys, os
from PySide import QtGui, QtCore, QtDeclarative
from lib.enum import Enum
from lib.viewer import QmlApplicationViewer

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #view = QtDeclarative.QDeclarativeView()
    #view.setSource(QtCore.QUrl('qml/qmlshopper/main.qml'))
    #view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
    view = QmlApplicationViewer()
    view.setMainQmlFile('qml/qmlshopper/main.qml')
    
    view.show()
    sys.exit(app.exec_())
