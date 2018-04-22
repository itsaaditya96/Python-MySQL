import mysql.connector;
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
print(cur)
connection.close()
