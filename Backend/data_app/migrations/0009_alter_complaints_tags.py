# Generated by Django 4.1.3 on 2022-12-01 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0008_complaints_delete_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='tags',
            field=models.BooleanField(default=False),
        ),
    ]
