+import mysql.connector;
+con = mysql.connector.connect(host ="localhost", user= "root",database="py",password="2429")
+cur = con.cursor()
+supplierId = input("Enter supplier Id> ")
+supplierName = input("Enter supplier Name> ")
+suppliercontactno = input("Enter supplier Contac No> ")
+supplieremailId = input("Enter supplier Email Id> ")
+
+bindVar = {'paramsupid':supplierId,'paramsupname':supplierName,'paramsupcontactno':suppliercontactno,'paramemail':supplieremailId}
+
+cur.execute("INSERT INTO supplier VALUES(%(paramsupid)s,%(paramsupname)s,%(paramsupcontactno)s,%(paramemail)s)""",bindVar)
+
+con.commit()
+con.close()
