# Generated by Django 3.1.4 on 2022-05-05 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20220502_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='author',
        ),
    ]
