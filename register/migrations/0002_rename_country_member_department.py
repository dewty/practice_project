# Generated by Django 5.1.3 on 2024-11-17 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='country',
            new_name='department',
        ),
    ]
