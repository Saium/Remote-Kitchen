from pathlib import Path
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.environ.get("DB_NAME"),
        'NAME': 'food_db',
        # 'USER': os.environ.get("DB_USER"),
        'USER': 'root',
        # 'PASSWORD': os.environ.get("DB_PASSWORD"),
        'PASSWORD': 'asdf',
        'OPTIONS': {
            'sql_mode': 'traditional',
            'init_command': "SET time_zone='+00:00'",
        },
    }
}


