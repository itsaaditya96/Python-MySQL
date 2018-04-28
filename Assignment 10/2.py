import mysql.connector
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
cur.execute("""SELECT * FROM supplier ORDER BY supplierId""")

for row in cur.fetchmany():
    print(row)
print(cur.arraysize)
cur.arraysize = 5
print(cur.rowcount)
for row in cur.fetchmany():
    print(row)
connection.close()
