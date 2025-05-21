#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python phone_store/manage.py collectstatic --no-input

# Run migrations
python phone_store/manage.py migrate