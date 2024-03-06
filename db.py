import sqlite3

def setup_database():
    con = sqlite3.connect("discord.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY, username TEXT NOT NULL)")

    cur.execute("""CREATE TABLE IF NOT EXISTS free_recall(
        id INTEGER PRIMARY KEY, 
        user_id INT, 
        prompt TEXT NOT NULL, 
        source_information TEXT NOT NULL, 
        tag TEXT, 
        creation_date DATETIME NOT NULL, 
        next_recall_date DATETIME NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id))""")

    cur.execute("""CREATE TABLE IF NOT EXISTS reflection(
        reflection_id INTEGER PRIMARY KEY,
        recall_id INT,
        reflection_text TEXT NOT NULL,
        accuracy INT CHECK (accuracy >= 1 AND accuracy <= 5),
        confidence INT CHECK (confidence >= 1 AND confidence <= 5),
        automaticity INT CHECK (automaticity >= 1 AND automaticity <= 5),
        previous_reflection INT,
        FOREIGN KEY(recall_id) REFERENCES free_recall(id),
        FOREIGN KEY(previous_reflection) REFERENCES reflection(reflection_id))""")

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