# Generated by Django 4.1.3 on 2023-05-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='seats',
            field=models.IntegerField(default=0),
        ),
    ]
