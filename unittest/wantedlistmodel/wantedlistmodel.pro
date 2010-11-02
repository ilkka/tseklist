#-------------------------------------------------
#
# Project created by QtCreator 2010-10-20T22:30:17
#
#-------------------------------------------------

QT       += testlib

QT       -= gui

TARGET = tst_wantedlistmodeltest
CONFIG   += console
CONFIG   -= app_bundle

TEMPLATE = app


SOURCES += tst_wantedlistmodeltest.cpp \
    ../common/testrunner.cpp
DEFINES += SRCDIR=\\\"$$PWD/\\\"

INCLUDEPATH += -I../../lib
SOURCES += ../../lib/wantedlistmodel.cpp
HEADERS += ../common/AutoTest.h
