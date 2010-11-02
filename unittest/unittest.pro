TEMPLATE = app

QT       += testlib
QT       -= gui

TARGET = unittests
CONFIG   += console
CONFIG   -= app_bundle

SOURCES += common/testrunner.cpp
DEFINES += SRCDIR=\\\"$$PWD/\\\"

INCLUDEPATH += -I../lib -I.
HEADERS += common/AutoTest.h

include(wantedlistmodel/test_wantedlistmodel.pri)
include(wantedlistitem/test_wantedlistitem.pri)
