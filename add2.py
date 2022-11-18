from faker import Faker
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


fake = Faker('ru-Ru')
con = QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('contacts.db')
if not con.open():
    print(con.lastError().databaseText())
    exit(1)

insertDataQuery = QSqlQuery()
insertDataQuery.prepare("""
    insert into contacts (
        name,
        job,
        email)
    values (?, ?, ?)
""")

data = [(fake.name(), fake.job(), fake.email()) for _ in range(5)]

for name, job, email in data:
    insertDataQuery.addBindValue(name)
    insertDataQuery.addBindValue(job)
    insertDataQuery.addBindValue(email)
    insertDataQuery.exec()

insertDataQuery.finish()
con.close()