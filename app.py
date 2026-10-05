import sqlite3

from database import create_table, add_patient, view_patients, search_patient, add_appointment, view_doctors, view_appointments_detailed, add_visit,view_visits_detailed, add_doctor, search_doctor_by_specialty, update_patient_age, delete_patient, update_appointment, delete_appointment, delete_visit
create_table()

from datetime import datetime

def get_valid_date(prompt):
    while True:
        date_text = input(prompt)
        try:
            datetime.strptime(date_text, "%Y-%m-%d %H:%M")
            return date_text
        except ValueError:
            print("Invalid format. Please use YYYY-MM-DD HH:MM, e.g. 2026-11-12 10:30")

while True:
    print("1. Register new patient")
    print("2. View all patients")
    print("3. Search for a patient")
    print("4. Book appointments")
    print("5. View appointments")
    print("6. view doctors")
    print("7. Record visit")
    print("8. view visits")
    print("9. Search for a doctor by specialty")
    print("10. Register doctor")
    print("11. update patient age")
    print("12. Delete patient")
    print("13. Update appointment")
    print("14. Delete appointment")
    print("15. Delete visit")
    print("16. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        add_patient(name, age)
        print("Patient registered.")
    
    elif choice == "2":
        patients = view_patients()
        for patient in patients:
            print(f"ID: {patient[0]}, name: {patient[1]}, age: {patient[2]}")
    elif choice == "3":
        name = input("Enter patient name: ")
        results = search_patient(name)
        if not results:
            print("No patient found.")
        else:
            for patient in results:
                print(f"ID: {patient[0]}, name: {patient[1]}, age: {patient[2]}")
    
    elif choice == "4":
        patient_id = int(input("Enter patient ID: "))
        doctor_id = int(input("Enter doctor ID: "))
        appointment_date = get_valid_date("Enter date (YYYY-MM-DD HH:MM): ")
        reason = input("Enter reason: ")
        try:
            add_appointment(patient_id, doctor_id, appointment_date, reason)
            print("Appointment booked.")
        except sqlite3.IntegrityError:
            print("That patient or doctor does not exist.")
    
    elif choice == "5":
        appointments = view_appointments_detailed()
        for appointment in appointments:
            print(f"ID: {appointment[0]}, Patient: {appointment[1]}, Doctor: {appointment[2]}, Date: {appointment[3]}, Reason: {appointment[4]}")
    
    elif choice == "6":
        doctors = view_doctors()
        for doctor in doctors:
            print(f"ID: {doctor[0]}, name: {doctor[1]}, specialty: {doctor[2]}")

    elif choice == "7":
        patient_id = int(input("Enter patient ID: "))
        visit_date = get_valid_date("Enter date (YYYY-MM-DD HH:MM): ")
        symptoms = input("Enter symptoms: ")
        diagnosis = input("Enter diagnosis: ")
        treatment = input("Enter treatment: ")
        prescription = input("Enter prescription: ")
        follow_up_date = input("Enter follow-up date (YYYY-MM-DD), or leave blank: ")
        if follow_up_date != "":
            follow_up_date = get_valid_date("Enter follow-up date again, properly: ")
        try:
            add_visit(patient_id, visit_date, symptoms, diagnosis, treatment, prescription, follow_up_date)
            print("Visit recorded.")
        except sqlite3.IntegrityError:
            print("That patient does not exist.")
    
    elif choice == "8":
        result = view_visits_detailed()
        for visit in result:
            print(f"Id: {visit[0]}, patient_name: {visit[1]}, visit_date: {visit[2]}, symptoms: {visit[3]}, diagnosis: {visit[4]}, treatment: {visit[5]}, prescripton: {visit[6]}, follow_up_date: {visit[7]}")
    
    elif choice == "9":
        specialty = input("Enter doctor specialty: ")
        results = search_doctor_by_specialty(specialty)
        if not results:
            print("No doctor found")
        else:
            for doctor in results:
                print(f"ID: {doctor[0]}, name: {doctor[1]}, specialty: {doctor[2]}")
    
    elif choice == "10":
        name = input("Enter : ")
        specialty = input("Enter specialty: ")
        add_doctor(name, specialty)
        print("Doctor registered.")

    elif choice == "11":
        patient_id = int(input("Enter patient ID: "))
        new_age = int(input("Enter new age: "))
        update_patient_age(patient_id, new_age)
        print("Patient age updated.")

    elif choice == "12":
        patient_id = int(input("Enter patient ID: "))
        try:
            delete_patient(patient_id)
            print("patient deleted")
        except sqlite3.IntegrityError:
            print("cannot delete - patient has an existing appointment or visit.")
    
    elif choice == "13":
        appointment_id = int(input("Enter appointment ID: "))
        new_date = get_valid_date("Enter new date (YYYY-MM-DD HH:MM): ")
        new_reason = input("Enter new reason: ")
        rows_changed = update_appointment(appointment_id, new_date, new_reason)
        if rows_changed == 0:
            print("No appointment found with that ID.")
        else:
            print("Appointment updated.")
        
    
    elif choice == "14":
        appointment_id = int(input("Enter appointment ID: "))
        rows_changed = delete_appointment(appointment_id)
        if rows_changed == 0:
            print("No appointment found with that ID.")
        else:
            print("Appointment deleted.")
    
    elif choice == "15":
        visit_id = int(input("Enter visit ID: "))
        rows_changed = delete_visit(visit_id)
        if rows_changed == 0:
            print("No visit found with that ID.")
        else:
            print("Visit deleted.")

    elif choice == "16":
        print("Goodbye!")
        break

