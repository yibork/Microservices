# Generated by Django 4.2.6 on 2023-11-29 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Diet', '0009_alter_dailymeal_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailymeal',
            name='meal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Diet.meal'),
            preserve_default=False,
        ),
    ]