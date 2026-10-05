from fastapi import FastAPI
from database import view_patients
from database import search_patient_by_id
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to MediTrack"}

@app.get("/patients")
def get_patients():
    return view_patients()

@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    results = search_patient_by_id(patient_id)
    if not results:
        raise HTTPException(status_code=404, detail="Patient not found")
    return results[0]