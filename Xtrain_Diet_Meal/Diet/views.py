from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Diet, Meal, Food, DietPlan, DailyMeal
from .serializers import DietSerializer, MealSerializer, FoodSerializer, DietPlanSerializer, DailyMealSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
class FoodView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class MealView(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(detail=True, methods=['post'])
    def add_food(self, request, pk=None):
        # Logic to add a food item to a meal
        pass

class DietView(viewsets.ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer

    @action(detail=True, methods=['post'])
    def add_meal(self, request, pk=None):
        # Add meal to diet logic here
        diet = self.get_object()
        meal_id = request.data.get('meal_id')
        meal = Meal.objects.get(pk=meal_id)
        diet.get_meals.add(meal)
        diet.save()
        return Response({'status': 'meal added'}, status=status.HTTP_200_OK)

class DietPlanView(viewsets.ModelViewSet):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer

    @action(detail=True, methods=['post'])
    def assign_to_user(self, request, pk=None):
        # Logic to assign a diet plan to a user
        pass

class DailyMealView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DailyMealSerializer

    def get_queryset(self):
        user = self.request.user
        return DailyMeal.objects.filter(trainee=user, date=timezone.now().date())

    def create(self, request, *args, **kwargs):
        # Getting the meal instance
        meal = Meal.objects.get(pk=request.data['meal']['id'])

        # Creating a new DailyMeal instance
        daily_meal_instance = DailyMeal(trainee=request.user, meal=meal, date=request.data['date'])
        daily_meal_instance.save()

        # Serializing the instance for the response
        serializer = DailyMealSerializer(daily_meal_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
