#include <QtGui/QApplication>
#include "qmlapplicationviewer.h"
#include <QObjectList>
#include "lib/wantedlistitem.h"
#include <QDeclarativeContext>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QObjectList* o = new QObjectList();
    o->append(new WantedListItem());
    o->append(new WantedListItem());

    QmlApplicationViewer viewer;

    viewer.rootContext()->setContextProperty("wantedlist", o);

    viewer.setOrientation(QmlApplicationViewer::Auto);
    viewer.setMainQmlFile(QLatin1String("qml/qmlshopper/main.qml"));
    viewer.show();

    return app.exec();
}
