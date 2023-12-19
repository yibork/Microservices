from django.contrib import admin
from .models import Workout, Exercise, WorkoutExercise, WorkoutExerciseSet, UserWorkout, Discipline, Sport
# Register your models here.
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(WorkoutExercise)
admin.site.register(UserWorkout)
admin.site.register(WorkoutExerciseSet)
admin.site.register(Discipline)
admin.site.register(Sport)

