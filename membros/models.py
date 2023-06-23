from django.db import models
from helpers.tracker import ModelTimestamps
from organizacao.models import Capitulo,  Castelo


class Membro(ModelTimestamps):
    id_demolay = models.CharField( max_length=10)
    nome = models.CharField( max_length=85)
    iniciacao = models.DateField()
    data_nascimento = models.DateField()
    def __str__(self):
        return self.nome

class MembroCastelo(Membro):
    castelo = models.ForeignKey(Castelo, on_delete=models.CASCADE)

class MembroCapitulo(Membro):
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)

