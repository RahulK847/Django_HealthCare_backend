# Production settings additions
import os
import dj_database_url
from decouple import config

# Add these to your settings.py for production deployment

# Environment-based configuration
SECRET_KEY = config('SECRET_KEY', default='django-insecure-)p2867eq=6^+#0=+y2@59e_xrrni51u2!xxj8k%qcl0f6@7cpn')
DEBUG = config('DEBUG', default=False, cast=bool)

# Allowed hosts for Render
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',
]

# Database configuration for Render
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://postgres:sql@localhost:5432/healthcare_db',
        conn_max_age=600
    )
}

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Whitenoise middleware for serving static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
