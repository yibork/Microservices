# repositories.py

from .models import Diet, Meal, Food, DietPlan

class DietRepository:
    @staticmethod
    def get_all():
        return Diet.objects.all()

    @staticmethod
    def get(pk):
        return Diet.objects.get(pk=pk)

    @staticmethod
    def assign_diet(diet, trainee):
        diet.trainee = trainee
        diet.save()

    @staticmethod
    def delete(diet):
        diet.delete()

class MealRepository:
    @staticmethod
    def get_all():
        return Meal.objects.all()

    @staticmethod
    def create(data):
        meal = Meal(**data)
        meal.save()
        return meal

    @staticmethod
    def update(meal, data):
        for key, value in data.items():
            setattr(meal, key, value)
        meal.save()
        return meal

    @staticmethod
    def delete(meal):
        meal.delete()

class FoodRepository:
    @staticmethod
    def get_all():
        return Food.objects.all()

    @staticmethod
    def create(data):
        food = Food(**data)
        food.save()
        return food

    @staticmethod
    def update(food, data):
        for key, value in data.items():
            setattr(food, key, value)
        food.save()
        return food

    @staticmethod
    def delete(food):
        food.delete()

class DietPlanRepository:
    @staticmethod
    def get_all_for_user(user):
        return DietPlan.objects.filter(trainee=user) | DietPlan.objects.filter(coach=user)

    @staticmethod
    def suggest_diets(goals, diet_preferences):
        # Implement your diet suggestion logic here based on user data
        # This might involve querying the database for suitable diet plans
        suggested_diets = DietPlan.objects.filter(goals__in=goals, allowed_foods__in=diet_preferences)
        return suggested_diets

    @staticmethod
    def create(data):
        diet_plan = DietPlan(**data)
        diet_plan.save()
        return diet_plan

    @staticmethod
    def update(diet_plan, data):
        for key, value in data.items():
            setattr(diet_plan, key, value)
        diet_plan.save()
        return diet_plan

    @staticmethod
    def delete(diet_plan):
        diet_plan.delete()
