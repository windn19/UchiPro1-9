#!/usr/bin/python

import sys
from PyQt5.QtWidgets import (QListWidget, QWidget, QMessageBox,
                             QApplication, QVBoxLayout, QPushButton, QHBoxLayout)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout()

        self.listWidget = QListWidget(self)

        self.listWidget.addItems(['sparrow', 'robin', 'crow', 'raven',
                                  'woopecker', 'hummingbird'])
        self.listWidget.itemDoubleClicked.connect(self.onClicked)

        clearBtn = QPushButton('Clear', self)
        clearBtn.clicked.connect(self.onClearClicked)

        countBtn = QPushButton('Count', self)
        countBtn.clicked.connect(self.onCountClicked)

        vbox.addWidget(self.listWidget)
        hbox.addWidget(clearBtn)
        hbox.addWidget(countBtn)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(400, 300, 350, 250)
        self.setWindowTitle('QListWidget')
        self.show()

    def onClearClicked(self):
        self.listWidget.clear()

    def onCountClicked(self):
        QMessageBox.information(self, "Info",
                                f'# of birds {self.listWidget.count()}')

    def onClicked(self, item):
        QMessageBox.information(self, "Info", item.text())


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
