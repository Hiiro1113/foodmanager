import os

#settings.pyからそのままコピー
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = ')(#%2!@hhf!@8)5zfd(z@y^(x@ru%uq!$#)h38db^50q+znt-d'


#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'normaluser',
        'PASSWORD': 'normaluser',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DEBUG = True #ローカルでDebugできるようになります