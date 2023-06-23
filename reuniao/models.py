from helpers.tracker import ModelTimestamps
from organizacao import models
from organizacao.models import Castelo
from django.db import models
from membros.models import MembroCastelo

class ReuniaoCastelo(ModelTimestamps):
    capitulo =  models.ForeignKey(Castelo, on_delete=models.CASCADE)
    data_criacao = models.DateField()
    membros_presentes = models.ManyToManyField(MembroCastelo)



