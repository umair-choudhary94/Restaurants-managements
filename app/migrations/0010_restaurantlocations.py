# Generated by Django 4.1.3 on 2023-05-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_foodorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='restaurantlocations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='Nothing', max_length=100)),
            ],
        ),
    ]
