# Generated by Django 3.0.3 on 2020-04-04 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web_Series_app', '0009_season_pics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode_file',
            old_name='_720p',
            new_name='_720px',
        ),
    ]
