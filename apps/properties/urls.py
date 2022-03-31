from django.urls import path
from .views import ListAllPropertiesAPIView, ListAgentsPropertiesAPIView, PropertyDetailView, create_property_api_view, \
    update_property_api_view, delete_property_api_view

urlpatterns = [
    path('', ListAllPropertiesAPIView.as_view(), name='all-properties'),
    path('agents/', ListAgentsPropertiesAPIView.as_view(), name='agents-properties'),
    path('<slug:slug>', PropertyDetailView.as_view(), name='property-details'),
    path('create/', create_property_api_view, name='create-property'),
    path('update/<slug:slug>', update_property_api_view, name='update-property'),
    path('delete/<slug:slug>', delete_property_api_view, name='delete-property'),
]
