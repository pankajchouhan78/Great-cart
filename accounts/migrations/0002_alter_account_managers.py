# Generated by Django 4.2.4 on 2023-08-11 13:31

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('Objects', django.db.models.manager.Manager()),
            ],
        ),
    ]