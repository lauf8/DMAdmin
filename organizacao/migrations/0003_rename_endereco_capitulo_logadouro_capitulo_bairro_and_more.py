# Generated by Django 4.2.2 on 2023-06-21 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizacao', '0002_castelo_numero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capitulo',
            old_name='endereco',
            new_name='logadouro',
        ),
        migrations.AddField(
            model_name='capitulo',
            name='bairro',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='capitulo',
            name='cidade',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]
