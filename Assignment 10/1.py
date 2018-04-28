import mysql.connector

connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
cur.execute("""SELECT itemcode,AVG(qtyavailable) FROM retailstock WHERE qtyavailable < 75""")
cur.arraysize = 3
for row in cur.fetchmany():
    print(row)
connection.close()
