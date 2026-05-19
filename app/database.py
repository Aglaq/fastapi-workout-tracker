import sqlite3

connection = sqlite3.connect("workouts.db", check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            duration_min INTEGER,
            calories INTEGER,
            date TEXT
            )
            """)

connection.commit()