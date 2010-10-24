#!/usr/bin/env python
import sys, oa
from PySide import QtGui, QtCore, QtDeclarative

# Enums are copyright 2005 Zoran Isailovski
# from http://code.activestate.com/recipes/413486-first-class-enums-in-python/
def Enum(*names):
   ##assert names, "Empty enums are not supported" # <- Don't like empty enums? Uncomment!

   class EnumClass(object):
      __slots__ = names
      def __iter__(self):        return iter(constants)
      def __len__(self):         return len(constants)
      def __getitem__(self, i):  return constants[i]
      def __repr__(self):        return 'Enum' + str(names)
      def __str__(self):         return 'enum ' + str(constants)

   class EnumValue(object):
      __slots__ = ('__value')
      def __init__(self, value): self.__value = value
      Value = property(lambda self: self.__value)
      EnumType = property(lambda self: EnumType)
      def __hash__(self):        return hash(self.__value)
      def __cmp__(self, other):
         # C fans might want to remove the following assertion
         # to make all enums comparable by ordinal value {;))
         assert self.EnumType is other.EnumType, "Only values from the same enum are comparable"
         return cmp(self.__value, other.__value)
      def __invert__(self):      return constants[maximum - self.__value]
      def __nonzero__(self):     return bool(self.__value)
      def __repr__(self):        return str(names[self.__value])

   maximum = len(names) - 1
   constants = [None] * len(names)
   for i, each in enumerate(names):
      val = EnumValue(i)
      setattr(EnumClass, each, val)
      constants[i] = val
   constants = tuple(constants)
   EnumType = EnumClass()
   return EnumType

# if __name__ == '__main__':
#    print '\n*** Enum Demo ***'
#    print '--- Days of week ---'
#    Days = Enum('Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su')
#    print Days
#    print Days.Mo
#    print Days.Fr
#    print Days.Mo < Days.Fr
#    print list(Days)
#    for each in Days:
#       print 'Day:', each
#    print '--- Yes/No ---'
#    Confirmation = Enum('No', 'Yes')
#    answer = Confirmation.No
#    print 'Your answer is not', ~answer

class QmlApplicationViewer(QtDeclarative.QDeclarativeView):
    Orientation = Enum('LockPortrait LockLandscape Auto')

    def __init__(self, parent=None):
        QtDeclarative.QDeclarativeView.__init__(self)
        QtCore.QObject.connect(self.engine(), QtCore.SIGNAL('quit()'), self, QtCore.SLOT('close()'))
        setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
        self.mainQmlFile = ""

    def setMainQmlFile(self, filename):
        self.mainQmlFile = QmlApplicationViewer._adjustPath(filename)

    def addImportPath(self,  path):
        pass

    def setOrientation(self, orientation):
        pass

    def _adjustPath(path):
        if not QtCore.QDir.isAbsolutePath(path):
            return os.path.join(QtCore.QCoreApplication.applicationDirPath(), "/../Resources/", path)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    view = QtDeclarative.QDeclarativeView()
    view.setSource(QtCore.QUrl('qml/qmlshopper/main.qml'))
    view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
    
    view.show()
    sys.exit(app.exec_())
