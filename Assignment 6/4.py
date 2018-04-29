import mysql.connector
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
sql = """UPDATE supplier SET 
        suppliercontactno = '303-537-9127'
        where supplierid='S1009'"""
cur.execute(sql)
connection.commit()
connection.close()
