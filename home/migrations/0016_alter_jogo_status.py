# Generated by Django 4.2.4 on 2023-09-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_delete_aposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Fechado', 'Fechado')], max_length=8, verbose_name='Status'),
        ),
    ]
