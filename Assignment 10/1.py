import mysql.connector
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
cur.execute("""SELECT * FROM supplier ORDER BY supplierId""")
print(cur.rowcount)
for row in cur.fetchall():
    print(row)
print(cur.rowcount)
connection.close()
