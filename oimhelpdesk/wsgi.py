import confy
from django.core.wsgi import get_wsgi_application
import os
from pathlib import Path


# These lines are required for interoperability between local and container environments.
d = Path(__file__).resolve().parents[1]
dot_env = os.path.join(str(d), '.env')
if os.path.exists(dot_env):
    confy.read_environment_file(dot_env)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oimhelpdesk.settings")
application = get_wsgi_application()
