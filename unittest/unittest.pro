TEMPLATE = app

QT       += testlib
QT       -= gui

TARGET = tst_wantedlistmodeltest
CONFIG   += console
CONFIG   -= app_bundle

SOURCES += common/testrunner.cpp
DEFINES += SRCDIR=\\\"$$PWD/\\\"

INCLUDEPATH += -I../lib
HEADERS += common/AutoTest.h

include(wantedlistmodel/test_wantedlistmodel.pri)
include(wantedlistitem/test_wantedlistitem.pri)
