# Generated by Django 3.1.5 on 2021-02-07 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(default='Open', max_length=10),
            preserve_default=False,
        ),
    ]