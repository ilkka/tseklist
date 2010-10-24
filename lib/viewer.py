# QML App viewer class
# Based on Qt Creator -created QmlApplicationViewer C++ class
# Licensed under the LGPL
from PySide import QtGui, QtCore, QtDeclarative
from enum import Enum
import os

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
        self.engine().addImportPath(QmlApplicationViewer._adjustPath(path))

    def setOrientation(self, orientation):
        try:
            from PySide import QtMaemo5
            if orientation == Orientation.LockPortrait:
                attr = QtMaemo5.Qt.WA_Maemo5PortraitOrientation
            elif orientation == Orientation.LockLandscape:
                attr = QtMaemo5.Qt.WA_Maemo5LandscapeOrientation
            else:
                attr = QtMaemo5.Qt.WA_Maemo5AutoOrientation
            self.setAttribute(attr, True)
        except ImportError:
            pass # We're not on Maemo 5

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

