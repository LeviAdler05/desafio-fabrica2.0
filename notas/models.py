from django.db import models

class Nota(models.Model):
    # Define um campo para armazenar o título da nota. 
    
    titulo = models.CharField(max_length=100)
    # CharField com o comprimento máximo de 100 caracteres.
    
    # Define um campo para armazenar o conteúdo da nota. 
    
    conteudo = models.TextField()
    
    # Define um campo para armazenar a data e hora em que a nota foi criada.
    # Usa DateTimeField com auto_now_add=True para definir automaticamente a data e hora no momento da criação da nota.
    data_criacao = models.DateTimeField(auto_now_add=True)

    # Retorna o título da nota quando o objeto Nota é convertido para uma string.
    def __str__(self):
        return self.titulo

