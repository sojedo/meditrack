import sqlite3

def create_table():
    connection = sqlite3.connect("meditrack.db")  
    cursor = connection.cursor()                   
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")
    connection.commit()
    connection.close()

def add_patient(name, age):
    connection = sqlite3.connect("meditrack.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO patients (name, age) VALUES (?, ?)", (name, age))
    connection.commit()
    connection.close()

def view_patients():
    connection = sqlite3.connect("meditrack.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    connection.close()
    return rows

def search_patient(name):
    connection = sqlite3.connect("meditrack.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patients WHERE name = ?", (name,))
    rows = cursor.fetchall()
    connection.close()
    return rows

create_table()
add_patient("tina", 21)
result = search_patient("blue")
print(result)
