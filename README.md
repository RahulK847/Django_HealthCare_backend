# 🏥 Healthcare Backend API

A comprehensive Django REST API for healthcare management with JWT authentication and interactive Swagger documentation.

**🚀 Live API:** https://healthcare-backend-4bbd.onrender.com  
**📖 Interactive Docs:** https://healthcare-backend-4bbd.onrender.com/swagger/

## ✨ Features

- **📖 Hybrid Documentation** - Beautiful custom docs + Interactive Swagger UI
- **🔐 JWT Authentication** - Secure user registration/login with role-based access
- **👥 Patient Management** - Complete CRUD with user-specific data access
- **👨‍⚕️ Doctor Management** - Doctor profiles with specializations & availability
- **🔗 Patient-Doctor Mapping** - Advanced assignment system with soft delete
- **📧 Case-Insensitive Email** - Login works regardless of email case
- **🧪 One-Click Testing** - Test APIs directly in browser with authentication
- **🛡️ Security** - Token-based auth with permission controls

## 🛠️ Tech Stack

- **Django 5.2.5** + **Django REST Framework 3.16.1**
- **JWT Authentication** (djangorestframework-simplejwt)
- **Swagger Documentation** (drf-yasg)
- **PostgreSQL** with Django ORM
- **Deployed on Render** with environment variables

## 📖 API Documentation Options

### 🏠 Main Documentation Hub
**https://healthcare-backend-4bbd.onrender.com/** - Beautiful custom documentation with Swagger integration

### 🌐 Interactive Documentation
- **Swagger UI:** https://healthcare-backend-4bbd.onrender.com/swagger/
- **ReDoc:** https://healthcare-backend-4bbd.onrender.com/redoc/
- **Alternative Docs:** https://healthcare-backend-4bbd.onrender.com/docs/

### 🔧 How to Use
**Option 1: One-Click Testing (Recommended)**
1. Visit the main documentation page
2. Click the **"📖 Try Interactive Swagger Documentation"** button
3. Register/Login to get your JWT token
4. Click **"Authorize"** in Swagger UI
5. Enter: `Bearer YOUR_ACCESS_TOKEN`
6. Test all endpoints with live examples!

**Option 2: Direct Access**
- Go directly to `/swagger/` for interactive testing
- Go to `/redoc/` for clean documentation view

## 🚀 Quick API Testing

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

## 🧪 Testing Your API

### 🚀 Instant Testing (No Setup Required)
1. **Visit:** https://healthcare-backend-4bbd.onrender.com/
2. **Click:** "📖 Try Interactive Swagger Documentation" button
3. **Register/Login** in Swagger UI to get JWT token
4. **Authorize** with your token and test all endpoints instantly!

### 🛠️ Manual Testing with External Tools
Use **Postman**, **curl**, or **HTTPie**:
1. **Register/Login** → Get access token
2. **Set Header:** `Authorization: Bearer YOUR_TOKEN`
3. **Test all endpoints** with realistic Indian healthcare data

### 📱 Quick Access URLs
- **📖 Main Docs:** https://healthcare-backend-4bbd.onrender.com/
- **⚡ Swagger UI:** https://healthcare-backend-4bbd.onrender.com/swagger/
- **📚 ReDoc:** https://healthcare-backend-4bbd.onrender.com/redoc/
- **🔐 Register:** https://healthcare-backend-4bbd.onrender.com/api/auth/register/
- **🔑 Login:** https://healthcare-backend-4bbd.onrender.com/api/auth/login/

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
🌐 Portfolio: [rahulk847.live](https://www.rahulk847.live/)

---

**🏥 Built with ❤️ for healthcare management systems**