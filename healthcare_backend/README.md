# Healthcare Management System

A comprehensive Django REST API application for managing healthcare operations including patient management, doctor profiles, and user authentication.

## Features

- **User Management**: Secure user registration and authentication using JWT tokens
- **Patient Management**: Complete CRUD operations for patient records
- **Doctor Management**: Doctor profile management and information tracking
- **Mapping System**: Advanced mapping functionality for healthcare data
- **REST API**: Full RESTful API with proper serialization
- **Authentication**: Token-based authentication using JWT

## Tech Stack

- **Backend**: Django 5.2.5
- **API Framework**: Django REST Framework 3.16.1
- **Authentication**: JWT (djangorestframework-simplejwt 5.5.1)
- **Database**: PostgreSQL (with psycopg2-binary 2.9.10)
- **Configuration**: python-decouple for environment variables

## Project Structure

```
healthcare_backend/
├── doctors/          # Doctor management app
├── patients/         # Patient management app
├── users/           # User authentication and management
├── mappings/        # Mapping functionality
├── healthcare_backend/  # Main project settings
├── manage.py        # Django management script
└── requirements.txt # Project dependencies
```

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/healthcare-management-system.git
   cd healthcare-management-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv rest_api_env
   
   # On Windows
   rest_api_env\Scripts\activate
   
   # On macOS/Linux
   source rest_api_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   cd healthcare_backend
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the `healthcare_backend` directory with the following variables:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DATABASE_URL=postgresql://username:password@localhost:5432/healthcare_db
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser** (Optional)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication
- `POST /users/register/` - User registration
- `POST /users/login/` - User login
- `POST /users/token/refresh/` - Refresh JWT token

### Patients
- `GET /patients/` - List all patients
- `POST /patients/` - Create new patient
- `GET /patients/{id}/` - Get patient details
- `PUT /patients/{id}/` - Update patient
- `DELETE /patients/{id}/` - Delete patient

### Doctors
- `GET /doctors/` - List all doctors
- `POST /doctors/` - Create new doctor
- `GET /doctors/{id}/` - Get doctor details
- `PUT /doctors/{id}/` - Update doctor
- `DELETE /doctors/{id}/` - Delete doctor

### Mappings
- `GET /mappings/` - List all mappings
- `POST /mappings/` - Create new mapping

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
This project follows PEP 8 coding standards. You can check code style using:
```bash
flake8 .
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please feel free to open an issue on GitHub.

## Author

**Rahul Kumar**

---

*Built with ❤️ using Django and Django REST Framework*


