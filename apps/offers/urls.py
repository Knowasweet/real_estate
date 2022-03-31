from django.urls import path
from .views import send_offer_email

urlpatterns = [
    path('', send_offer_email, name='send-offer'),
]
