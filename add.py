from faker import Faker
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


fake = Faker(['ru-Ru'])

con = QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('contacts.db')
if not con.open():
    print(con.lastError().databaseText())
    exit(1)

name = fake.name()
job = fake.job()
email = fake.email()

query = QSqlQuery()
query.exec(f"""
    insert into contacts (name, job, email) values ('{name}', '{job}', '{email}');
""")

query.finish()
con.close()
