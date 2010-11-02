#include <QtCore/QString>
#include <QtTest/QtTest>
#include <QtCore/QCoreApplication>

class WantedListModelTest : public QObject
{
    Q_OBJECT

public:
    WantedListModelTest();

private Q_SLOTS:
    void initTestCase();
    void cleanupTestCase();
    void rowCount();
    void rowCount_data();
};

WantedListModelTest::WantedListModelTest()
{
}

void WantedListModelTest::initTestCase()
{
}

void WantedListModelTest::cleanupTestCase()
{
}

void WantedListModelTest::rowCount()
{
    QFETCH(QString, data);
    QVERIFY2(true, "Failure");
}

void WantedListModelTest::rowCount_data()
{
    QTest::addColumn<QString>("data");
    QTest::newRow("0") << QString();
}

DECLARE_TEST(WantedListModelTest);

#include "tst_wantedlistmodeltest.moc"
