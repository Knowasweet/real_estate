from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/profile/', include('apps.profiles.urls')),
    path('api/v1/properties/', include('apps.properties.urls')),
    path('api/v1/ratings/', include('apps.ratings.urls')),
    path('api/v1/offers/', include('apps.offers.urls')),
]

admin.site.site_header = _('Estate Administrator')
admin.site.site_title = _('Estate Administrator Portal')
admin.site.index_title = _('Welcome to the estate administrator portal')
