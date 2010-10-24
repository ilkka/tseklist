#!/usr/bin/env python
import sys, os
from PySide import QtGui, QtCore, QtDeclarative
from enum import Enum

class QmlApplicationViewer(QtDeclarative.QDeclarativeView):
    Orientation = Enum('LockPortrait', 'LockLandscape', 'Auto')

    def __init__(self, parent=None):
        QtDeclarative.QDeclarativeView.__init__(self)
        QtCore.QObject.connect(self.engine(), QtCore.SIGNAL('quit()'), self, QtCore.SLOT('close()'))
        self.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
        self.mainQmlFile = ""

    def setMainQmlFile(self, filename):
        self.mainQmlFile = QmlApplicationViewer._adjustPath(filename)
        self.setSource(QtCore.QUrl.fromLocalFile(self.mainQmlFile))

    def addImportPath(self,  path):
        pass

    def setOrientation(self, orientation):
        pass

    @classmethod
    def _adjustPath(cls, path):
        pathInShareDir = os.path.join(
            QtCore.QCoreApplication.applicationDirPath(),
            "/../share/",
            QtCore.QFileInfo(QtCore.QCoreApplication.applicationFilePath()).fileName(),
            path)
        if QtCore.QFileInfo(pathInShareDir).exists():
            return pathInShareDir
        return path

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #view = QtDeclarative.QDeclarativeView()
    #view.setSource(QtCore.QUrl('qml/qmlshopper/main.qml'))
    #view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
    view = QmlApplicationViewer()
    view.setMainQmlFile('qml/qmlshopper/main.qml')
    
    view.show()
    sys.exit(app.exec_())
