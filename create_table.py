import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery


con = QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('contacts.db')

if not con.open():
    print(f"Database Error: {con.lastError().databaseText()}")
    sys.exit(1)

createTableQuery = QSqlQuery()
print(createTableQuery.exec(
    """
    create table contacts (
        id integer primary key autoincrement,
        name varchar(40) not null,
        job varchar(50),
        email varchar(40) not null
        );
    """))
print(con.tables())
createTableQuery.finish()
con.close()
