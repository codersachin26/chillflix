# Generated by Django 3.0.3 on 2020-04-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_Series_app', '0002_auto_20200403_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series_info',
            name='poster_img',
            field=models.ImageField(upload_to='poster_img/'),
        ),
    ]
