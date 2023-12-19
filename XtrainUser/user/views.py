import self
from django.shortcuts import render

from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from .serializers import UserInfoSerializer
from .models import DayMacro
from django.utils import timezone
from .models import User, DayMacro, DayWeight

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import DayMacroSerializer
from django.forms.models import model_to_dict

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['id'] = user.id
        token['phone_number'] = user.phone_number




        # ...
        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response({"message":"User Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInformationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            # Fetch related data for the user
            day_macros = DayMacro.objects.filter(user=user, date=timezone.now().date())
            day_weights = DayWeight.objects.filter(user=user, date=timezone.now().date())

            # Serialize the data
            serialized_data = UserInfoSerializer(user, context={
                'day_macros': day_macros,
                'day_weights': day_weights,
            }).data

            return Response(serialized_data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class DayMacroListCreateView(generics.ListCreateAPIView):
    serializer_class = DayMacroSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # This will ensure that a user can only see their own DayMacro instances.
        return DayMacro.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # This sets the user to the current user when creating a new DayMacro instance.
        serializer.save(user=self.request.user)

from .serializers import DayWeightSerializer

class DayWeightListCreateView(generics.ListCreateAPIView):
    serializer_class = DayWeightSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users should only see their own weight records.
        return DayWeight.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Sets the user to the current user when creating a new record.
        serializer.save(user=self.request.user)


class TokenView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = model_to_dict(user, fields=['username', 'first_name', 'last_name', 'email'])
        return Response({"allowed": user_data}, status=status.HTTP_200_OK)
