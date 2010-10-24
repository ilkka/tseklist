#ifndef WANTEDLISTMODEL_H
#define WANTEDLISTMODEL_H

#include <QAbstractListModel>

class WantedListModel : public QAbstractListModel
{
    Q_OBJECT
public:
    explicit WantedListModel(QObject *parent = 0);
    int rowCount(const QModelIndex &parent) const;
    QVariant data(const QModelIndex &index, int role) const;
    QVariant headerData(int section, Qt::Orientation orientation, int role) const;

signals:

public slots:

};

#endif // WANTEDLISTMODEL_H
