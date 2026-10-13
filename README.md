# meditrack

# MediTrack: Patient & Appointment Management System

A small clinic management app built as a learning project. It registers patients and doctors, books appointments, and records visit notes. It runs three ways: a command-line menu, a REST API, and a simple web page.

> **Demo only.** MediTrack uses fictional data and is not a medical system. It doesn't diagnose anything or make medical decisions, and it should never be used for real patient records.

## Features

- **Patients:** register, list, view one, update age, delete
- **Doctors:** register, list, view one, search by specialty, delete
- **Appointments:** book, list (with patient and doctor names), reschedule, delete
- **Visits:** record symptoms, diagnosis, treatment, prescription and follow-up date; list, update date and treatment, delete
- **Data integrity:** SQLite foreign keys are enforced, so you can't book an appointment for a patient who doesn't exist, and you can't delete a patient who still has appointments or visits

## Tech stack

Python 3.12, SQLite (standard library `sqlite3`), FastAPI with Uvicorn, Pydantic, and plain HTML/CSS/JavaScript using `fetch` (no frontend framework).

## Project structure

```
meditrack/
├── database.py        # SQLite tables and all database functions
├── api.py             # FastAPI REST API
├── index.html         # Browser frontend (talks to the API)
├── app.py             # Command-line menu on top of SQLite
├── main.py            # Early version: command-line menu with JSON file storage
├── requirements.txt
└── README.md
```

## Getting started

1. Clone the repository and enter the folder:
```
   git clone https://github.com/sojedo/meditrack.git
   cd <meditrack>
```
2. Create and activate a virtual environment:
```
   python3 -m venv venv
   source venv/bin/activate
```
   (On Windows, activate with `venv\Scripts\activate`.)
3. Install the dependencies:
```
   pip install -r requirements.txt
```
4. Create the database tables (run once):
```
   python3 database.py
```
5. Start the API:
```
   uvicorn api:app --reload
```
6. Open `index.html` in your browser. Interactive API docs are at http://127.0.0.1:8000/docs

To use the command-line version instead of the web page, run `python3 app.py`.

## API overview

| Resource | Endpoints |
|---|---|
| Patients | `POST /patients`, `GET /patients`, `GET /patients/{id}`, `PUT /patients/{id}`, `DELETE /patients/{id}` |
| Doctors | `POST /doctors`, `GET /doctors`, `GET /doctors/{id}`, `GET /doctors/specialty/{specialty}`, `DELETE /doctors/{id}` |
| Appointments | `POST /appointments`, `GET /appointments`, `PUT /appointments/{id}`, `DELETE /appointments/{id}` |
| Visits | `POST /visits`, `GET /visits`, `PUT /visits/{id}`, `DELETE /visits/{id}` |

Status codes used: `200` OK, `201` Created, `404` Not Found, `409` Conflict (for example, deleting a patient who has appointments or visits), and `422` Unprocessable Entity (invalid request body, or a patient or doctor that doesn't exist).

## How it was built

1. **Python fundamentals:** a command-line menu using functions, lists and dictionaries
2. **File storage:** saving and loading patient records as JSON
3. **Database:** SQLite with patients, doctors, appointments and visits tables, foreign keys, and JOIN queries
4. **REST API:** FastAPI with Pydantic validation, response models and proper HTTP status codes
5. **Frontend:** an HTML/CSS/JavaScript page that calls the API

## Known limitations

- No authentication, and CORS allows all origins. That's fine for local use but not for deployment.
- The web forms for appointments and visits take patient and doctor IDs, and they don't validate date format (the command-line menu does).
- Updating a patient only changes their age.
- Dates are stored as text in `YYYY-MM-DD HH:MM` format.