import mysql.connector;
connection = mysql.connector.connect(host='localhost',database='python_mysql',user='root',password='aaditya')
cur = connection.cursor();
sql = """CREATE TABLE item(
        itemcode VARCHAR(6) PRIMARY KEY,
        itemtype VARCHAR(30),
        description VARCHAR(100) NOT NULL,
        price int,
        reorderlevel int,
        quantityonhand int,
        category char(1)
        );"""
cur.execute(sql)
connection.commit()
connection.close()
