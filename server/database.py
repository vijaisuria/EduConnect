import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create Users table
c.execute('''CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                verified BOOLEAN DEFAULT 0
             )''')

# Create Course table
c.execute('''CREATE TABLE IF NOT EXISTS Course (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                instructor TEXT,
                duration INTEGER,
                url TEXT
             )''')

# Create Course_Enrolled table
c.execute('''CREATE TABLE IF NOT EXISTS Course_Enrolled (
                uid INTEGER,
                cid INTEGER,
                status TEXT CHECK (status IN ('active', 'enrolled', 'completed')),
                FOREIGN KEY (uid) REFERENCES Users(id),
                FOREIGN KEY (cid) REFERENCES Course(id),
                PRIMARY KEY (uid, cid)
             )''')

conn.commit()
conn.close()
