#include "wantedlistmodel.h"

WantedListModel::WantedListModel(QObject *parent) :
    QAbstractListModel(parent)
{
}

int WantedListModel::rowCount(const QModelIndex &parent) const
{
    return 5;
}

QVariant WantedListModel::data(const QModelIndex &index, int role) const
{
    if (index.isValid() && role == Qt::DisplayRole) {
        return QVariant("Moro");
    }
    return QVariant();
}

QVariant WantedListModel::headerData(int section, Qt::Orientation orientation, int role) const
{
    if (index.isValid() && role == Qt::DisplayRole) {
        return QVariant("Terppa");
    }
    return QVariant();
}
