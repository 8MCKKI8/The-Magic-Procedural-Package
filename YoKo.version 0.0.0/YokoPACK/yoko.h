#ifndef YOKO_H
#define YOKO_H

#include <QDockWidget>

namespace Ui {
class Yoko;
}

class Yoko : public QDockWidget
{
    Q_OBJECT

public:
    explicit Yoko(QWidget *parent = nullptr);
    ~Yoko();

private:
    Ui::Yoko *ui;
};

#endif // YOKO_H
