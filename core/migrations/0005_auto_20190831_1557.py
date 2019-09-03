# Generated by Django 2.1.7 on 2019-08-31 18:57

import core.models
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190406_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAffiliated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.PositiveIntegerField()),
                ('affiliatedId', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Afiliado a um produto',
                'verbose_name_plural': 'Afiliados a um produto',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.CharField(default='', max_length=11, verbose_name='CPF')),
                ('dataNascimento', models.DateField(default='', verbose_name='Data de Nascimento')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='E-mail')),
                ('emailConfirmado', models.BooleanField(default=False, verbose_name='E-mail confirmado')),
                ('senha', models.CharField(max_length=30, verbose_name='Senha')),
                ('telefone', phone_field.models.PhoneField(default='', help_text='Telefone para contato', max_length=31, verbose_name='Telefone')),
                ('cep', models.CharField(default='', max_length=8, verbose_name='CEP')),
                ('numeroCasa', models.IntegerField(default='', verbose_name='Número')),
                ('rua', models.CharField(default='', max_length=100, verbose_name='Rua')),
                ('bairro', models.CharField(default='', max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(default='', max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(choices=[(core.models.BRStates('Acre'), 'Acre'), (core.models.BRStates('Alagoas'), 'Alagoas'), (core.models.BRStates('Amapá'), 'Amapá'), (core.models.BRStates('Amazonas'), 'Amazonas'), (core.models.BRStates('Bahia'), 'Bahia'), (core.models.BRStates('Ceará'), 'Ceará'), (core.models.BRStates('Distrito Federal'), 'Distrito Federal'), (core.models.BRStates('Espírito Santo'), 'Espírito Santo'), (core.models.BRStates('Goiás'), 'Goiás'), (core.models.BRStates('Maranhão'), 'Maranhão'), (core.models.BRStates('Mato Grosso'), 'Mato Grosso'), (core.models.BRStates('Mato Grosso do Sul'), 'Mato Grosso do Sul'), (core.models.BRStates('Minas Gerais'), 'Minas Gerais'), (core.models.BRStates('Pará'), 'Pará'), (core.models.BRStates('Paraíba'), 'Paraíba'), (core.models.BRStates('Paraná'), 'Paraná'), (core.models.BRStates('Pernambuco'), 'Pernambuco'), (core.models.BRStates('Piauí'), 'Piauí'), (core.models.BRStates('Rio de Janeiro'), 'Rio de Janeiro'), (core.models.BRStates('Rio Grande do Norte'), 'Rio Grande do Norte'), (core.models.BRStates('Rio Grande do Sul'), 'Rio Grande do Sul'), (core.models.BRStates('Rondônia'), 'Rondônia'), (core.models.BRStates('Roraima'), 'Roraima'), (core.models.BRStates('Santa Catarina'), 'Santa Catarina'), (core.models.BRStates('São Paulo'), 'São Paulo'), (core.models.BRStates('Sergipe'), 'Sergipe'), (core.models.BRStates('Tocantins'), 'Tocantins')], max_length=5, verbose_name='Estado')),
                ('complemento', models.CharField(default='', max_length=100, verbose_name='Complemento')),
                ('isProdutor', models.BooleanField(default=False, verbose_name='Produtor')),
                ('isAfiliado', models.BooleanField(default=False, verbose_name='Afiliado')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dataModificacao', models.DateTimeField(auto_now=True, verbose_name='Última modificação')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'ordering': ['nome'],
            },
        ),
        migrations.DeleteModel(
            name='Affiliated',
        ),
        migrations.AlterField(
            model_name='product',
            name='produtorId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meusProdutos', to='core.User', verbose_name='Produtor Principal'),
        ),
        migrations.DeleteModel(
            name='Manufacturer',
        ),
        migrations.AddField(
            model_name='product',
            name='segundoProdutorId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produtosAfiliacao', to='core.User', verbose_name='Segundo Produtor'),
        ),
    ]
