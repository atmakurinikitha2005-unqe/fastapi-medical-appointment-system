from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field
from typing import List, Optional
app = FastAPI()

# In-Memory Database

doctors = []
appointments = []

# Pydantic Models

class Doctor(BaseModel):
    id: int
    name: str = Field(..., min_length=3)
    specialization: str
    fee: float = Field(..., gt=0)


class Appointment(BaseModel):
    id: int
    patient_name: str = Field(..., min_length=3)
    doctor_id: int
    status: Optional[str] = "booked"  # booked → checked-in → completed

# Helper Functions

def find_doctor(doc_id: int):
    for doc in doctors:
        if doc["id"] == doc_id:
            return doc
    return None


def find_appointment(app_id: int):
    for ap in appointments:
        if ap["id"] == app_id:
            return ap
    return None


def filter_doctors(specialization=None, max_fee=None):
    result = doctors

    if specialization is not None:
        result = [d for d in result if d["specialization"].lower() == specialization.lower()]

    if max_fee is not None:
        result = [d for d in result if d["fee"] <= max_fee]

    return result

# Day 1 - GET APIs

@app.get("/")
def home():
    return {"message": "Medical Appointment System API Running"}


@app.get("/doctors")
def get_all_doctors():
    return doctors


@app.get("/appointments")
def get_all_appointments():
    return appointments


@app.get("/doctors/count")
def doctor_count():
    return {"total_doctors": len(doctors)}

# Day 2 - POST + Validation

@app.post("/doctors", status_code=status.HTTP_201_CREATED)
def add_doctor(doc: Doctor):
    if find_doctor(doc.id):
        raise HTTPException(status_code=400, detail="Doctor already exists")

    doctors.append(doc.dict())
    return {"message": "Doctor added", "data": doc}


@app.post("/appointments", status_code=status.HTTP_201_CREATED)
def book_appointment(ap: Appointment):
    if find_appointment(ap.id):
        raise HTTPException(status_code=400, detail="Appointment exists")

    doctor = find_doctor(ap.doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    appointments.append(ap.dict())
    return {"message": "Appointment booked", "data": ap}

# Day 3 - Filter + Query

@app.get("/doctors/filter")
def filter_doctor_api(
    specialization: Optional[str] = Query(None),
    max_fee: Optional[float] = Query(None)
):
    result = filter_doctors(specialization, max_fee)

    if not result:
        return {"message": "No doctors found"}

    return result

# Day 4 - CRUD

@app.put("/doctors/{doc_id}")
def update_doctor(doc_id: int, updated: Doctor):
    doctor = find_doctor(doc_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    doctor.update(updated.dict(exclude_unset=True))
    return {"message": "Doctor updated", "data": doctor}


@app.delete("/doctors/{doc_id}")
def delete_doctor(doc_id: int):
    doctor = find_doctor(doc_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    doctors.remove(doctor)
    return {"message": "Doctor deleted"}

# Day 5 - Workflow APIs

@app.put("/appointments/checkin/{app_id}")
def checkin(app_id: int):
    ap = find_appointment(app_id)
    if not ap:
        raise HTTPException(status_code=404, detail="Appointment not found")

    ap["status"] = "checked-in"
    return {"message": "Checked-in", "data": ap}


@app.put("/appointments/complete/{app_id}")
def complete(app_id: int):
    ap = find_appointment(app_id)
    if not ap:
        raise HTTPException(status_code=404, detail="Appointment not found")

    ap["status"] = "completed"
    return {"message": "Appointment completed", "data": ap}

# Day 6 - Search

@app.get("/doctors/search")
def search_doctors(keyword: str):
    result = [
        d for d in doctors
        if keyword.lower() in d["name"].lower()
        or keyword.lower() in d["specialization"].lower()
    ]

    if not result:
        return {"message": "No matching doctors"}

    return result

# Sorting

@app.get("/doctors/sort")
def sort_doctors(sort_by: str = "fee", order: str = "asc"):
    if sort_by not in ["fee", "name"]:
        raise HTTPException(status_code=400, detail="Invalid sort field")

    reverse = True if order == "desc" else False

    sorted_data = sorted(doctors, key=lambda x: x[sort_by], reverse=reverse)
    return sorted_data

# Pagination

@app.get("/doctors/page")
def paginate(page: int = 1, limit: int = 2):
    start = (page - 1) * limit
    end = start + limit

    total = len(doctors)
    total_pages = (total + limit - 1) // limit

    return {
        "page": page,
        "total_pages": total_pages,
        "data": doctors[start:end]
    }


# Combined Browse

@app.get("/doctors/browse")
def browse(
    keyword: Optional[str] = None,
    sort_by: Optional[str] = None,
    order: str = "asc",
    page: int = 1,
    limit: int = 2
):
    result = doctors

    # Search
    if keyword:
        result = [
            d for d in result
            if keyword.lower() in d["name"].lower()
            or keyword.lower() in d["specialization"].lower()
        ]

    # Sort
    if sort_by:
        reverse = True if order == "desc" else False
        result = sorted(result, key=lambda x: x[sort_by], reverse=reverse)

    # Pagination
    start = (page - 1) * limit
    end = start + limit
    total = len(result)

    return {
        "total": total,
        "page": page,
        "data": result[start:end]
    }

# Variable Routes (LAST)

@app.get("/doctors/{doc_id}")
def get_doctor(doc_id: int):
    doctor = find_doctor(doc_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor


@app.get("/appointments/{app_id}")
def get_appointment(app_id: int):
    ap = find_appointment(app_id)
    if not ap:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return ap