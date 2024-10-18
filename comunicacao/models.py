from django.db import models

class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return f'{self.nome} ({self.email})'
