PREINSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

EXTERNAL_APPS = [
    'rest_framework',
    'rest_framework.authtoken',	
    'corsheaders',
]

PROJECT_APPS = [  
   'Account',
   'kitchen_api',

]

INSTALLED_APPS = PREINSTALLED_APPS + EXTERNAL_APPS + PROJECT_APPS