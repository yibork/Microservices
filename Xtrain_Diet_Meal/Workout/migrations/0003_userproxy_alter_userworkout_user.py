# Generated by Django 4.2.6 on 2023-12-19 12:49

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Workout', '0002_discipline_remove_workout_user_workout_picture_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='userworkout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Workout.userproxy'),
        ),
    ]
