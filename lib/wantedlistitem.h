#ifndef WANTEDLISTITEM_H
#define WANTEDLISTITEM_H

#include <QObject>

class WantedListItem : public QObject
{
    Q_OBJECT
    Q_PROPERTY(QString title READ get_title WRITE set_title NOTIFY titleChanged)
    Q_PROPERTY(int status READ get_status WRITE set_status NOTIFY statusChanged)
public:
    explicit WantedListItem(const QString& title, QObject *parent = 0);

    QString get_title() const {
        return m_title;
    }
    int get_status() const {
        return m_status;
    }

signals:
    void titleChanged();
    void statusChanged();

public slots:
    void set_title(const QString& title) {
        m_title = title;
    }
    void set_status(int status) {
        m_status = status;
    }

private:
    QString m_title;
    int m_status;
};

#endif // WANTEDLISTITEM_H
