import sqlite3

def setup_database():
    con = sqlite3.connect("discord.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY, username TEXT NOT NULL)")

    cur.execute("""CREATE TABLE IF NOT EXISTS free_recall(
        id INT PRIMARY KEY, 
        user_id INT, 
        prompt TEXT NOT NULL, 
        source TEXT NOT NULL, 
        tag TEXT, 
        creation_date DATETIME NOT NULL, 
        days_till_next_recall INTEGER NOT NULL, 
        next_recall_date DATETIME NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id))""")

    con.commit()
    con.close()


def insert_profile_into_database(id, username):
    try:
        con = sqlite3.connect("discord.db")
        cur = con.cursor()

        cur.execute("""SELECT id FROM users WHERE id = ?""", (id,))
        user_exists = cur.fetchone()

        if user_exists:
            return False
        else:
            cur.execute("""INSERT INTO users (id, username) VALUES(?, ?)""", (id, username))
            con.commit()
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        if con:
            con.close()