import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QComboBox, QApplication


class Combodemo(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        layout = QHBoxLayout()
        self.cb = QComboBox()
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(self.selectionchange)

        layout.addWidget(self.cb)
        self.setLayout(layout)
        self.setWindowTitle("combo box demo")

    def selectionchange(self, i):
        print("Items in the list are :")

        for count in range(self.cb.count()):
            print(self.cb.itemText(count))
        print("Current index", i, "selection changed ", self.cb.currentText())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Combodemo()
    ex.show()
    sys.exit(app.exec_())
