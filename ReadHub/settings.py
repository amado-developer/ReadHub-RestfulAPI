"""
Django settings for ReadHub project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c_m7(8ins*x$$m*5qm^z%j8d5eklh)dr&u890hy$f@t@r$xj^!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.255', '10.120.61.149', '10.0.2.2', 'localhost', '127.0.0.1', '192.168.1.6', '192.168.1.5']

CORS_ORIGIN_ALLOW_ALL =  True
# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth',
    'rest_auth.registration',
    'guardian',
    'corsheaders',

    'equipments.apps.EquipmentsConfig',
    'magazines.apps.MagazinesConfig',
    'comments.apps.CommentsConfig',
    'storebranches.apps.StorebranchesConfig',
    'studyclassrooms.apps.StudyclassroomsConfig',
    'equipment_assigments.apps.EquipmentAssigmentsConfig',
    'digital_books.apps.DigitalBooksConfig',
    'audio_books.apps.AudioBooksConfig',
    'promotions.apps.PromotionsConfig',
    'studyclassrooms_reservations.apps.StudyclassroomsReservationsConfig',
    'magazinesPDF.apps.MagazinespdfConfig',

    'books.apps.BooksConfig',
    'authors.apps.AuthorsConfig',
    'users.apps.UsersConfig',

    'logs.apps.LogsConfig',
    'adquisitions.apps.AdquisitionsConfig',
    'bookcollections.apps.BookcollectionsConfig',
    'electronicbookcollections.apps.ElectronicbookcollectionsConfig',
    'magazinecollections.apps.MagazinecollectionsConfig',
    'events.apps.EventsConfig',
    'wishlists.apps.WishlistsConfig',
    'inventories.apps.InventoriesConfig',
    'permissions.apps.PermissionsConfig',
    'digitalBooksPDF.apps.DigitalbookspdfConfig',
    'bookloans.apps.BookloansConfig',
    'equipmentloans.apps.EquipmentloansConfig',
    'paymentoptions.apps.PaymentoptionsConfig'
]

AUTH_USER_MODEL = 'users.User'

# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = None
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/?verification=1'
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/?verification=1'
# SITE_ID = 1
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# REST_AUTH_SERIALIZERS = {
#     'USER_DETAILS_SERIALIZER': 'users.serializers.UserSerializer',
# }

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

JWT_AUTH = {
'JWT_ALLOW_REFRESH' : True,
'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=48),
'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', 
    'guardian.backends.ObjectPermissionBackend'
)

ROOT_URLCONF = 'ReadHub.urls'

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

WSGI_APPLICATION = 'ReadHub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ReadHub',
        'USER': 'postgres',
        'PASSWORD': 'Anikalinda11',
        'HOST' : 'localhost',
        'PORT' : '5432',

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static-server', 'media_root')
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
