from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from .models import DayMacro

# This script should be run in the Django shell, not as a standalone script.

# Replace 'your_username' with the username of the specific user you want to create data for.
username = 'a'
user = get_user_model().objects.get(username=username)

# Generate macros data for the last 30 days for the specific user.
for day in range(30):
    date = timezone.now().date() - timedelta(days=day)
    # Replace the following values with your own logic for determining intake
    protein = 100  # Example fixed value
    fat = 50  # Example fixed value
    carbs = 200  # Example fixed value

    # Create or update the DayMacro instance for the user and date
    DayMacro.objects.update_or_create(user=user, date=date, defaults={
        'protein': protein,
        'fat': fat,
        'carbs': carbs
    })

print("Data populated for the last 30 days.")
