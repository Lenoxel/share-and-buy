from django.db import models
from enum import Enum
from phone_field import PhoneField
from localflavor.br.forms import BRCPFField, BRCNPJField, BRZipCodeField

class ProductType(Enum): 
    DIGITAL = "Digital"
    FISICO = "Físico"

class ProductFileFormat(Enum):  
    PDF = "PDF"
    MP4 = "MP4"

class BRStates(Enum):
   AC = "Acre"
   AL = "Alagoas"
   AP = "Amapá"
   AM = "Amazonas"
   BA = "Bahia"
   CE = "Ceará"
   DF = "Distrito Federal"
   ES = "Espírito Santo"
   GO = "Goiás"
   MA = "Maranhão"
   MT = "Mato Grosso"
   MS = "Mato Grosso do Sul"
   MG = "Minas Gerais"
   PA = "Pará"
   PB = "Paraíba"
   PR = "Paraná"
   PE = "Pernambuco"
   PI = "Piauí"
   RJ = "Rio de Janeiro"
   RN = "Rio Grande do Norte"
   RS = "Rio Grande do Sul"
   RO = "Rondônia"
   RR = "Roraima"
   SC = "Santa Catarina"
   SP = "São Paulo"
   SE = "Sergipe"
   TO = "Tocantins"

class Product(models.Model):
    produtorId = models.ForeignKey('core.User', verbose_name='Produtor Principal', related_name='meusProdutos', on_delete=models.CASCADE)
    # Perguntar a Gileno se a linha abaixo faz sentido
    segundoProdutorId = models.ForeignKey('core.User', verbose_name='Segundo Produtor', related_name='produtosAfiliacao', blank=True, null=True, on_delete=models.CASCADE)
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

class User(models.Model):
    slug = models.SlugField('Identificador', max_length=100)
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, default='')
    dataNascimento = models.DateField('Data de Nascimento', default='')
    email = models.EmailField('E-mail', max_length=40, unique=True)
    emailConfirmado = models.BooleanField('E-mail confirmado', default=False)
    senha = models.CharField('Senha', max_length=30)
    telefone = PhoneField('Telefone', help_text='Telefone para contato', default='')
    cep = models.CharField('CEP', max_length=8, default='')
    numeroCasa = models.IntegerField('Número', default='')
    rua = models.CharField('Rua', max_length=100, default='')
    bairro = models.CharField('Bairro', max_length=100, default='')
    cidade = models.CharField('Cidade', max_length=100, default='')
    estado = models.CharField('Estado', max_length=5, choices=[(tag, tag.value) for tag in BRStates])
    complemento = models.CharField('Complemento', max_length=100, default='')

    isProdutor = models.BooleanField("Produtor", default=False)
    isAfiliado = models.BooleanField("Afiliado", default=False)

    dataCriacao = models.DateTimeField('Criado em', auto_now_add=True)
    dataModificacao = models.DateTimeField('Última modificação', auto_now=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nome']

    def save(self):
        self.save()

    def __str__(self):
        return self.nome

class ProductAffiliated(models.Model):
    productId = models.PositiveIntegerField()
    affiliatedId = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Afiliado a um produto'
        verbose_name_plural = 'Afiliados a um produto'
