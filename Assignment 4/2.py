import mysql.connector;
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
sql = """SELECT suppliername, suppliercontactno FROM supplier WHERE supplierid = 'S1002';"""
cur.execute(sql)
data = cur.fetchall();
for row in data:
    print(row)
connection.commit()
connection.close()
