from django.db import models
from helpers.tracker import ModelTimestamps
from django.contrib.auth.models import Group, Permission

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

    
class Oficialaria(ModelTimestamps):
    nome = models.CharField(max_length=30)
    def __str__(self):
        return self.nome

class Capitulo(ModelTimestamps):
    nome = models.CharField(max_length=50)
    numero = models.IntegerField()
    logadouro = models.CharField(max_length =80)
    bairro = models.CharField(max_length =80)
    cidade = models.CharField(max_length =80)
    loja_patrocinadora = models.CharField(max_length=80)
    oficialaria = models.ForeignKey(Oficialaria, related_name='capitulos', on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    
class Castelo(ModelTimestamps):
    nome = models.CharField(max_length=80)
    numero = models.IntegerField()
    capitulo = models.ForeignKey(Capitulo,related_name='castelo', on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Gestao(ModelTimestamps):
    nome = models.CharField(max_length=10) 
    comeco = models.DateField()
    final = models.DateField()

    def __str__(self):
        return self.nome

class Lideranca(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=80)
    email =  models.EmailField()
    id_demolay = models.CharField(max_length=7)
    gestao = models.ForeignKey(Gestao,related_name='gestao', on_delete=models.CASCADE)
    capitulo = models.ForeignKey(Capitulo,related_name='capitulo', on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='liderancas')
    user_permissions = models.ManyToManyField(Permission, related_name='liderancas')




    



    

