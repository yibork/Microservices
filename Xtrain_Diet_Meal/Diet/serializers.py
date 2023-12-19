from rest_framework import serializers
from .models import Diet
from .models import Meal
from .models import Food
from .models import DietPlan, DailyMeal

class DietSerializer(serializers.ModelSerializer):
    # Define a custom field for get_meals
    get_meals = serializers.SerializerMethodField()

    class Meta:
        model = Diet
        fields = ['user', 'name', 'get_meals']

    # Define a method to serialize get_meals
    def get_get_meals(self, obj):
        # Assuming you have a MealSerializer defined
        meal_serializer = MealSerializer(obj.get_meals, many=True)
        return meal_serializer.data

class FoodSerializer(serializers.ModelSerializer):
    calories = serializers.SerializerMethodField()
    class Meta:
        model = Food
        fields = ('name','calories','protein','carbohydrates','fat','image')

    def get_calories(self, obj):
        return obj.calories

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None



class MealSerializer(serializers.ModelSerializer):
    total_calories = serializers.SerializerMethodField()
    total_protein = serializers.SerializerMethodField()
    total_carbohydrates = serializers.SerializerMethodField()
    total_fat = serializers.SerializerMethodField()
    foods = serializers.SerializerMethodField()
    class Meta:
        model = Meal
        fields = ('name', 'date', 'time', 'diet', 'total_calories','total_protein','total_carbohydrates','total_fat','foods','picture')

    def get_foods(self, obj):
# Assuming you have a FoodSerializer defined
        food_serializer = FoodSerializer(obj.food_item, many=True, context=self.context)
        return food_serializer.data
    def get_total_calories(self, obj):
        return obj.total_calories

    def get_total_protein(self, obj):
        return obj.total_protein

    def get_total_carbohydrates(self, obj):
        return obj.total_carbohydrates

    def get_total_fat(self, obj):
        return obj.total_fat

class DietPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietPlan
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'protein', 'carbohydrates', 'fat', 'image', 'calories']

class MealSerializer(serializers.ModelSerializer):
    food_item = FoodSerializer(many=True, read_only=True)
    total_calories = serializers.ReadOnlyField()
    total_protein = serializers.ReadOnlyField()
    total_carbohydrates = serializers.ReadOnlyField()
    total_fat = serializers.ReadOnlyField()

    class Meta:
        model = Meal
        fields = ['id', 'name', 'date', 'time', 'food_item', 'taken', 'total_calories', 'total_protein', 'total_carbohydrates', 'total_fat','picture']

class DietSerializer(serializers.ModelSerializer):
    get_meals = MealSerializer(many=True, read_only=True)

    class Meta:
        model = Diet
        fields = ['id', 'name','image' ,'get_meals']

class DailyMealSerializer(serializers.ModelSerializer):
    meal = MealSerializer(read_only=True)

    class Meta:
        model = DailyMeal
        fields = ['id', 'meal', 'date']
        read_only_fields = ('trainee',)
