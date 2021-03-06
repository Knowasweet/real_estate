from django.contrib import admin

from .models import Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'message')


admin.site.register(Offer, OfferAdmin)
