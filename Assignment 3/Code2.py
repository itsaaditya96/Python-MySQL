import mysql.connector;
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
sql = """Select * from supplier;"""
cur.execute(sql)
print(cur.fetchone())
connection.close()
