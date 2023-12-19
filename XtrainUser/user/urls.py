from .views import UserRegister, MyTokenObtainPairView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import UserInformationView
from .views import DayMacroListCreateView, DayWeightListCreateView, TokenView

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('info/', UserInformationView.as_view(), name='info'),
    path('day-macros/', DayMacroListCreateView.as_view(), name='day-macro-list-create'),
    path('day-weights/', DayWeightListCreateView.as_view(), name='day-weight-list-create'),
    path('token/', TokenView.as_view(), name='token'),
]
