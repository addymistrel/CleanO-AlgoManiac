# Generated by Django 4.1.3 on 2022-12-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0006_managebins_lat_managebins_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickup',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
