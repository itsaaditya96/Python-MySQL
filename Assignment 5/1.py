import mysql.connector
connection = mysql.connector.connect(host='localhost',database='python_mysql',user='root',password='aaditya')
cur = connection.cursor();
supplierId = input("Enter Supplier ID > ")
supplierName = input("Enter Supplier Name > ")
suppliercontactno = input("Enter Supplier Contact No. > ")
supplieremailid = input("Enter Supplier Email Id > ")

cur.execute("""INSERT INTO supplier VALUES
                (%s,%s,%s,%s)""",(supplierId,supplierName,suppliercontactno,supplieremailid))
connection.commit()
connection.close()
