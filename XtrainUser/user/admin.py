from django.contrib import admin
from .models import User, CoachingRelationship, DayMacro, DayWeight
# Register your models here.
admin.site.register(User)
admin.site.register(CoachingRelationship)
admin.site.register(DayMacro)
admin.site.register(DayWeight)
