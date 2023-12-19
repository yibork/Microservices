from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import WorkoutViewSet, ExerciseViewSet, WorkoutExerciseViewSet, WorkoutExerciseSetViewSet, UserWorkoutViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('Workout', WorkoutViewSet, basename='Workout')
router.register('Exercise', ExerciseViewSet, basename='Exercise')
router.register('WorkoutExercise', WorkoutExerciseViewSet, basename='WorkoutExercise')
router.register('WorkoutExerciseSet', WorkoutExerciseSetViewSet, basename='WorkoutExerciseSet')
router.register('UserWorkout', UserWorkoutViewSet, basename='UserWorkout')
router.register('Discipline', views.DisciplineViewSet, basename='Discipline')
router.register('Sport', views.SportViewSet, basename='Sport')
urlpatterns = [
    # Include the router URLs
]
urlpatterns += router.urls
