import mysql.connector;
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
sql = """SELECT supplierid, suppliername 
            FROM supplier WHERE 
            suppliername LIKE '_i%';"""
cur.execute(sql)
data = cur.fetchall();
for row in data:
    print(row)
connection.commit()
connection.close()
