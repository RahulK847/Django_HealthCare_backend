#!/usr/bin/env bash
# exit on error
set -o errexit

# Change to the healthcare_backend directory
cd healthcare_backend

# Install dependencies
pip install -r requirements_production.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply migrations
python manage.py migrate
