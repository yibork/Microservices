# Generated by Django 4.2.6 on 2023-11-02 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Diet', '0004_remove_diet_coach_remove_diet_duration_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dietplan',
            old_name='user',
            new_name='trainee',
        ),
    ]
