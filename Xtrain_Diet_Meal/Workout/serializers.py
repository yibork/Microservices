from rest_framework import serializers
from .models import Workout
from .models import Exercise
from .models import WorkoutExercise
from .models import WorkoutExerciseSet
from .models import UserWorkout
from .models import Sport
from .models import Discipline

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['name', 'sets', 'reps', 'weight', 'workout']

class WorkoutExerciseSetSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)

    class Meta:
        model = WorkoutExercise
        fields = ['workout', 'exercise']

from rest_framework import serializers
from .models import Workout
from .models import Exercise
from .models import WorkoutExercise
from .models import WorkoutExerciseSet
from .models import UserWorkout
from .models import Sport
from .models import Discipline

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['name', 'sets', 'reps', 'weight', 'workout']

class WorkoutExerciseSetSerializer(serializers.ModelSerializer):
    exercise = serializers.SerializerMethodField()

    class Meta:
        model = WorkoutExercise
        fields = ['workout', 'exercise']

    def get_exercise(self, obj):
        exercise = Exercise.objects.get(id=obj.exercise.id)
        return ExerciseSerializer(exercise).data



class WorkoutSerializer(serializers.ModelSerializer):
    exercises = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['name', 'sport', 'picture', 'exercises']

    def get_exercises(self, obj):
        # Fetching related exercises for the workout
        workout_exercises = WorkoutExercise.objects.filter(workout=obj)
        # Serializing the exercises
        return WorkoutExerciseSetSerializer(workout_exercises, many=True).data

class SportSerializer(serializers.ModelSerializer):
    workouts = serializers.SerializerMethodField()
    class Meta:
        model = Sport
        fields = ['name', 'picture', 'workouts']  # Include 'workouts' field

    def get_workouts(self, obj):
        # Fetching related workouts for the sport
        workouts = Workout.objects.filter(sport=obj)
        # Serializing the workouts
        return WorkoutSerializer(workouts, many=True).data
class DisciplineSerializer(serializers.ModelSerializer):
    sports = serializers.SerializerMethodField()

    class Meta:
        model = Discipline
        fields = ['name', 'sports']

    def get_sports(self, obj):
        # Fetching related sports for the discipline
        sports = Sport.objects.filter(disciplines=obj)
        # Serializing the sports
        return SportSerializer(sports, many=True).data




class UserWorkoutSerializer(serializers.ModelSerializer):
    workout = WorkoutSerializer(read_only=True)
    class Meta:
        model = UserWorkout
        fields = ['user', 'workout', 'date']
class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = ['workout', 'exercise']



