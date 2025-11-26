import os
import sys
from django.core.wsgi import get_wsgi_application

# Add project to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'women_safety_platform.settings')

application = get_wsgi_application()

def handler(event, context):
    return application(event, context)