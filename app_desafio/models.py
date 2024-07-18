from django.db import models

class Equipamento(models.Model):
    id_equipamento = models.AutoField(primary_key=True)
    tipo = models.TextField(max_length=255, null=True)
    fabricante = models.TextField(max_length=255, null=True)
    modelo = models.TextField(max_length=255, null=True)
    numero_de_serie = models.TextField(max_length=255, null=True)
    data_de_compra = models.DateField(null=True)
    valor_da_compra = models.DecimalField(max_digits=10,decimal_places=2,null=True)