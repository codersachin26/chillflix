# Generated by Django 3.0.3 on 2020-04-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_Series_app', '0011_auto_20200404_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='season_pics',
            name='s_screenshot2',
            field=models.ImageField(null=True, upload_to='screenshot2/'),
        ),
        migrations.AddField(
            model_name='season_pics',
            name='s_screenshot3',
            field=models.ImageField(null=True, upload_to='screenshot3/'),
        ),
        migrations.AlterField(
            model_name='season_pics',
            name='s_screenshot1',
            field=models.ImageField(upload_to='screenshot1/'),
        ),
    ]
