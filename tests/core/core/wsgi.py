import os
from microdjango.core.handlers import get_wsgi_application

os.environ.setdefault('MICRODJANGO_SETTINGS_MODULE', 'project_name.settings')

application = get_wsgi_application()
