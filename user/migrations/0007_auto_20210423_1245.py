# Generated by Django 3.1.5 on 2021-04-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_profile_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='roll',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
