import mysql.connector;
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
cur.execute("Select * from supplier;")
data = cur.fetchmany(3);
for row in data:
    print(row)
connection.close()
