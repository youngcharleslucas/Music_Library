
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9u3upi6bb(3a^0ldt&s+umda3np#)c-72cwf(o*mw*iow-ud3u'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'QAZwsx12!@',
        'HOST': '127.0.0.1',
        'PORT' : '3306',
        'OPTIONS' : {
            'autocommit': True
        }
    }
}
