# Generated by Django 5.0.2 on 2024-03-03 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_team_car_team_engine_team_factory_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
