# Add more folders to ship with the application, here
folder_01.source = qml/qmlshopper
folder_01.target = qml
DEPLOYMENTFOLDERS = folder_01

# Additional import path used to resolve Qml modules in Creator's code model
QML_IMPORT_PATH = /usr/lib/qt4/imports

# Avoid auto screen rotation
#DEFINES += ORIENTATIONLOCK

# Needs to be defined for Symbian
#DEFINES += NETWORKACCESS

symbian:TARGET.UID3 = 0xE50FD061

# Define QMLJSDEBUGGER to enable basic debugging (setting breakpoints etc)
# Define QMLOBSERVER for advanced features (requires experimental QmlInspector plugin!)
#DEFINES += QMLJSDEBUGGER
#DEFINES += QMLOBSERVER

# The .cpp file which was generated for your project. Feel free to hack it.
SOURCES += main.cpp \
    lib/wantedlistmodel.cpp

# Please do not modify the following two lines. Required for deployment.
include(qmlapplicationviewer/qmlapplicationviewer.pri)
qtcAddDeployment()

HEADERS += \
    lib/wantedlistmodel.h
