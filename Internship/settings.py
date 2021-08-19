from os.path import join
# import django_heroku
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse_lazy
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = 'django-insecure-os1iwsj-zywg7d6n_anxygtpg=79uuzl2&sy6)8h#5y1cn)=d5'

DEBUG = False

ALLOWED_HOSTS = ['internship-2021.herokuapp.com', '127.0.0.1']

INSTALLED_APPS = [
    'Internship',
    'Internship.internship_app',
    'Internship.internship_auth',
    'Internship.internship_profiles',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',

    'debug_toolbar',

    'django_summernote',
    'crispy_forms'

]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'Internship.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'Internship.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'internship_db',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd4c6e25piing9j',
        'USER': 'vljfgzrddxlaej',
        'PASSWORD': '80dd46182054771d2f4cf2a190ffbb27cafd94ed95361f80f3cd79e7ef3d4550',
        'HOST': 'ec2-54-76-249-45.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (join(BASE_DIR, 'static'),)

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media')

LOGIN_URL = reverse_lazy('sign in')

AUTH_USER_MODEL = 'internship_auth.InternshipUser'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SUMMERNOTE_THEME = 'bs4'

X_FRAME_OPTIONS = 'SAMEORIGIN'

# django_heroku.settings(locals())
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

cloudinary.config(
    cloud_name="dhavld11j",
    api_key="137955467533472",
    api_secret="zmrAQXommqofywnVJENgkIk9sx8",
    secure=True
)
