# Generated by Django 4.1.3 on 2023-05-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_delete_restaurantlocations'),
    ]

    operations = [
        migrations.CreateModel(
            name='restaurantcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='Nothing', max_length=400)),
            ],
        ),
    ]
