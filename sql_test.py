import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()    # Responsible for executing a query

create_table = "CREATE TABLE test (id int, username str,email str )"
cursor.execute(create_table)

user = (1, 'testuser', 'testuser@gmail.com')
insert_query = "INSERT INTO test VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

test = [
    (1, 'testuser', 'testuser@gmail.com'),
]
cursor.executemany(insert_query, test)

select_query = "SELECT * FROM test"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
