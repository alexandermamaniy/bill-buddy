
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-p^dqgpd_0f(6p@pi45cdn)9j=vo3b-mht9^4-#$lo^i)d%h_w)'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# TESTING = False

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL=True
CORS_ALLOW_CREDENTIALS = True
# ALLOWED_HOSTS = ['*']


# Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     #LOCAL_APPS
#     'core',
#     'billbuddy',
#     'users',
#     'buddy_profiles',
#     'buddy_expenses',
#     'buddy_groups',
#     #THRID_APPS
#     'rest_framework',
#     'corsheaders',
#     'rest_framework_simplejwt',
#     'drf_spectacular',
# ]

# REST_FRAMEWORK = {
#     # 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
#     'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework.renderers.JSONRenderer',
#     ],
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ]
# }
# #  base confoguration
#
# # SPECTACULAR_SETTINGS = {
# #     "TITTLE": "Django DRF Ecommerce",
# # }
#
# if DEBUG:
#     REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append(
#         'rest_framework.renderers.BrowsableAPIRenderer'
#     )
#     REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append(
#         'rest_framework.authentication.SessionAuthentication'
#     )
#
#
# if TESTING:
#     REST_FRAMEWORK = {
#         'DEFAULT_RENDERER_CLASSES': (
#             'rest_framework.renderers.JSONRenderer',
#             'rest_framework.renderers.BrowsableAPIRenderer',
#         ),
#         'DEFAULT_AUTHENTICATION_CLASSES': [
#             'rest_framework_simplejwt.authentication.JWTAuthentication',
#         ]
#     }


# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#
#     # Your custom timezone middleware
#     'buddy_profiles.middleware.TimezoneMiddleware',
# ]

# ROOT_URLCONF = 'billbuddy.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'billbuddy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mydatabase',
#         'USER': 'myuser',
#         'PASSWORD': 'mypassword',
#         'HOST': 'db',
#         'PORT': '3306',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Directory where collectstatic will store files
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
#
# # use custom authentications
# AUTH_USER_MODEL = 'users.User'

# Actual directory user files go to
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'mediafiles')
#
# # URL used to access the media
# MEDIA_URL = '/media/'