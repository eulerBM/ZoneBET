# Generated by Django 4.2.4 on 2023-08-31 07:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_user_money_currency_alter_user_money'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='user_money',
        ),
    ]