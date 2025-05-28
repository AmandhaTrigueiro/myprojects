from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField()
    cnpj = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Sistema(models.Model):
    nome = models.CharField()

    def __str__(self):
        return self.nome


class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="contrato")
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, related_name="contrato")
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    inicio = models.DateField()
    termino = models.DateField()

    def __str__(self):
        return f"{self.cliente} - {self.sistema}"
