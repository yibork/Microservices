# Generated by Django 4.2.6 on 2023-11-01 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Diet', '0002_mealfood_remove_food_calories_diet_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach', to=settings.AUTH_USER_MODEL),
        ),
    ]
