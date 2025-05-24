import os
import sys

# Path to your project directory (contains manage.py)
project_path = '/home/nhan1111/Lokki_Store'
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Path to your Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'phone_store.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
