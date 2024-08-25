import os

from django.core.asgi import get_asgi_application

# Define a variável de ambiente DJANGO_SETTINGS_MODULE com o caminho para o módulo de configurações do Django.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notas_project.settings')

# Obtém a aplicação ASGI do Django. 


application = get_asgi_application()
