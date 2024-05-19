from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Products(models.Model):
    nome_vendedor = models.CharField(max_length=100)
    nome_loja = models.CharField(max_length=100)
    nome_produto = models.CharField(max_length=200)
    quantidade_coletada = models.IntegerField(validators=[MaxValueValidator(10)])
    lote = models.CharField(max_length=50)
    data_fabricacao = models.DateField()
    motivo_da_coleta = models.TextField()
    data_da_coleta = models.DateField()
    troca_confirmada = models.BooleanField(
        default=False
    )  # Campo booleano para indicar se a troca foi confirmada
