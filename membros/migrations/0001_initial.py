# Generated by Django 4.2.2 on 2023-06-21 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('id_demolay', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=85)),
                ('iniciacao', models.DateField()),
                ('data_nascimento', models.DateField()),
            ],
            options={
                'ordering': ['-date_created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MembroCastelo',
            fields=[
                ('membro_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='membros.membro')),
                ('castelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacao.castelo')),
            ],
            options={
                'ordering': ['-date_created'],
                'abstract': False,
            },
            bases=('membros.membro',),
        ),
        migrations.CreateModel(
            name='MembroCapitulo',
            fields=[
                ('membro_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='membros.membro')),
                ('capitulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacao.capitulo')),
            ],
            options={
                'ordering': ['-date_created'],
                'abstract': False,
            },
            bases=('membros.membro',),
        ),
    ]
