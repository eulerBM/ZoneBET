# Generated by Django 4.2.4 on 2023-08-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_jogo_status_alter_jogo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Em jogo', 'Em jogo'), ('Fechado', 'Fechado')], max_length=8, verbose_name='Status'),
        ),
    ]
