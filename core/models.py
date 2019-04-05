from django.db import models
from enum import Enum

class ProductType(Enum): 
    DIGITAL = "Digital"
    FISICO = "Físico"

class ProductFileFormat(Enum):  
    PDF = "PDF"
    MP4 = "MP4"

class Product(models.Model):
    produtorId = models.ForeignKey('core.Manufacturer', verbose_name='Produtor', on_delete=models.CASCADE)
    slug = models.SlugField('Identificador', max_length=100)
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    disponivelEstoque = models.BooleanField("Disponível no estoque", default=False)
    quantidadeEstoque = models.IntegerField("Quantidade no estoque")
    afiliadoComissao = models.FloatField("Comissão do afiliado", decimal_places=2, max_digits=5)
    desconto = models.FloatField("Desconto", decimal_places=2, max_digits=5)
    emPromocao = models.BooleanField("Em promoção", default=False)
    tipo = models.CharField('Tipo', max_length=5, choices=[(tag, tag.value) for tag in ProductType])
    tamanho = models.FloatField("Tamanho [MB]", decimal_places=2, max_digits=15)
    formato = models.CharField('Formato', max_length=5, choices=[(tag, tag.value) for tag in ProductFileFormat])
    dataCriacao = models.DateTimeField('Criado em', auto_now_add=True)
    dataModificacao = models.DateTimeField('Última modificação', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    slug = models.SlugField('Identificador', max_length=100)
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=40, unique= True)
    senha = models.CharField('Senha', max_length=30)
    produtorPrincipal = models.BooleanField("Produtor Principal", default=False)

    dataCriacao = models.DateTimeField('Criado em', auto_now_add=True)
    dataModificacao = models.DateTimeField('Última modificação', auto_now=True)

    class Meta:
        verbose_name = 'Produtor'
        verbose_name_plural = 'Produtores'
        ordering = ['nome']

    def __str__(self):
        return self.name


class Affiliated(models.Model):
    slug = models.SlugField('Identificador', max_length=100)
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=40, unique= True)
    senha = models.CharField('Senha', max_length=30)

    dataCriacao = models.DateTimeField('Criado em', auto_now_add=True)
    dataModificacao = models.DateTimeField('Última modificação', auto_now=True)

    class Meta:
        verbose_name = 'Afiliado'
        verbose_name_plural = 'Afiliados'
        ordering = ['nome']

    def __str__(self):
        return self.name

