import sqlite3

conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS sample_table (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    height REAL,
                    city TEXT
                )''')

# Insert
cursor.execute('''INSERT INTO sample_table (name, age, height, city)
                  VALUES ('Alice', 25, 1.75, 'New York'),
                         ('Bob', 30, 1.80, 'Los Angeles'),
                         ('Charlie', 22, 1.70, 'Chicago'),
                         ('David', 28, 1.85, 'Houston'),
                         ('Eve', 35, 1.60, 'Miami')''')

cursor.execute('''SELECT * FROM sample_table''')
print(cursor.fetchall())

cursor.execute('''SELECT * FROM sample_table WHERE city='New York' ''')
print(cursor.fetchall())

cursor.execute('''SELECT name, city FROM sample_table''')
print(cursor.fetchall())

cursor.execute('''SELECT SUM(height) FROM sample_table''')
print(cursor.fetchone()[0])

cursor.execute('''SELECT COUNT(*) FROM sample_table''')
print(cursor.fetchone()[0])

cursor.execute('''SELECT * FROM sample_table''')
for row in cursor.fetchall():
    print(row)

# Session 12 addition
cursor.execute('''ALTER TABLE sample_table 
                  ADD COLUMN description TEXT''')

cursor.execute(''' UPDATE sample_table
                   SET description = 'Works in IT'
                   WHERE name = 'Alice' ''')

cursor.execute(''' UPDATE sample_table
                   SET description = 'Teacher'
                   WHERE name = 'Bob' ''')

cursor.execute(''' UPDATE sample_table
                   SET description = 'Doctor'
                   WHERE name = 'Charlie' ''')

cursor.execute(''' UPDATE sample_table
                   SET description = 'Engineer'
                   WHERE name = 'David' ''')

cursor.execute(''' UPDATE sample_table
                   SET description = 'Artist'
                   WHERE name = 'Eve' ''')

cursor.execute(''' UPDATE sample_table
                   SET description = 'Professional' ''')

cursor.execute('''UPDATE sample_table
                   SET description = 'Manager'
                   WHERE name = 'Alice' ''')

cursor.execute('''UPDATE sample_table
                   SET description = 'Designer'
                   WHERE name = 'Bob' ''')

cursor.execute('''DELETE FROM sample_table
                   WHERE name = 'David' ''')

cursor.execute('''SELECT * FROM sample_table''')
for row in cursor.fetchall():
    print(row)

conn.close()