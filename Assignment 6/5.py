import mysql.connector
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
sql = """SELECT description,price 
        FROM item WHERE description LIKE '%Hard disk'"""
cur.execute(sql)
for row in cur.fetchall():
    print(row)
connection.commit()
connection.close()
