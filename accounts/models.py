from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from phone_field import PhoneField
from enum import Enum
from django.template.defaultfilters import slugify

<<<<<<< HEAD
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
=======

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

>>>>>>> 2de61abb52edc5456bba7a7913595b33133d95c9

class User(models.Model):
    slug = models.SlugField('Identificador', max_length=100, unique=True)
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
    isAtivo = models.BooleanField("Ativo", default=True)

    dataCriacao = models.DateTimeField('Criado em', auto_now_add=True)
    dataModificacao = models.DateTimeField('Última modificação', auto_now=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nome']

    # def save(self):
<<<<<<< HEAD
        # self.save()
    
=======
    # self.save()

>>>>>>> 2de61abb52edc5456bba7a7913595b33133d95c9
    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.nome)
        super().save(*args, **kwargs)

<<<<<<< HEAD
    def __str__(self):
=======
    def _str_(self):
>>>>>>> 2de61abb52edc5456bba7a7913595b33133d95c9
        return self.nome