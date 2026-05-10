#include "yokowidge.h"
#include "ui_yokowidge.h"

YokoWidge::YokoWidge(QWidget *parent)
    : QDockWidget(parent)
    , ui(new Ui::YokoWidge)
{
    ui->setupUi(this);
}

YokoWidge::~YokoWidge()
{
    delete ui;
}
