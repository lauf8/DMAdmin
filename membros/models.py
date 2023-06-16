from django.db import models
from helpers.tracker import ModelTimestamps
from organizacao.models import Capitulo, Gestao
from django.contrib.auth.models import User

class MembroCapitulo(ModelTimestamps):
    id_demolay = models.CharField( max_length=10)
    nome = models.CharField( max_length=85)
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)
    iniciacao = models.DateField()

class Escrivao(User):
    id_demolay = models.CharField(max_length=10)
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)
    gestao = models.ForeignKey(Gestao, on_delete=models.CASCADE)
    iniciacao = models.DateField()


class MestreConselheiro(User):
    id_demolay = models.CharField(max_length=10)
    gestao = models.ForeignKey(Gestao, on_delete=models.CASCADE)
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)
    iniciacao = models.DateField()
