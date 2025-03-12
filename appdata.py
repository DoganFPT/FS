import sqlite3

connection = sqlite3.connect("appdata.db")
cursor=connection.cursor()




cursor.execute("""""
	CREATE TABLE IF NOT EXISTS players (
		id INTEGER PRIMARY KEY,
		name TEXT,
		threes INTEGER,
        twos INTEGER,
        points INTEGER
	)
""""")

cursor.execute("INSERT INTO players (name, age) VALUES (?,?)",("Steph",35))

connection.commit()


connection.close()
