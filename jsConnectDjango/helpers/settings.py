# Django imports
from django.conf import settings

# Defaults
TIMEOUT = 24 * 60 # 24 minutes


# Fetch settings
PHOTO_BACKEND = getattr(settings, 'JS_CONNECT_PHOTO_BACKEND', None)
CLIENT_ID = getattr(settings, 'JS_CONNECT_CLIENT_ID', None)
SECRET = getattr(settings, 'JS_CONNECT_SECRET', None)

# Check for errors
if not SECRET or not CLIENT_ID:
    raise Exception("JS_CONNECT_SECRET and JS_CONNECT_CLIENT_ID are not configured correctly")