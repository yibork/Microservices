from django.db import models

class UserProxy(models.Model):
    id=models.IntegerField(primary_key=True)

