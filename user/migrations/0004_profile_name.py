# Generated by Django 3.1.5 on 2021-01-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='ab', max_length=50),
            preserve_default=False,
        ),
    ]
