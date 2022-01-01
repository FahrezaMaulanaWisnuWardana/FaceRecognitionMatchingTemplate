
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="face-recognition"
)
mycursor = db.cursor()

mycursor.execute("INSERT INTO absens(name) VALUES('test')")
db.commit()
# mycursor.execute()
