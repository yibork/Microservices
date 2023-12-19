from rest_framework import viewsets
from .models import Workout, UserWorkout, Exercise, WorkoutExercise, WorkoutExerciseSet, Sport, Discipline
from .serializers import (
    WorkoutSerializer,
    UserWorkoutSerializer,
    ExerciseSerializer,
    WorkoutExerciseSerializer,
    WorkoutExerciseSetSerializer,
    SportSerializer,
    DisciplineSerializer,
)
from rest_framework.permissions import IsAuthenticated
class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        # Directly return all Workout instances
        return Workout.objects.all()

class UserWorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = UserWorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter by the logged-in user
        return UserWorkout.objects.filter(user=self.request.user)

class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Assuming you want to filter exercises for the logged-in user
        # Adjust the filter as per your application's logic
        return Exercise.objects.filter(workout__userworkout__user=self.request.user)

class WorkoutExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutExerciseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter based on the logged-in user
        return WorkoutExercise.objects.filter(workout__userworkout__user=self.request.user)

class WorkoutExerciseSetViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutExerciseSetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter based on the logged-in user
        return WorkoutExerciseSet.objects.filter(workout_exercise__workout__userworkout__user=self.request.user)

class SportViewSet(viewsets.ModelViewSet):
    serializer_class = SportSerializer

    def get_queryset(self):
        # Directly return all Sport instances
        return Sport.objects.all()

class DisciplineViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplineSerializer

    def get_queryset(self):
        # Directly return all Discipline instances
        return Discipline.objects.all()
