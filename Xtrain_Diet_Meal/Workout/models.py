from django.db import models
from pictures.models import PictureField

# Create your models here.
class Discipline(models.Model):
    name = models.CharField(max_length=100)
    picture = PictureField(upload_to='XTrain/discipline_pictures', blank=True, null=True)
    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=100)
    picture = PictureField(upload_to='XTrain/sport_pictures', blank=True, null=True)
    disciplines = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Workout(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    picture = PictureField(upload_to='XTrain/workout_pictures', blank=True, null=True)

    def __str__(self):
        return self.name

class UserWorkout(models.Model):
    user = models.ForeignKey('Workout.UserProxy', on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date = models.DateTimeField()


    def __str__(self):
        return self.user.username + ' - ' + self.workout.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.IntegerField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    def __str__(self):
        return self.workout.name + ' - ' + self.exercise.name

class WorkoutExerciseSet(models.Model):
    workout_exercise = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE)
    set_number = models.IntegerField()
    reps = models.IntegerField()
    weight = models.IntegerField()
    def __str__(self):
        return self.workout_exercise.workout.name + ' - ' + self.workout_exercise.exercise.name + ' - ' + str(self.set_number)





