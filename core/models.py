from django.db import models
from enum import Enum

class ProductType(Enum): 
    DIGITAL = "Digital"
    FISICO = "Físico"

class ProductFileFormat(Enum):  
    PDF = "PDF"
    MP4 = "MP4"

class Product(models.Model):
    produtorId = models.ForeignKey('accounts.User', verbose_name='Produtor Principal', related_name='meusProdutos', on_delete=models.CASCADE)
    # Perguntar a Gileno se a linha abaixo faz sentido
    segundoProdutorId = models.ForeignKey('accounts.User', verbose_name='Segundo Produtor', related_name='produtosAfiliacao', blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField('Identificador', max_length=100)
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    disponivelEstoque = models.BooleanField("Disponível no estoque", default=False)
    quantidadeEstoque = models.IntegerField("Quantidade no estoque")
    afiliadoComissao = models.DecimalField("Comissão do afiliado", decimal_places=2, max_digits=5)
    desconto = models.DecimalField("Desconto", decimal_places=2, max_digits=5)
    emPromocao = models.BooleanField("Em promoção", default=False)
    tipo = models.CharField('Tipo', max_length=5, choices=[(tag, tag.value) for tag in ProductType])
    tamanho = models.DecimalField("Tamanho [MB]", decimal_places=2, max_digits=15)
    formato = models.CharField('Formato', max_length=5, choices=[(tag, tag.value) for tag in ProductFileFormat])
    dataCriacao = models.DateTimeField('Criado em', auto_now_add=True)
    dataModificacao = models.DateTimeField('Última modificação', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']

    def save(self):
        self.save()

    def __str__(self):
        return self.nome

class ProductAffiliated(models.Model):
    productId = models.ForeignKey('core.Product', verbose_name='Id do Produto', on_delete=models.CASCADE)
    affiliatedId = models.ForeignKey('accounts.User', verbose_name='Id do Afiliado', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Afiliado a um produto'
        verbose_name_plural = 'Afiliados a um produto'
