#include "yoko.h"
#include "ui_yoko.h"

Yoko::Yoko(QWidget *parent)
    : QDockWidget(parent)
    , ui(new Ui::Yoko)
{
    ui->setupUi(this);
}

Yoko::~Yoko()
{
    delete ui;
}
