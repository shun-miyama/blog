import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'akatombo_django',
        'USER': 'harishanti',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}


DEBUG = True