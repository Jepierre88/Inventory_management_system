# Configuraciones específicas para producción
from .base import *

# Configuración de depuración
DEBUG = False

# Hosts permitidos
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['example.com'])

# Configuración de seguridad
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True