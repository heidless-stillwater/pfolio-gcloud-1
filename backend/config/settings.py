import environ
import os
from pathlib import Path

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

print("****************************")
print("****** SETTINGS ***********")
print("BASE_DIR:", BASE_DIR)
print("SECRET_KEY:", env('SECRET_KEY'))
print("DEBUG:", env('DEBUG'))
print("****************************")
print("****************************")


SECRET_KEY = env('SECRET_KEY')

print("DEBUG::", env('DEBUG'))

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = bool(int(os.environ.get('DEBUG',0)))
#print("DEBUG::", env('DEBUG'))
DEBUG=env('DEBUG')

#DEBUG = False

ALLOWED_HOSTS = [
    '0.0.0.0',
    'backend',
    'localhost',
    '127.0.0.1',
    '*',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'rest_framework',
    'corsheaders',

    # Local
    'about',
    'projects',
    'technologies',
    'contact',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hpfolio',
        'USER': 'heidless',
        'PASSWORD': 'havana11',
        'HOST': 'localhost',
        'PORT': '', # leave blank so the default port is selected
#        'PORT': '', # leave blank so the default port is selected
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': env('POSTGRES_DB'),
#        'USER': env('POSTGRES_USER'),
#        'PASSWORD': env('POSTGRES_PASSWORD'),
#        'HOST': env('POSTGRES_HOST'),
#        'PORT': '', # leave blank so the default port is selected
#        'PORT': '', # leave blank so the default port is selected
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# MEDIA_ROOT is for the user-uploaded content

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOWED_ORIGINS = [
    env('FRONTEND_URL'),
]
 
FILE_UPLOAD_PERMISSIONS=0o640

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = 'AKIAYUPGERUWX4LIA47Z'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'hpfolio-upload-bucket'
AWS_QUERYSTRING_AUTH = False
