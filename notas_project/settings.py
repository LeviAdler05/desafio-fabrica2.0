from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-_(9%!oq%-36^h#t=!n3cdu)+cyyj1y_e#(u#whnk$3$ktz9-dh'


DEBUG = True


ALLOWED_HOSTS = []


# Definição da aplicação

INSTALLED_APPS = [
    'django.contrib.admin',  
    'django.contrib.auth',   
    'django.contrib.contenttypes',  
    'django.contrib.sessions',  
    'django.contrib.messages',  
    'django.contrib.staticfiles',  
    'notas',  # Inclui o aplicativo 'notas' 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  
    'django.contrib.sessions.middleware.SessionMiddleware', 
    'django.middleware.common.CommonMiddleware',  
    'django.middleware.csrf.CsrfViewMiddleware',  
    'django.contrib.auth.middleware.AuthenticationMiddleware',  
    'django.contrib.messages.middleware.MessageMiddleware',  
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  
]

# Define o módulo de URL raiz para o projeto.
# Configurações de URL do projeto.
ROOT_URLCONF = 'notas_project.urls'

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



WSGI_APPLICATION = 'notas_project.wsgi.application'





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  
    }
}


# Validação de senha
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Valida a similaridade dos atributos do usuário
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Valida o comprimento mínimo da senha
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Valida se a senha não é comum
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Valida se a senha não é apenas numérica
    },
]


# Internacionalização
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'  # Define o código de idioma padrão como português do Brasil

TIME_ZONE = 'America/Fortaleza'
 

USE_I18N = True  
USE_TZ = True  


# Arquivos estáticos (CSS, JavaScript, Imagens)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'  # Define o URL base para arquivos estáticos

# Tipo de campo de chave primária padrão
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  
