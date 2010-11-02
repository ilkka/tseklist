#include <QtTest>
#include "common/AutoTest.h"

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

}

void WantedListItemTest::testSetStatus()
{

}

DECLARE_TEST(WantedListItemTest)

#include "tst_wantedlistitemtest.moc"
#include "../../moc_wantedlistitem.cpp"
