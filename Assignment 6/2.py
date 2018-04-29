import mysql.connector
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
sql = """UPDATE supplier SET
        supplieremailid = 'john@ebats.com'
        where supplierid='S1009'"""
sql1 = """UPDATE supplier SET 
        suppliercontactno = '879-456-398'
        where supplierid='S1009'"""
cur.execute(sql)
cur.execute(sql1)
connection.commit()
connection.close()
