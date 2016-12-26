import sqlite3

conn = sqlite3.connect(r'database.db')
conn.execute('CREATE TABLE info (sid TEXT,name TEXT, addr TEXT, city TEXT, pin TEXT)')
conn.close()