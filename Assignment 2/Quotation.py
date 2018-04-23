import mysql.connector;
connection = mysql.connector.connect(host='localhost',database='python_mysql',user='root',password='aaditya')
cur = connection.cursor();
sql = """CREATE TABLE quotation(
        quotationid VARCHAR(6) PRIMARY KEY,
        supplierid VARCHAR(6),
        itemcode VARCHAR(10),
        quotedprice INT,
        quotationdate DATE,
        quotationstatus VARCHAR(10)
    );"""
cur.execute(sql)
connection.commit()
connection.close()
