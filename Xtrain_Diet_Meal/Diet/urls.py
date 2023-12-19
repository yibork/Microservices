from django.contrib import admin
from .views import DietView, MealView, FoodView, DailyMealView
from django.urls import path
from django.urls import include
from rest_framework import routers
router = routers.DefaultRouter()
router.register('Diet', DietView, basename='Diet')
router.register('Meal', MealView, basename='Meal')
router.register('Food', FoodView, basename='Food')
router.register('DailyMeal', DailyMealView, basename='DailyMeal')


urlpatterns = router.urls
urlpatterns += [
    path('diets/<int:pk>/add_meal/', DietView.as_view({'post': 'add_meal'}), name='add-meal'),
]



