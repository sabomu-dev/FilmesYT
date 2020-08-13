# Generated by Django 3.0.7 on 2020-08-03 03:30

from django.db import migrations, models
import filmes.models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lancamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cria', models.DateField(auto_now_add=True, verbose_name='Postado')),
                ('data_act', models.DateField(auto_now=True, verbose_name='Actualizado')),
                ('Activ', models.BooleanField(default=True, verbose_name='Esta activo?')),
                ('image', stdimage.models.StdImageField(upload_to=filmes.models.get_file_path, verbose_name='Imagem do filme')),
                ('nome_film', models.CharField(max_length=100, verbose_name='Nome do filme')),
                ('genero', models.CharField(max_length=50, verbose_name='Género')),
                ('descricao', models.TextField(max_length=1000, verbose_name='Simpose')),
            ],
            options={
                'verbose_name': 'Lançamento',
                'verbose_name_plural': 'Lançamentos',
            },
        ),
        migrations.CreateModel(
            name='Misturados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cria', models.DateField(auto_now_add=True, verbose_name='Postado')),
                ('data_act', models.DateField(auto_now=True, verbose_name='Actualizado')),
                ('Activ', models.BooleanField(default=True, verbose_name='Esta activo?')),
                ('image', stdimage.models.StdImageField(upload_to=filmes.models.get_file_path, verbose_name='Imagem do filme')),
                ('nome_film', models.CharField(max_length=100, verbose_name='Nome do filme')),
                ('genero', models.CharField(max_length=50, verbose_name='Género')),
                ('simpose', models.CharField(max_length=1000, verbose_name='Simpose')),
            ],
            options={
                'verbose_name': 'Misturado',
                'verbose_name_plural': 'Misturados',
            },
        ),
    ]