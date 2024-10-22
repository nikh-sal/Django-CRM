import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'admin123',
	)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE nikco")

print("All Done")