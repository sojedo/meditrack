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


def update_patient_age(patient_id, new_age):
    connection = sqlite3.connect("meditrack.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE patients SET age = ? WHERE id = ?", (patient_id, new_age))
    connection.commit()
    connection.close()

def delete_patient(patient_id):
    connection = sqlite3.connect("meditrack.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM patients WHERE id = ?", (patient_id,))
    connection.commit()
    connection.close()

# create_table()
# # add_patient("kate", 19)
# print(view_patients())
# delete_patient(2)
# print(view_patients())

def create_doctors_table():
    connection = sqlite3.connect("meditrack.db")  
    cursor = connection.cursor()                   
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialty TEXT NOT NULL
)
""")
    connection.commit()
    connection.close()

def add_doctor(name, specialty):
    connection = sqlite3.connect("meditrack.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO doctors (name, specialty) VALUES (?, ?)", (name, specialty))
    connection.commit()
    connection.close()

def view_doctors():
    connection = sqlite3.connect("meditrack.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM doctors")
    rows = cursor.fetchall()
    connection.close()
    return rows
# create_doctors_table()
# add_doctor("Dr. Adeyemi", "pediatrics")
# print(view_doctors())

def create_appointments_table():
    connection = sqlite3.connect("meditrack.db")  
    cursor = connection.cursor()                   
    cursor.execute ("""
    CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    appointment_date TEXT NOT NULL,
    reason TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients (id),
    FOREIGN KEY (doctor_id) REFERENCES doctors (id)
)
""")
    connection.commit()
    connection.close()

def add_appointment(patient_id, doctor_id, appointment_date, reason):
    connection = sqlite3.connect("meditrack.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("INSERT INTO appointments (patient_id,  doctor_id, appointment_date, reason) VALUES (?, ?, ?, ?)", (patient_id, doctor_id, appointment_date, reason))
    connection.commit()
    connection.close()

def view_appointments():
    connection = sqlite3.connect("meditrack.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM appointments")
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete_appointment(appointment_id):
    connection = sqlite3.connect("meditrack.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM appointments WHERE id = ?", (patient_id,))
    connection.commit()
    connection.close()

create_appointments_table()
# add_appointment(1, 1, "2026-11-06 09:45", "malaria")
add_appointment(99, 1, "2026-11-07 10:00", "checkup")
delete_appointment(2)
print(view_appointments())