# Generated by Django 4.1.3 on 2023-05-09 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_restaurant_tables'),
    ]

    operations = [
        migrations.CreateModel(
            name='fooditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Nothing', max_length=1000)),
                ('price', models.IntegerField(default=0)),
                ('photo', models.ImageField(upload_to='food')),
                ('restaurant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.restaurant')),
            ],
        ),
    ]
