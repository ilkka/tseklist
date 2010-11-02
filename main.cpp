#include <QtGui/QApplication>
#include "qmlapplicationviewer.h"
#include <QObjectList>
#include "lib/wantedlistitem.h"
#include <QDeclarativeContext>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QObjectList o;
    o.append(new WantedListItem("eka"));
    o.append(new WantedListItem("toka"));

    QmlApplicationViewer viewer;

    viewer.rootContext()->setContextProperty("wantedlist", QVariant::fromValue(o));

    viewer.setOrientation(QmlApplicationViewer::Auto);
    viewer.setMainQmlFile(QLatin1String("qml/qmlshopper/main.qml"));
    viewer.show();

    return app.exec();
}
