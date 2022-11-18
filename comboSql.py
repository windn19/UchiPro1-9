import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QComboBox, QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


class Combodemo1(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.cb = QComboBox()
        self.cb.addItems(self.get_items())
        self.cb.currentIndexChanged.connect(self.selectionchange)

        layout.addWidget(self.cb)
        self.setLayout(layout)
        self.setWindowTitle("Combo box demo1")

    def selectionchange(self, i):
        print("Items in the list are :")

        for count in range(self.cb.count()):
            print(self.cb.itemText(count))
        print("Current index", i, "selection changed ", self.cb.currentText())

    def get_items(self):
        con = QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName('contacts.db')
        if not con.open():
            print(con.lastError().databaseText())
            exit(10)
        query = QSqlQuery()
        query.exec('select job from contacts')
        result = []
        while query.next():
            result.append(query.value(0))
        query.finish()
        con.close()
        return sorted(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Combodemo1()
    ex.show()
    sys.exit(app.exec_())
