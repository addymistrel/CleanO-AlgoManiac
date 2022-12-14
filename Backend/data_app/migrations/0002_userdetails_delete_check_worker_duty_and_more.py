# Generated by Django 4.1.3 on 2022-11-30 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('number', models.PositiveIntegerField()),
                ('password', models.CharField(max_length=50)),
                ('passwor2', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='check_worker_duty',
        ),
        migrations.DeleteModel(
            name='complaint',
        ),
        migrations.DeleteModel(
            name='details_house',
        ),
        migrations.DeleteModel(
            name='nearby_bins',
        ),
        migrations.DeleteModel(
            name='pickup',
        ),
        migrations.DeleteModel(
            name='user_registration',
        ),
        migrations.DeleteModel(
            name='worker_registration',
        ),
    ]
