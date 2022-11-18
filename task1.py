import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery


con = QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('animals.db')

if not con.open():
    print(f"Database Error: {con.lastError().databaseText()}")
    sys.exit(1)

createTableQuery = QSqlQuery()
print(createTableQuery.exec(
    """
    create table animal (
        id integer primary key autoincrement,
        title varchar(40) not null,
        gr_an varchar(40),
        max_speed integer
        );
    """))
print(con.tables())
createTableQuery.finish()


insert_data = QSqlQuery()
insert_data.prepare("""
    insert into animal (title,
                        gr_an,
                        max_speed)
    values (?, ?, ?)
""")

data = [('cheetah', 'cats', 120), ('pronghorn', 'ungulates', 115), ('gazelle', 'ungulates', 105),
        ('antelope', 'ungulates', 90), ('lion', 'cats', 80)]

for title, group, max_speed in data:
    insert_data.addBindValue(title)
    insert_data.addBindValue(group)
    insert_data.addBindValue(max_speed)
    insert_data.exec()
insert_data.finish()
con.close()
