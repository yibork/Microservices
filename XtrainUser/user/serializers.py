from .models import User
from .models import DayMacro
from rest_framework import serializers
from django.utils import timezone
from django.db import models

from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'picture','first_name','last_name','role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number'),
            picture=validated_data.get('picture'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            role=validated_data.get('role'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user




class CoachListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


from rest_framework import serializers
from .models import  DayWeight

class DayMacroSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayMacro
        fields = ['protein', 'fat', 'carbs', 'calories']

class DayWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayWeight
        fields = ['date', 'weight']



class UserInfoSerializer(serializers.ModelSerializer):
    day_macros = DayMacroSerializer(many=True)
    day_weights = DayWeightSerializer(many=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'role', 'day_macros', 'day_weights','picture']

class DayMacroSerializer(serializers.ModelSerializer):
    calories = serializers.ReadOnlyField()
    protein_percentage = serializers.ReadOnlyField()
    fat_percentage = serializers.ReadOnlyField()
    carbs_percentage = serializers.ReadOnlyField()

    class Meta:
        model = DayMacro
        fields = ['id', 'user', 'date', 'protein', 'fat', 'carbs', 'calories', 'protein_percentage', 'fat_percentage', 'carbs_percentage']
