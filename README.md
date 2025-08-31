# 🏥 Healthcare Backend API

A comprehensive Django REST API for healthcare management with JWT authentication, built for Indian healthcare institutions.

**🚀 Live API:** https://healthcare-backend-4bbd.onrender.com

## ✨ Features

- **🔐 JWT Authentication** - Secure user registration/login with role-based access
- **👥 Patient Management** - Complete CRUD with user-specific data access
- **👨‍⚕️ Doctor Management** - Doctor profiles with specializations & availability
- **🔗 Patient-Doctor Mapping** - Advanced assignment system with soft delete
- **📧 Case-Insensitive Email** - Login works regardless of email case
- **🛡️ Security** - Token-based auth with permission controls

## 🛠️ Tech Stack

- **Django 5.2.5** + **Django REST Framework 3.16.1**
- **JWT Authentication** (djangorestframework-simplejwt)
- **PostgreSQL** with Django ORM
- **Deployed on Render** with environment variables

## 📚 API Documentation

### Base URL
```
https://healthcare-backend-4bbd.onrender.com
```

### 🔐 Authentication

#### Register User
```http
POST /api/auth/register/
Content-Type: application/json

{
    "username": "rahul_kumar",
    "email": "rahul.kumar@gmail.com",
    "password": "Secure@123",
    "phone": "9876543210",
    "role": "patient"  // or "doctor"
}
```

#### Login
```http
POST /api/auth/login/
Content-Type: application/json

{
    "email": "rahul.kumar@gmail.com",  // Case-insensitive
    "password": "Secure@123"
}
```

**Response includes access token for authentication.**

### 👥 Patient Management
*All endpoints require: `Authorization: Bearer YOUR_TOKEN`*

```http
POST /api/patients/          # Create patient
GET /api/patients/           # Get all patients (user-specific)
GET /api/patients/{id}/      # Get specific patient
PUT /api/patients/{id}/      # Update patient
DELETE /api/patients/{id}/   # Delete patient
```

**Example Patient Data:**
```json
{
    "name": "Arjun Sharma",
    "email": "arjun.sharma@gmail.com",
    "phone": "8765432109",
    "date_of_birth": "1990-05-15",
    "address": "123 MG Road, Bangalore",
    "gender": "male",
    "blood_group": "B+",
    "emergency_contact": "9876543210",
    "medical_history": "No known allergies"
}
```

### 👨‍⚕️ Doctor Management
*All endpoints require authentication*

```http
POST /api/doctors/           # Create doctor
GET /api/doctors/            # Get all doctors
GET /api/doctors/{id}/       # Get specific doctor
PUT /api/doctors/{id}/       # Update doctor
DELETE /api/doctors/{id}/    # Delete doctor
```

**Example Doctor Data:**
```json
{
    "name": "Dr. Priya Patel",
    "email": "priya.patel@aiims.edu",
    "phone": "7654321098",
    "specialization": "Cardiology",
    "license_number": "CARD2025001",
    "experience_years": 8,
    "address": "AIIMS Hospital, New Delhi",
    "consultation_fee": "1500.00",
    "availability": "Mon-Fri 9AM-5PM"
}
```

### 🔗 Patient-Doctor Mapping
*User can only map their own patients*

```http
POST /api/mappings/              # Assign doctor to patient
GET /api/mappings/               # Get all mappings
GET /api/mappings/{patient_id}/  # Get doctors for specific patient
DELETE /api/mappings/{id}/       # Remove mapping (soft delete)
```

**Example Mapping:**
```json
{
    "patient": 1,
    "doctor": 1,
    "notes": "Regular cardiology consultation"
}
```

## 🧪 Testing with Postman

1. **Register/Login** → Get access token
2. **Set Header:** `Authorization: Bearer YOUR_TOKEN`
3. **Test all endpoints** with Indian names and medical scenarios

### Quick Test URLs:
- **Register:** `https://healthcare-backend-4bbd.onrender.com/api/auth/register/`
- **Login:** `https://healthcare-backend-4bbd.onrender.com/api/auth/login/`
- **Patients:** `https://healthcare-backend-4bbd.onrender.com/api/patients/`
- **Doctors:** `https://healthcare-backend-4bbd.onrender.com/api/doctors/`
- **Mappings:** `https://healthcare-backend-4bbd.onrender.com/api/mappings/`

## 🗄️ Database Schema

- **User:** email (unique), role (patient/doctor), phone
- **Patient:** name, medical info, created_by (FK to User)
- **Doctor:** name, specialization, license_number, consultation_fee
- **Mapping:** patient (FK), doctor (FK), is_active (soft delete)

## 🔒 Security Features

- **JWT tokens** (1-day access, 7-day refresh)
- **User-specific data** (patients belong to creator)
- **Role-based access** (patient/doctor roles)
- **Input validation** and error handling

## 🚀 Local Development

```bash
# Clone repository
git clone https://github.com/RahulK847/Django_HealthCare_backend.git
cd Django_HealthCare_backend

# Setup virtual environment
python -m venv rest_api_env
.\rest_api_env\Scripts\Activate.ps1  # Windows
# source rest_api_env/bin/activate   # Mac/Linux

# Install dependencies
cd healthcare_backend
pip install -r requirements.txt

# Setup PostgreSQL database
# Update settings.py with your database credentials

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

Local API: `http://127.0.0.1:8000`

## 👨‍💻 Author

**Rahul Kumar**  
📧 smilerahul847@gmail.com  
🌟 GitHub: [@RahulK847](https://github.com/RahulK847)

---

**🏥 Perfect for Indian healthcare institutions like AIIMS, Apollo, Fortis, and Max Healthcare!**