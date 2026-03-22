#  FastAPI Medical Appointment System

# Project Overview

The **Medical Appointment System** is a backend application built using **FastAPI** that allows efficient management of doctors and patient appointments.
This project was developed as part of the **FastAPI Internship Final Project**, covering all core backend development concepts including API design, validation, CRUD operations, workflows, and advanced querying techniques

# Project Objective

The goal of this project is to:

* Build a real-world backend system using FastAPI
* Implement RESTful APIs (GET, POST, PUT, DELETE)
* Apply Pydantic validation for request data
* Design multi-step workflows (Appointment lifecycle)
* Implement advanced features like search, sorting, and pagination
* Test APIs using Swagger UI

# Features Implemented

# Day 1 — GET APIs

* Home route (`/`)
* Get all doctors (`/doctors`)
* Get doctor by ID (`/doctors/{id}`)
* Count total doctors (`/doctors/count`)
* Get all appointments (`/appointments`)

# Day 2 — POST APIs + Pydantic Validation

* Add new doctor with validation
* Book appointment
* Field validations:
  * `min_length` for names
  * `gt=0` for fee
* Automatic error handling for invalid inputs

# Day 3 — Helper Functions & Filtering

Helper functions used:
* `find_doctor()` → find doctor by ID
* `find_appointment()` → find appointment
* `filter_doctors()` → filter based on specialization and fee
Filtering implemented using query parameters:
* `/doctors/filter?specialization=Cardiology`
* `/doctors/filter?max_fee=500`

# Day 4 — CRUD Operations
*POST* → Create doctor
*PUT* → Update doctor
*DELETE* → Remove doctor
* Error handling:
  * 404 → Not Found
  * 400 → Bad Request

# Day 5 — Multi-Step Workflow
Appointment lifecycle:
1. *Book Appointment* → `/appointments`
2. *Check-in* → `/appointments/checkin/{id}`
3. *Complete Appointment* → `/appointments/complete/{id}`
This simulates a real-world hospital workflow.

# Day 6 — Advanced APIs
# Search
* `/doctors/search?keyword=Ravi`
* Case-insensitive search across name and specialization
# Sorting
* `/doctors/sort?sort_by=fee&order=desc`
* Supports ascending and descending order
# Pagination
* `/doctors/page?page=1&limit=2`
* Returns paginated results with total pages
# Combined Browse
* `/doctors/browse`
* Supports:
  * Search
  * Sorting
  * Pagination
* All parameters optional

# Technologies Used

| Technology | Purpose              |
| ---------- | -------------------- |
| FastAPI    | API framework        |
| Uvicorn    | ASGI server          |
| Pydantic   | Data validation      |
| Python     | Programming language |

#  Project Structure
fastapi-medical-appointment-system/
│
├── main.py              # Main FastAPI application
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── screenshots/         # Swagger API screenshots 

# How to Run the Project

# Step 1: Go to the folder created

fastapi-medical-appointment

# Step 2:Open Terminal
Terminal->New Terminal

# Step 3: Install Dependencies
pip install -r requirements.txt

#  Step 4: Run Server
uvicorn main:app --reload

# Step 5: Open Swagger UI
http://127.0.0.1:8000/docs

#  Screenshots
All APIs are tested using Swagger UI.
Screenshots for all 20 endpoints are included in the `screenshots/` folder.

#  API Endpoints Summary

#  Doctors APIs

* GET `/doctors`
* GET `/doctors/{id}`
* POST `/doctors`
* PUT `/doctors/{id}`
* DELETE `/doctors/{id}`

#  Appointment APIs

* GET `/appointments`
* POST `/appointments`
* PUT `/appointments/checkin/{id}`
* PUT `/appointments/complete/{id}`

#  Advanced APIs

* GET `/doctors/filter`
* GET `/doctors/search`
* GET `/doctors/sort`
* GET `/doctors/page`
* GET `/doctors/browse`

# Key Learning Outcomes

* Built REST APIs using FastAPI
* Implemented data validation with Pydantic
* Designed modular helper functions
* Implemented full CRUD operations
* Created real-world workflow system
* Applied search, sorting, and pagination
* Gained experience with Swagger API testing

# Acknowledgement
I sincerely thank 
## Innomatics Research Labs##
 for providing this valuable internship opportunity. This project helped me gain practical knowledge in FastAPI, API development, and backend system design.

#  Conclusion
This project demonstrates the ability to design and develop a complete backend system using FastAPI. It reflects strong understanding of API development, validation, workflows, and advanced querying techniques.
