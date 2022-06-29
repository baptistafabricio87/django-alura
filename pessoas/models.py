from datetime import datetime
from django.db import models

# Create your models here.
class Pessoa(models.Model):    
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    dt_cadastro = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self) -> str:
        return self.nome