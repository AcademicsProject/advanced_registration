# Generated by Django 2.2.5 on 2021-01-28 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
