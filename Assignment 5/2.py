import mysql.connector
connection = mysql.connector.connect(host='localhost',database='python_mysql',user='root',password='aaditya')
cur = connection.cursor();
supplierId = input("Enter Supplier ID > ")
supplierName = input("Enter Supplier Name > ")
suppliercontactno = input("Enter Supplier Contact No. > ")
supplieremailid = input("Enter Supplier Email Id > ")
bindVar={'paramsupID':supplierId,'paramsupName':supplierName,'paramsupcontact':suppliercontactno,'paramsupemail':supplieremailid}
print(bindVar.get('paramsupID'))
cur.execute("""INSERT INTO supplier VALUES(%(paramsupID)s,%(paramsupName)s,%(paramsupcontact)s,%(paramsupemail)s)""",bindVar)
connection.commit()
connection.close()
