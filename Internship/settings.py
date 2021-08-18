from os.path import join
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = 'django-insecure-os1iwsj-zywg7d6n_anxygtpg=79uuzl2&sy6)8h#5y1cn)=d5'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'internship_db',
        'USER': 'postgres',
        'PASSWORD': '1234qwe',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    BASE_DIR / "static",
)

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media/')
LOGIN_URL = reverse_lazy('sign in')

AUTH_USER_MODEL = 'internship_auth.InternshipUser'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SUMMERNOTE_THEME = 'bs4'

X_FRAME_OPTIONS = 'SAMEORIGIN'