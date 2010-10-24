#ifndef WANTEDLISTMODEL_H
#define WANTEDLISTMODEL_H

#include <QAbstractListModel>

class WantedListModel : public QAbstractListModel
{
    Q_OBJECT
public:
    explicit WantedListModel(QObject *parent = 0);
    virtual ~WantedListModel();
    int rowCount(const QModelIndex &parent = QModelIndex()) const;
    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const;
    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const;
    QModelIndex parent(const QModelIndex &child) const;

signals:

public slots:

};

#endif // WANTEDLISTMODEL_H
