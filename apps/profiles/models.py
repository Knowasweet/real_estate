from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampUUIDModel


class Gender(models.TextChoices):
    MALE = 'male', _('male')
    FEMALE = 'female', _('female')
    OTHER = 'other', _('other')


class Profile(TimeStampUUIDModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name=_('phone number'), max_length=30, blank=False, null=False)
    about_me = models.TextField(verbose_name=_('about me'), null=True)
    gender = models.CharField(verbose_name=_('gender'), choices=Gender.choices, default=Gender.OTHER, max_length=20)
    country = CountryField(verbose_name=_('country'), default='RU', blank=False, null=False)
    city = models.CharField(verbose_name=_('city'), max_length=180, blank=False, null=False)
    license = models.CharField(verbose_name=_('property license'), max_length=20, blank=True, null=True)
    profile_image = models.ImageField(verbose_name=_('profile image'), default='/profile_example.png')
    buyer = models.BooleanField(verbose_name=_('buyer'), default=False,
                                help_text=_('do you want to buy a property?'))
    seller = models.BooleanField(verbose_name=_('seller'), default=False,
                                 help_text=_('do you want to sell a property?'))
    agent = models.BooleanField(verbose_name=_('agent'), default=False, help_text=_('are you an agent?'))
    top_agent = models.BooleanField(verbose_name=_('top agent'), default=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    count_reviews = models.IntegerField(verbose_name=_('number of reviews'), default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'
