# Generated by Django 2.1.7 on 2019-04-06 19:32

import core.models
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.IntegerField(default='', max_length=11, verbose_name='CPF')),
                ('dataNascimento', models.DateField(default='', verbose_name='Data de Nascimento')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='E-mail')),
                ('emailConfirmado', models.BooleanField(default=False, verbose_name='E-mail confirmado')),
                ('senha', models.CharField(max_length=30, verbose_name='Senha')),
                ('telefone', phone_field.models.PhoneField(default='', help_text='Telefone para contato', max_length=31, verbose_name='Telefone')),
                ('cep', models.IntegerField(default='', verbose_name='CEP')),
                ('numeroCasa', models.IntegerField(default='', verbose_name='Número')),
                ('rua', models.CharField(default='', max_length=100, verbose_name='Rua')),
                ('bairro', models.CharField(default='', max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(default='', max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(default='', max_length=5, verbose_name='Estado')),
                ('complemento', models.CharField(default='', max_length=100, verbose_name='Complemento')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dataModificacao', models.DateTimeField(auto_now=True, verbose_name='Última modificação')),
            ],
            options={
                'verbose_name': 'Afiliado',
                'verbose_name_plural': 'Afiliados',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.IntegerField(default='', max_length=11, verbose_name='CPF')),
                ('dataNascimento', models.DateField(default='', verbose_name='Data de Nascimento')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='E-mail')),
                ('emailConfirmado', models.BooleanField(default=False, verbose_name='E-mail confirmado')),
                ('senha', models.CharField(max_length=30, verbose_name='Senha')),
                ('produtorPrincipal', models.BooleanField(default=False, verbose_name='Produtor Principal')),
                ('telefone', phone_field.models.PhoneField(default='', help_text='Telefone para contato', max_length=31, verbose_name='Telefone')),
                ('cep', models.IntegerField(default='', verbose_name='CEP')),
                ('numeroCasa', models.IntegerField(default='', verbose_name='Número')),
                ('rua', models.CharField(default='', max_length=100, verbose_name='Rua')),
                ('bairro', models.CharField(default='', max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(default='', max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(default='', max_length=5, verbose_name='Estado')),
                ('complemento', models.CharField(default='', max_length=100, verbose_name='Complemento')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dataModificacao', models.DateTimeField(auto_now=True, verbose_name='Última modificação')),
            ],
            options={
                'verbose_name': 'Produtor',
                'verbose_name_plural': 'Produtores',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('disponivelEstoque', models.BooleanField(default=False, verbose_name='Disponível no estoque')),
                ('quantidadeEstoque', models.IntegerField(verbose_name='Quantidade no estoque')),
                ('afiliadoComissao', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Comissão do afiliado')),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Desconto')),
                ('emPromocao', models.BooleanField(default=False, verbose_name='Em promoção')),
                ('tipo', models.CharField(choices=[(core.models.ProductType('Digital'), 'Digital'), (core.models.ProductType('Físico'), 'Físico')], max_length=5, verbose_name='Tipo')),
                ('tamanho', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Tamanho [MB]')),
                ('formato', models.CharField(choices=[(core.models.ProductFileFormat('PDF'), 'PDF'), (core.models.ProductFileFormat('MP4'), 'MP4')], max_length=5, verbose_name='Formato')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dataModificacao', models.DateTimeField(auto_now=True, verbose_name='Última modificação')),
                ('produtorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Manufacturer', verbose_name='Produtor')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['nome'],
            },
        ),
    ]
