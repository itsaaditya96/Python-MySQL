import mysql.connector;
connection = mysql.connector.connect(host='localhost',database='python_mysql',user='root',password='aaditya')
cur = connection.cursor();
sql = """CREATE TABLE supplier(
        supplierid VARCHAR(6) PRIMARY KEY,
        suppliername VARCHAR(30),
        suppliercontactno VARCHAR(15),
        supplieremailid VARCHAR(30)
        );"""
cur.execute(sql)
connection.commit()
connection.close()
