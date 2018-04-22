# Python-MySQL
Performing Database operations on MySQL using Python

## Assignment 1
### Step 1

To Start, we need to install the driver mysql-python connector, download it from link below: -
https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-8.0.11.zip

After Downloading, Extract the zip

Enter the following command to windows command line
```
cd <extracter zip path>\
python setup.py install
```

Note = You'll need to add python to *System Variables under *Environmental Variables to execute installation command

### Step 2
#### Use below command to import MySQL Connector
```
import mysql.connector;
```

### Step 3
#### Creating cursor for executing commands
```
connection = mysql.connector.connect(host='localhost',database='rdbms',user='root',password='')
cur = cur = connection.cursor();
```
