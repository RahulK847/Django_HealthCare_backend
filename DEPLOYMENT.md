# 🚀 Deploy Django Healthcare Backend on Render

## Prerequisites
- GitHub repository: https://github.com/RahulK847/Django_HealthCare_backend
- Render account: https://render.com

## Step 1: Create Database on Render

1. **Login to Render** → Click **"New +"** → **"PostgreSQL"**
2. **Configuration:**
   - Name: `healthcare-db`
   - Database: `healthcare_db`
   - User: `healthcare_user`
   - Plan: Free
3. **Click "Create Database"**
4. **Copy the External Database URL** (you'll need this)

## Step 2: Deploy Web Service

1. **Click "New +"** → **"Web Service"**
2. **Connect Repository:** `RahulK847/Django_HealthCare_backend`
3. **Configuration:**
   - Name: `healthcare-backend`
   - Branch: `main`
   - Root Directory: `healthcare_backend`
   - Runtime: `Python 3`
   - Build Command: `./build.sh`
   - Start Command: `gunicorn healthcare_backend.wsgi:application`

## Step 3: Environment Variables

Add these environment variables in Render:

```bash
DATABASE_URL=<your-postgres-external-url>
SECRET_KEY=django-healthcare-secret-key-2025
DEBUG=False
PYTHONPATH=/opt/render/project/src/healthcare_backend
```

## Step 4: Update Settings

Update your `healthcare_backend/settings.py`:

```python
import os
import dj_database_url
from decouple import config

# Production settings
SECRET_KEY = config('SECRET_KEY', default='django-insecure-)p2867eq=6^+#0=+y2@59e_xrrni51u2!xxj8k%qcl0f6@7cpn')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',
]

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://postgres:sql@localhost:5432/healthcare_db',
        conn_max_age=600
    )
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add whitenoise to middleware
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
```

## Step 5: Deploy

1. **Push changes to GitHub** (if you made any)
2. **Click "Deploy"** in Render dashboard
3. **Wait for deployment** (usually 3-5 minutes)
4. **Your API will be live at:** `https://healthcare-backend.onrender.com`

## Step 6: Test Your Deployed API

```bash
# Test registration
curl -X POST https://healthcare-backend.onrender.com/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "Test@123", "role": "patient"}'

# Test login
curl -X POST https://healthcare-backend.onrender.com/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "Test@123"}'
```

## Troubleshooting

### Common Issues:
1. **Build fails:** Check `build.sh` permissions
2. **Database errors:** Verify DATABASE_URL
3. **Static files:** Ensure whitenoise is configured
4. **Environment variables:** Double-check all env vars

### Logs:
- Check Render logs for detailed error messages
- Use `python manage.py check --deploy` for production checklist

## Success! 🎉

Your Django Healthcare Backend is now live on Render!

**Live URL:** `https://healthcare-backend.onrender.com`
**Admin:** `https://healthcare-backend.onrender.com/admin/`
**API Docs:** Check your README.md for endpoints
