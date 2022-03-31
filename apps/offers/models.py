from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampUUIDModel


class Offer(TimeStampUUIDModel):
    name = models.CharField(_('name'), max_length=100)
    phone_number = PhoneNumberField(_('phone number'), max_length=30, null=True)
    email = models.EmailField(_('email'))
    subject = models.CharField(_('subject'), max_length=100)
    message = models.TextField(_('message'))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')
