import mysql.connector
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='aaditya')
cur = connection.cursor();
sql = """DELETE FROM supplier
        where supplierid='S1009'"""
cur.execute(sql)
connection.commit()
connection.close()
