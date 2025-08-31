# 🏥 Healthcare Backend Management System

A comprehensive Django REST API application for managing healthcare operations including patient management, doctor profiles, user authentication, and patient-doctor mapping system. Perfect for Indian healthcare institutions, clinics, and hospitals like AIIMS, Apollo, Fortis, and Max Healthcare.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Authentication](#authentication)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Contributing](#contributing)

## ✨ Features

- **🔐 User Authentication**: Secure JWT-based authentication with role-based access (Patient/Doctor)
- **👥 Patient Management**: Complete CRUD operations for patient records with user-specific data
- **👨‍⚕️ Doctor Management**: Doctor profile management with specializations and availability
- **🔗 Patient-Doctor Mapping**: Advanced mapping system to assign doctors to patients
- **📱 RESTful API**: Full REST API with proper serialization and validation
- **🛡️ Security**: Token-based authentication with permission controls
- **📊 Database Integration**: PostgreSQL integration with Django ORM
- **📧 Case-Insensitive Email**: Email authentication works regardless of case

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5
- **API Framework**: Django REST Framework 3.16.1
- **Authentication**: JWT (djangorestframework-simplejwt 5.5.1)
- **Database**: PostgreSQL (with psycopg2-binary 2.9.10)
- **Configuration**: python-decouple 3.8 for environment variables
- **Other Dependencies**: PyJWT 2.10.1, sqlparse 0.5.3

## 📁 Project Structure

```
healthcare_backend/
├── 📁 doctors/                 # Doctor management app
│   ├── models.py              # Doctor model with specialization
│   ├── serializers.py         # Doctor API serializers
│   ├── views.py               # Doctor CRUD views
│   ├── urls.py                # Doctor API endpoints
│   └── admin.py               # Admin interface
├── 📁 patients/               # Patient management app
│   ├── models.py              # Patient model with medical info
│   ├── serializers.py         # Patient API serializers
│   ├── views.py               # Patient CRUD views (user-specific)
│   ├── urls.py                # Patient API endpoints
│   └── admin.py               # Admin interface
├── 📁 users/                  # User authentication and management
│   ├── models.py              # Custom User model with roles
│   ├── serializers.py         # User registration/auth serializers
│   ├── views.py               # Registration views
│   ├── token_views.py         # Custom JWT login with user info
│   ├── urls.py                # Auth API endpoints
│   └── admin.py               # User admin interface
├── 📁 mappings/               # Patient-Doctor mapping system
│   ├── models.py              # PatientDoctorMapping model
│   ├── serializers.py         # Mapping API serializers
│   ├── views.py               # Mapping CRUD views
│   ├── urls.py                # Mapping API endpoints
│   └── admin.py               # Mapping admin interface
├── 📁 healthcare_backend/     # Main project settings
│   ├── settings.py            # Django settings with JWT config
│   ├── urls.py                # Main URL configuration
│   ├── wsgi.py                # WSGI configuration
│   └── asgi.py                # ASGI configuration
├── manage.py                  # Django management script
└── requirements.txt           # Project dependencies
```

## 🚀 Installation

### Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/RahulK847/Django_HealthCare_backend.git
   cd Django_HealthCare_backend
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv rest_api_env
   
   # On Windows
   .\rest_api_env\Scripts\Activate.ps1
   
   # On macOS/Linux
   source rest_api_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   cd healthcare_backend
   pip install -r requirements.txt
   ```

4. **Database Setup**
   
   Create PostgreSQL database:
   ```sql
   CREATE DATABASE healthcare_db;
   CREATE USER postgres WITH PASSWORD 'sql';
   GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO postgres;
   ```

5. **Environment Configuration** (Optional)
   Create a `.env` file for production:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   DATABASE_URL=postgresql://postgres:sql@localhost:5432/healthcare_db
   ```

6. **Apply migrations**
   ```bash
   python manage.py makemigrations users
   python manage.py makemigrations patients
   python manage.py makemigrations doctors
   python manage.py makemigrations mappings
   python manage.py migrate
   ```

7. **Create superuser** (Optional)
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Documentation

### Base URL
```
http://127.0.0.1:8000
```

### 🔐 Authentication Endpoints

#### Register User
```http
POST /api/auth/register/
Content-Type: application/json

{
    "username": "aniketgupta",
    "email": "aniket.gupta@gmail.com",
    "password": "Aniket@123",
    "phone": "9876543210",
    "role": "patient"  // or "doctor"
}
```

**Response:**
```json
{
    "user": {
        "id": 1,
        "username": "aniketgupta",
        "email": "aniket.gupta@gmail.com",
        "phone": "9876543210",
        "role": "patient"
    },
    "message": "User registered successfully",
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
}
```

#### Login User
```http
POST /api/auth/login/
Content-Type: application/json

{
    "email": "aniket.gupta@gmail.com",  // Case-insensitive
    "password": "Aniket@123"
}
```

**Response:**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user": {
        "id": 1,
        "email": "aniket.gupta@gmail.com",
        "role": "patient"
    }
}
```

#### Refresh Token
```http
POST /api/auth/token/refresh/
Content-Type: application/json

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 👨‍⚕️ Doctor Management

