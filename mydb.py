import mysql.connector



dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'aatroxking2004',

    
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE hazadata1")

print("All Done")