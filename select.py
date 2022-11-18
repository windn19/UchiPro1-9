from PyQt5.QtSql import QSqlDatabase, QSqlQuery


con = QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('contacts.db')
if not con.open():
    print(con.lastError().databaseText())
    exit(10)

query = QSqlQuery()
query.exec('select name, job, email from contacts')

while query.next():
    print([query.value(i) for i in range(3)])
