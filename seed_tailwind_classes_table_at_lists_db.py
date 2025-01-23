import sqlite3

# Path to the text file
file_path = 'tailwind_classes.txt'

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('lists.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS tailwind_classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT NOT NULL UNIQUE
)
''')

# Read the text file and insert data
with open(file_path, 'r') as file:
    classes = [line.strip() for line in file.readlines() if line.strip()]

# Insert each class into the database
for class_name in classes:
    try:
        cursor.execute('INSERT INTO tailwind_classes (class_name) VALUES (?)', (class_name,))
    except sqlite3.IntegrityError:
        # Skip duplicates
        print(f"Class '{class_name}' already exists, skipping.")

# Commit and close the connection
conn.commit()
conn.close()
