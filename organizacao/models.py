from django.db import models
from helpers.tracker import ModelTimestamps

from django.contrib.auth.models import User

class MestreConselheiroEstadual(User):
    id_demolay_demolay = models.CharField( max_length=10)
    

class GrandeConscelho(User):
    id_demolay = models.CharField( max_length=10)
    
class Oficialaria(ModelTimestamps):
    nome = models.CharField(max_length=30)
    def __str__(self):
        return self.nome

class OficialExecutivo(User):
    id_demolay = models.CharField( max_length=10)
    oficialaria = models.ForeignKey(Oficialaria, related_name='oficiais_executivos', on_delete=models.CASCADE)
    

class MestreConselheiroRegional(User):
    id_demolay = models.CharField( max_length=10)
    oficialaria = models.ForeignKey(Oficialaria, related_name='mestres_conselheiros', on_delete=models.CASCADE)
    
class Capitulo(ModelTimestamps):
    nome = models.CharField(max_length=80)
    endereco = models.CharField(max_length =80)
    loja_patrocinadora = models.CharField(max_length=80)
    oficialaria = models.ForeignKey(Oficialaria, related_name='capitulos', on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Gestao(ModelTimestamps):
    nome = models.CharField(max_length=50) 
    comeco = models.DateField()
    final = models.DateField()

    def __str__(self):
        return self.nome

    
    


    