#### Create Doctor
```http
POST /api/doctors/
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
    "name": "Dr. Arjun Sharma",
    "email": "dr.arjun@aiims.edu",
    "phone": "9876543210",
    "specialization": "Cardiology",
    "license_number": "MH12345",
    "experience_years": 15,
    "address": "AIIMS Hospital, New Delhi",
    "consultation_fee": 1500.00,
    "availability": "Mon-Fri 9AM-5PM"
}
```

#### Get All Doctors
```http
GET /api/doctors/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Response:**
```json
[
    {
        "id": 1,
        "name": "Dr. Arjun Sharma",
        "email": "dr.arjun@aiims.edu",
        "specialization": "Cardiology",
        "consultation_fee": "1500.00",
        "availability": "Mon-Fri 9AM-5PM"
    },
    {
        "id": 2,
        "name": "Dr. Kavya Reddy",
        "email": "dr.kavya@apollo.com",
        "specialization": "Gynecology",
        "consultation_fee": "1200.00",
        "availability": "Tue-Sat 10AM-6PM"
    }
]
```

#### Get Specific Doctor
```http
GET /api/doctors/{id}/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

#### Update Doctor
```http
PUT /api/doctors/{id}/
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
    "name": "Dr. Arjun Sharma",
    "consultation_fee": 1800.00,
    // ... other fields
}
```

#### Delete Doctor
```http
DELETE /api/doctors/{id}/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### 👥 Patient Management

**Note**: Users can only access patients they created.

#### Create Patient
```http
POST /api/patients/
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
    "name": "Vikram Singh",
    "email": "vikram.singh@gmail.com",
    "phone": "8765432109",
    "date_of_birth": "1990-05-15",
    "address": "123 CP, New Delhi, 110001",
    "gender": "male",
    "blood_group": "B+",
    "emergency_contact": "7890123456",
    "medical_history": "Diabetes, High BP, Regular medication"
}
```

#### Get All Patients (User-Specific)
```http
GET /api/patients/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Response:**
```json
[
    {
        "id": 1,
        "name": "Vikram Singh",
        "email": "vikram.singh@gmail.com",
        "phone": "8765432109",
        "date_of_birth": "1990-05-15",
        "address": "123 CP, New Delhi, 110001",
        "gender": "male",
        "blood_group": "B+",
        "emergency_contact": "7890123456",
        "medical_history": "Diabetes, High BP, Regular medication",
        "created_by": "aniket.gupta@gmail.com",
        "created_at": "2025-01-31T10:30:00Z"
    }
]
```

#### Get Specific Patient
```http
GET /api/patients/{id}/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

#### Update Patient
```http
PUT /api/patients/{id}/
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
    "name": "Vikram Singh",
    "medical_history": "Diabetes, High BP, Regular medication. Recent checkup normal.",
    // ... other fields
}
```

#### Delete Patient
```http
DELETE /api/patients/{id}/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### 🔗 Patient-Doctor Mapping

#### Assign Doctor to Patient
```http
POST /api/mappings/
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
    "patient": 1,
    "doctor": 1,
    "notes": "Regular cardiology checkup for diabetes complications"
}
```

#### Get All Mappings
```http
GET /api/mappings/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Response:**
```json
[
    {
        "id": 1,
        "patient": 1,
        "doctor": 1,
        "patient_details": {
            "id": 1,
            "name": "Vikram Singh",
            "email": "vikram.singh@gmail.com",
            "phone": "8765432109"
        },
        "doctor_details": {
            "id": 1,
            "name": "Dr. Arjun Sharma",
            "specialization": "Cardiology",
            "consultation_fee": "1500.00"
        },
        "notes": "Regular cardiology checkup for diabetes complications",
        "is_active": true,
        "assigned_date": "2025-01-31T11:00:00Z",
        "created_by": "aniket.gupta@gmail.com"
    }
]
```

#### Get Doctors for Specific Patient
```http
GET /api/mappings/{patient_id}/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

