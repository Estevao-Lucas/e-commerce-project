from django.db import models
from django.conf import settings

from django.utils.text import slugify
from PIL import Image
import os

from utils import utils

# Create your models here.
class Produto(models.Model):
    TIPO = (('V', 'Variável'), ('S', 'Simples'))

    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m/',
                              blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField(verbose_name='Preço')
    preco_marketing_promocional = models.FloatField(default=0, verbose_name='Preço Promo')
    tipo = models.CharField(default='V', choices=TIPO, max_length=1)

    def get_preco_formatado(self):
        return utils.formata_preco(self.preco_marketing)

    def get_preco_promo_formatado(self):
        return utils.formata_preco(self.preco_marketing_promocional)

    get_preco_formatado.short_description = 'Preço'
    get_preco_promo_formatado.short_description = 'Preço Promocional'

    @staticmethod
    def resize_image(img, nova_largura=800):
        path_img = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(path_img)
        largura_original, altura_orginal = img_pil.size


        if largura_original <= nova_largura:
            img_pil.close()
            return

        nova_altura = round((nova_largura * altura_orginal)
                            / largura_original)

        nova_imagem = img_pil.resize((nova_largura, nova_altura),
                                     Image.LANCZOS)
        nova_imagem.save(
            path_img,
            optimize=True,
            quality = 50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem,max_image_size)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Produto'

class Variacao(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        db_table = 'Variacao'
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'