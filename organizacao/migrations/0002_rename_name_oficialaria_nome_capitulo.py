# Generated by Django 4.2.2 on 2023-06-16 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizacao', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oficialaria',
            old_name='name',
            new_name='nome',
        ),
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=80)),
                ('endereco', models.CharField(max_length=80)),
                ('loja_patrocinadora', models.CharField(max_length=80)),
                ('oficialaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capitulos', to='organizacao.oficialaria')),
            ],
            options={
                'ordering': ['-date_created'],
                'abstract': False,
            },
        ),
    ]
