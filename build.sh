#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Add the project directory to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(pwd)/phone_store

# Collect static files
python phone_store/manage.py collectstatic --no-input

# Run migrations
python phone_store/manage.py migrate