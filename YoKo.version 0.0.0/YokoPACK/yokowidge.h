#ifndef YOKOWIDGE_H
#define YOKOWIDGE_H

#include <QDockWidget>

namespace Ui {
class YokoWidge;
}

class YokoWidge : public QDockWidget
{
    Q_OBJECT

public:
    explicit YokoWidge(QWidget *parent = nullptr);
    ~YokoWidge();

private:
    Ui::YokoWidge *ui;
};

#endif // YOKOWIDGE_H
