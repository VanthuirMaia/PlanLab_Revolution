# Generated by Django 5.1.1 on 2024-10-09 01:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.CharField(max_length=100)),
                ('data_aula', models.DateField()),
                ('turma', models.CharField(max_length=100)),
                ('semestre', models.CharField(max_length=10)),
                ('titulo', models.CharField(max_length=200)),
                ('conteudo_programatico', models.TextField()),
                ('metodologia', models.TextField()),
                ('recursos_necessarios', models.TextField()),
                ('avaliacao_observacoes', models.TextField()),
                ('observacoes', models.TextField()),
                ('eventos_extraordinarios', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlanLab.usuario')),
            ],
        ),
    ]
