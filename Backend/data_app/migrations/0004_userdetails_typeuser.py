# Generated by Django 4.1.3 on 2022-11-30 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0003_rename_passwor2_userdetails_password2'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='typeuser',
            field=models.BooleanField(default=False),
        ),
    ]