#### Remove Doctor from Patient (Soft Delete)
```http
DELETE /api/mappings/{mapping_id}/
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## 💡 Usage Examples

### Complete Workflow Example

1. **Register as a doctor from Apollo Hospital**:
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "drpriya", "email": "priya@apollo.com", "password": "Doctor@123", "role": "doctor"}'
```

2. **Create a patient record**:
```bash
curl -X POST http://127.0.0.1:8000/api/patients/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Rohan Mehta", "email": "rohan.mehta@gmail.com", "phone": "9123456789", "date_of_birth": "1987-04-30", "address": "Mumbai, Maharashtra", "gender": "male", "blood_group": "A+"}'
```

3. **Create doctor profile for specialist**:
```bash
curl -X POST http://127.0.0.1:8000/api/doctors/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Dr. Sneha Joshi", "email": "sneha@fortis.com", "specialization": "Endocrinology", "license_number": "DL67890", "experience_years": 12, "consultation_fee": 1800}'
```

4. **Assign specialist to patient**:
```bash
curl -X POST http://127.0.0.1:8000/api/mappings/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"patient": 1, "doctor": 1, "notes": "Diabetes management and regular monitoring"}'
```

## 🗄️ Database Schema

### User Model
- `id` (Primary Key)
- `username` (Unique)
- `email` (Unique, Case-insensitive)
- `phone` (Unique, 10 digits)
- `role` (Choice: 'patient' or 'doctor')
- `password` (Hashed)
- `is_active`, `is_staff`, `date_joined`

### Patient Model
- `id` (Primary Key)
- `created_by` (Foreign Key to User)
- `name`, `email`, `phone`
- `date_of_birth`, `address`
- `gender` (male/female/other)
- `blood_group` (A+, A-, B+, B-, AB+, AB-, O+, O-)
- `emergency_contact`, `medical_history`
- `created_at`, `updated_at`

### Doctor Model
- `id` (Primary Key)
- `name`, `email`, `phone`
- `specialization` (Cardiology, Neurology, etc.)
- `license_number` (Medical license format)
- `experience_years`, `consultation_fee` (in INR)
- `address` (Hospital/clinic address)
- `availability`
- `created_at`, `updated_at`

### PatientDoctorMapping Model
- `id` (Primary Key)
- `created_by` (Foreign Key to User)
- `patient` (Foreign Key to Patient)
- `doctor` (Foreign Key to Doctor)
- `notes`, `is_active` (Soft Delete)
- `assigned_date`, `created_at`, `updated_at`
- `unique_together` = ['patient', 'doctor']

## 🔒 Authentication & Permissions

### JWT Configuration
- **Access Token Lifetime**: 1 day
- **Refresh Token Lifetime**: 7 days
- **Auth Header**: `Authorization: Bearer <token>`

### Permission System
- **Authentication Required**: All endpoints except registration
- **Patient Data**: Users can only access patients they created
- **Doctor Data**: All authenticated users can access all doctors
- **Mapping Data**: Users can only create mappings for their patients

## 🧪 Testing

### Manual API Testing
Use tools like:
- **Postman**: Import the API collection
- **curl**: Command line testing
- **HTTPie**: User-friendly HTTP client
- **Django Admin**: `http://127.0.0.1:8000/admin/`

### Test Scenarios
- ✅ User registration and login
- ✅ CRUD operations for all models
- ✅ Authentication and permissions
- ✅ Case-insensitive email login
- ✅ Patient-doctor mapping relationships
- ✅ Error handling and validation

## 📊 Sample Test Data

### Doctors
- Dr. Arjun Sharma (Cardiologist, AIIMS Delhi)
- Dr. Kavya Reddy (Gynecologist, Apollo Mumbai)
- Dr. Rajesh Kumar (Orthopedic, Fortis Bangalore)

### Patients
- Vikram Singh (Male, B+, Delhi)
- Priya Agarwal (Female, A+, Bangalore)
- Rohan Mehta (Male, O+, Mumbai)

### Common Specializations
- Cardiology, Neurology, Orthopedics
- Gynecology, Pediatrics, ENT
- Dermatology, Ophthalmology

## 📊 API Response Codes

- `200 OK` - Successful GET, PUT requests
- `201 Created` - Successful POST requests
- `204 No Content` - Successful DELETE requests
- `400 Bad Request` - Validation errors
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Permission denied
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server errors

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Rahul Kumar** - Healthcare Backend Developer  
📧 Email: smilerahul847@gmail.com  
🌟 GitHub: [@rahulk847](https://github.com/rahulk847)

---

*Built with ❤️ using Django and Django REST Framework*

## 🙏 Acknowledgments

- Thanks to healthcare institutions for inspiration
- AIIMS, Apollo, Fortis, Max Healthcare for reference
- Django and DRF communities for excellent documentation