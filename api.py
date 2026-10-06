from fastapi import FastAPI
from database import view_patients
from database import search_patient_by_id
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import add_patient
from database import update_patient_age
import sqlite3
from database import delete_patient
from database import add_doctor
from database import view_doctors
from database import add_appointment
from database import view_appointments_detailed
from database import update_appointment
from database import delete_appointment

class PatientCreate(BaseModel):
    name: str
    age: int
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to MediTrack"}

class Patient(BaseModel):
    id: int
    name: str
    age: int

@app.get("/patients", response_model=list[Patient])
def get_patients():
    rows = view_patients()
    return [Patient(id=row[0], name=row[1], age=row[2]) for row in rows]

@app.get("/patients/{patient_id}", response_model=Patient)
def get_patient(patient_id: int):
    results = search_patient_by_id(patient_id)
    if not results:
        raise HTTPException(status_code=404, detail="Patient not found")
    row = results[0]
    return Patient(id=row[0], name=row[1], age=row[2])

@app.post("/patients", status_code=201)
def create_patient(patient: PatientCreate):
    add_patient(patient.name, patient.age)
    return {"message": "Patient created"}

class PatientUpdate(BaseModel):
    age: int

@app.put("/patients/{patient_id}")
def update_patient(patient_id: int, patient: PatientUpdate):
    rows_changed = update_patient_age(patient_id, patient.age)
    if rows_changed == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient updated"}

@app.delete("/patients/{patient_id}")
def delete_patient_endpoint(patient_id: int):
    try:
        rows_changed = delete_patient(patient_id)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Cannot delete — patient has existing appointments or visits")
    if rows_changed == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted"}

class Doctor(BaseModel):
    id: int
    name: str
    specialty: str

class DoctorCreate(BaseModel):
    name: str
    specialty: str

@app.get("/doctors", response_model=list[Doctor])
def get_doctors():
    rows = view_doctors()
    return [Doctor(id=row[0], name=row[1], specialty=row[2]) for row in rows]

@app.post("/doctors", status_code=201)
def create_doctor(doctor: DoctorCreate):
    add_doctor(doctor.name, doctor.specialty)
    return {"message": "Doctor created"}

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: str
    reason: str

@app.post("/appointments", status_code=201)
def create_appointment(appointment: AppointmentCreate):
    try:
        add_appointment(appointment.patient_id, appointment.doctor_id, appointment.appointment_date, appointment.reason)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=422, detail="Patient or doctor does not exist")
    return {"message": "Appointment booked"}

class AppointmentDetail(BaseModel):
    id: int
    patient_name: str
    doctor_name: str
    appointment_date: str
    reason: str

@app.get("/appointments", response_model=list[AppointmentDetail])
def get_appointments():
    rows = view_appointments_detailed()
    return [AppointmentDetail(id=row[0], patient_name=row[1], doctor_name=row[2], appointment_date=row[3], reason=row[4]) for row in rows]

class AppointmentUpdate(BaseModel):
    new_date: str
    new_reason: str

@app.put("/appointments/{appointment_id}")
def update_appointment_endpoint(appointment_id: int, appointment: AppointmentUpdate):
    rows_changed = update_appointment(appointment_id, appointment.new_date, appointment.new_reason)
    if rows_changed == 0:
        raise HTTPException(status_code=404, detail="appointment not found")
    return {"message": "appointment updated"}

@app.delete("/appointments/{appointment_id}")
def delete_appointment_endpoint(appointment_id: int):
    
    rows_changed = delete_appointment(appointment_id)
    if rows_changed == 0:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Appointment deleted"}
