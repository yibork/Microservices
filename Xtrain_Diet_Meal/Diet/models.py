from django.db import models
from pictures.models import PictureField


class Food(models.Model):
    name = models.CharField(max_length=100)
    protein = models.IntegerField()
    carbohydrates = models.IntegerField()
    fat = models.IntegerField()
    image = PictureField(upload_to='food_images', blank=True, null=True)
    def __str__(self):
        return self.name
    @property
    def calories(self):
        return self.protein * 4 + self.carbohydrates * 4 + self.fat * 9

class Diet(models.Model):

    name = models.CharField(max_length=100)
    image = PictureField(upload_to='diet_images', blank=True, null=True)
    def __str__(self):
        return self.name
    @property
    def get_meals(self):
        return Meal.objects.filter(diet=self)

class DietMeal(models.Model):
    diet = models.ForeignKey('Diet', on_delete=models.CASCADE)
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
    quantity = models.IntegerField()

class MealFood(models.Model):
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
    food = models.ForeignKey('Food', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    image = PictureField(upload_to='food_images', blank=True, null=True)

class DietPlan(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    diet = models.ForeignKey('Diet', on_delete=models.CASCADE)
    trainee = models.ForeignKey('user.User', on_delete=models.CASCADE)
    coach = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='coach')
    def __str__(self):
        return self.name
class Meal(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    food_item = models.ManyToManyField('Food', blank=True)
    picture = PictureField(upload_to='meal_images', blank=True, null=True)
    taken = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    @property
    def total_calories(self):
        return sum([food.calories for food in self.food_item.all()])

    @property
    def total_protein(self):
        return sum([food.protein for food in self.food_item.all()])

    @property
    def total_carbohydrates(self):
        return sum([food.carbohydrates for food in self.food_item.all()])

    @property
    def total_fat(self):
        return sum([food.fat for food in self.food_item.all()])

class DailyMeal(models.Model):
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
    trainee = models.ForeignKey('user.User', on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return self.meal.name