# settings.py (base o principal)

import environ
from pathlib import Path

# Inicializar entorno
env = environ.Env()
environ.Env.read_env(env_file=str(Path(__file__).resolve().parent.parent.parent / '.env'))

# Ruta base del proyecto (sube tres niveles si estás en settings dentro de una subcarpeta)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Clave secreta desde el .env
SECRET_KEY = env('SECRET_KEY')

# Debug desde el entorno, por defecto True
DEBUG = env.bool('DEBUG', default=True)

# Hosts permitidos
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=["*"])

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps de terceros
    'rest_framework',
    'rest_framework.authtoken',

    # Apps locales
    'category_management',
    'item_management',
    'stock_management',
    'supplier_management',
    'transaction_management',
    'business_management',
    'auth_management',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Usuario personalizado
AUTH_USER_MODEL = 'auth_management.AuthUser'

# Configuración de URLs
ROOT_URLCONF = 'inventory_management_project.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuración de WSGI
WSGI_APPLICATION = 'inventory_management_project.wsgi.application'

# Base de datos (puedes adaptar para PostgreSQL o MySQL desde .env)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos y multimedia
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Campo por defecto para claves primarias
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
