from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pedido(models.Model):
    STATUS = (('A', 'Aprovado'), ('C', 'Criado'), ('R', 'Reprovado'),
              ('P', 'Pendente'), ('E', 'Enviado'), ('F', 'Finalizado'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(choices=STATUS, max_length=1, default='C')

    def __str__(self):
        return f'Pedido N.{self.pk}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField()
    variacao = models.CharField(max_length=255)
    variacao_id = models.PositiveIntegerField()
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField(max_length=2000)

    def __str__(self):
        return f'Item do {self.pedido}'

    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'