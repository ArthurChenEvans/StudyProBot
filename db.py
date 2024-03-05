import sqlite3

def setup_database():
	con = sqlite3.connect("discord.db")
	cur = con.cursor()

	cur.execute("""CREATE TABLE IF NOT EXISTS users("id INTEGER PRIMARY KEY, username TEXT NOT NULL")""")

	con.commit()
	con.close()

