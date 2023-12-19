from django.db import models
from django.contrib.auth.models import AbstractUser
from pictures.models import PictureField
class User(AbstractUser):
    Client = 1
    Coach = 2
    Admin = 3
    Role = (
        (Client, 'Client'),
        (Coach, 'Coach'),
        (Admin, 'Admin'),
    )
    role = models.PositiveSmallIntegerField(choices=Role, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    picture = PictureField(upload_to='XTrain/profile_pictures', blank=True, null=True)

    def __str__(self):
        return self.username


class CoachingRelationship(models.Model):
    coach = models.ForeignKey(User, related_name='coached_trainees', on_delete=models.CASCADE)
    trainee = models.ForeignKey(User, related_name='assigned_coaches', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.coach.username} coaches {self.trainee.username}"

class DayMacro(models.Model):
    user = models.ForeignKey(User, related_name='day_macros', on_delete=models.CASCADE)
    date = models.DateField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s macros for {self.date}"

    @property
    def calories(self):
        return self.protein * 4 + self.fat * 9 + self.carbs * 4

    @property
    def protein_percentage(self):
        return self.protein / self.calories * 100

    @property
    def fat_percentage(self):
        return self.fat / self.calories * 100

    @property
    def carbs_percentage(self):
        return self.carbs / self.calories * 100

class DayWeight(models.Model):
    user = models.ForeignKey(User, related_name='day_weights', on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user.username}'s weight for {self.date}"




class Macro(models.Model):
    user = models.ForeignKey(User, related_name='macros', on_delete=models.CASCADE)
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s macros"

    @property
    def calories(self):
        return self.protein * 4 + self.fat * 9 + self.carbs * 4