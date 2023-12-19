from django.contrib import admin
from .models import Diet
from .models import Food
from .models import Meal
from .models import DietMeal
from .models import MealFood
from .models import DietPlan
from .models import DailyMeal


# Register your models here.
admin.site.register(Diet)
admin.site.register(Food)
admin.site.register(Meal)
admin.site.register(DietMeal)
admin.site.register(MealFood)
admin.site.register(DietPlan)
admin.site.register(DailyMeal)
