# Generated by Django 3.1.5 on 2021-02-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20210209_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False, unique=True),
        ),
    ]
