#include <QtTest>
#include "common/AutoTest.h"
#include "lib/wantedlistitem.h"

class WantedListItemTest : public QObject
{
    Q_OBJECT
public:
    WantedListItemTest();

private Q_SLOTS:
    void testSetTitle();
    void testSetStatus();
};

WantedListItemTest::WantedListItemTest()
{
}

void WantedListItemTest::testSetTitle()
{
    i = WantedListItem();
    i.set_title("moro");
    QCOMPARE("moro", i.get_title());
    i.set_title("tere");
    QCOMPARE("tere", i.get_title());
}

void WantedListItemTest::testSetStatus()
{
    i = WantedListItem();
    i.set_status(0);
    QCOMPARE(0, i.get_status());
    i.set_status(1);
    QCOMPARE(1, i.get_status());
}

DECLARE_TEST(WantedListItemTest)

#include "tst_wantedlistitemtest.moc"
#include "../moc_wantedlistitem.cpp"
