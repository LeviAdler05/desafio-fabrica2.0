from django.apps import AppConfig

class NotasConfig(AppConfig):
    # Define o tipo de campo padrão para chaves primárias geradas automaticamente.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nome do diretório do aplicativo.
    name = 'notas'
