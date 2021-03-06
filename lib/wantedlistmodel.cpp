#include "wantedlistmodel.h"

WantedListModel::WantedListModel(QObject *parent) :
    QAbstractListModel(parent)
{
}

WantedListModel::~WantedListModel()
{

}

int WantedListModel::rowCount(const QModelIndex &/*parent*/) const
{
    return 5;
}

QModelIndex WantedListModel::parent(const QModelIndex &child) const
{
    return QModelIndex();
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
    if (section == 0 && role == Qt::DisplayRole && orientation == Qt::Vertical) {
        return QVariant("Terppa");
    }
    return QVariant();
}
