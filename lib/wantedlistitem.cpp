#include "wantedlistitem.h"

WantedListItem::WantedListItem(const QString& title, QObject *parent) :
    QObject(parent), m_title(title), m_status(0)
{
}
