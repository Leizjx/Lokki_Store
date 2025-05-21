#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Navigate to project directory
cd phone_store

# Set Python path
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate