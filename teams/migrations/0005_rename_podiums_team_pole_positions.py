# Generated by Django 5.0.2 on 2024-03-03 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_team_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='podiums',
            new_name='pole_positions',
        ),
    ]