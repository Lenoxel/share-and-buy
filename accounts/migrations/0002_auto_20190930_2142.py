# Generated by Django 2.1.7 on 2019-10-01 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Identificador'),
        ),
    ]
