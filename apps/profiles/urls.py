from django.urls import path
from .views import (AgentListAPIView, GetProfileAPIView, TopAgentsListAPIView, UpdateProfileAPIView)

urlpatterns = [
    path('', GetProfileAPIView.as_view(), name='get_profile'),
    path('update/<str:username>/', UpdateProfileAPIView.as_view(), name='update_profile'),
    path('agents/', AgentListAPIView.as_view(), name='agents'),
    path('agents/top/', TopAgentsListAPIView.as_view(), name='top-agents'),
]
