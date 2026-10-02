import sqlite3

def create_table():
    connection = sqlite3.connect("meditrack.db")  
    try:
        cursor = connection.cursor()                   
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
        )
    """)
        connection.commit()
    finally:
        connection.close()

def add_patient(name, age):
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO patients (name, age) VALUES (?, ?)", (name, age))
        connection.commit()
    finally:
        connection.close()

def view_patients():
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM patients")
        rows = cursor.fetchall()
    finally:
        connection.close()
    return rows

def search_patient(name):
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM patients WHERE name = ?", (name,))
        rows = cursor.fetchall()
    finally:  
        connection.close()
    return rows


def update_patient_age(patient_id, new_age):
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE patients SET age = ? WHERE id = ?", (patient_id, new_age))
        connection.commit()
    finally:
        connection.close()

def delete_patient(patient_id):
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("DELETE FROM patients WHERE id = ?", (patient_id,))
        connection.commit()
    finally:
        connection.close()
    

# create_table()
# add_patient("kate", 19)
# print(view_patients())
# delete_patient(2)
# print(view_patients())

def create_doctors_table():
    connection = sqlite3.connect("meditrack.db") 
    try: 
        cursor = connection.cursor()                   
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialty TEXT NOT NULL
        )
    """)
        connection.commit()
    finally:
        connection.close()

def add_doctor(name, specialty):
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO doctors (name, specialty) VALUES (?, ?)", (name, specialty))
        connection.commit()
    finally:
        connection.close()

def view_doctors():
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM doctors")
        rows = cursor.fetchall()
    finally:
        connection.close()
    return rows
# create_doctors_table()
# add_doctor("Dr. Adeyemi", "pediatrics")
# print(view_doctors())

def create_appointments_table():
    connection = sqlite3.connect("meditrack.db") 
    try: 
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
    finally:
        connection.close()

def add_appointment(patient_id, doctor_id, appointment_date, reason):
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("INSERT INTO appointments (patient_id,  doctor_id, appointment_date, reason) VALUES (?, ?, ?, ?)", (patient_id, doctor_id, appointment_date, reason))
        connection.commit()
    finally:
        connection.close()
def view_appointments():
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM appointments")
        rows = cursor.fetchall()
    finally:
        connection.close()
    return rows

def delete_appointment(appointment_id):
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM appointments WHERE id = ?", (appointment_id,))
        connection.commit()
    finally:
        connection.close()

# create_appointments_table()
# add_appointment(1, 1, "2026-11-06 09:45", "malaria")
# try:
#     add_appointment(1, 1, "2026-11-08 11:00", "follow-up")
#     print("Appointment booked.")
# except sqlite3.IntegrityError:
#     print("Patient or doctor does not exist.")
# print(view_appointments())

def create_visits_table():
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()                   
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER NOT NULL,
        visit_date TEXT NOT NULL,
        symptoms TEXT,
        diagnosis TEXT,
        treatment TEXT,
        prescription TEXT,
        follow_up_date TEXT,
        FOREIGN KEY (patient_id) REFERENCES patients (id)
    )
    """)
        connection.commit()
    finally:
        connection.close() 

def add_visit(patient_id, visit_date, symptoms, diagnosis, treatment, prescription, follow_up_date):
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("INSERT INTO visits (patient_id, visit_date, symptoms, diagnosis, treatment, prescription, follow_up_date) VALUES (?, ?, ?, ?, ?, ?, ?)", (patient_id, visit_date, symptoms, diagnosis, treatment, prescription, follow_up_date))
        connection.commit()
    finally:
        connection.close()

def view_visit():
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM visits")
        rows = cursor.fetchall()
    finally:
        connection.close()
    return rows

def delete_visit(visit_id):
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM visits WHERE id = ?", (visit_id,))
        connection.commit()
    finally:
        connection.close()

def view_appointments_detailed():
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT appointments.id, patients.name, doctors.name, appointments.appointment_date, appointments.reason
            FROM appointments
            JOIN patients ON appointments.patient_id = patients.id
            JOIN doctors ON appointments.doctor_id = doctors.id
        """)
        rows = cursor.fetchall()
    finally:
        connection.close()
    return rows

def view_visits_detailed():
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT visits.id, patients.name, visits.visit_date, visits.symptoms,
                   visits.diagnosis, visits.treatment, visits.prescription, visits.follow_up_date
            FROM visits
            JOIN patients ON visits.patient_id = patients.id
        """)
        rows = cursor.fetchall()
    finally:
        connection.close()
    return rows

def search_doctor_by_specialty(specialty):
    connection = sqlite3.connect("meditrack.db")
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM doctors WHERE specialty = ?", (specialty,))
        rows = cursor.fetchall()
    finally:
        connection.close()
    return rows

# create_visits_table()
# add_visit(1, "2026-11-12 10:30", "malaria", "not critical", "malaria injection", "twice a day for three days", "2026-12-09 8:30")
# delete_visit(4)
# delete_visit(5)
# print(view_visit())

if __name__ == "__main__":
    create_table()
    create_doctors_table()
    create_appointments_table()
    create_visits_table()
    print(view_visit())
    