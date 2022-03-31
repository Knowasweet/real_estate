import random
import string

from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from apps.common.models import TimeStampUUIDModel

User = get_user_model()


class PropertyPublishedManager(models.Manager):
    def get_queryset(self):
        return super(PropertyPublishedManager, self).get_queryset().filter(published_status=True)


class Property(TimeStampUUIDModel):
    class AdvertType(models.TextChoices):
        SALE = 'sale', _('sale')
        RENT = 'rent', _('rent')
        AUCTION = 'auction', _('auction')

    class PropertyType(models.TextChoices):
        HOUSE = 'house', _('house')
        APARTMENT = 'apartment', _('apartment')
        COMMERCIAL = 'commercial premises', _('commercial premises')
        OFFICE = 'office', _('office')
        WAREHOUSE = 'warehouse', _('warehouse')
        OTHER = 'other', _('other')

    user = models.ForeignKey(User, verbose_name=_('who are you? - agent, seller, buyer'), on_delete=models.DO_NOTHING)
    title = models.CharField(verbose_name=_('ownership'), max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)
    ref_code = models.CharField(verbose_name=_('link to properties'), max_length=255, unique=True, blank=True, )
    description = models.TextField(verbose_name=_('description'), default='', null=True)
    country = CountryField(verbose_name=_('country'), default="RU", blank_label=_('country selection'))
    city = models.CharField(verbose_name=_('city'), max_length=180, default='Saint-Petersburg')
    postal_code = models.CharField(verbose_name=_('postal code'), max_length=100, default="000000")
    property_street = models.CharField(verbose_name=_('property_street'), max_length=150, default='')
    property_number = models.IntegerField(verbose_name=_('property number'),
                                          validators=[MinValueValidator(1)], default=123)
    price = models.DecimalField(verbose_name=_('price'), max_digits=8, decimal_places=2, default=0.0)
    property_tax = models.DecimalField(verbose_name=_('property tax'), max_digits=6, decimal_places=2,
                                       default=0.15, help_text='property tax is charged in the amount of 15%')
    plot_area = models.DecimalField(verbose_name=_('plot area (m^2)'), max_digits=8, decimal_places=2,
                                    default=0.0)
    number_of_floors = models.IntegerField(verbose_name=_('number of floors'), default=0)
    bedrooms = models.IntegerField(verbose_name=_('bedrooms'), default=1)
    bathrooms = models.IntegerField(verbose_name=_('bathrooms'), default=1)
    advert_type = models.CharField(verbose_name=_('advert type'), max_length=50, choices=AdvertType.choices,
                                   default=AdvertType.SALE)
    property_type = models.CharField(verbose_name=_('property type'), max_length=50, choices=PropertyType.choices,
                                     default=PropertyType.OTHER)
    main_photo = models.ImageField(verbose_name=_('main photo'), default='/property_main_example.jpg', null=True,
                                   blank=True)
    photo1 = models.ImageField(default='/property_example.jpg', null=True, blank=True)
    photo2 = models.ImageField(default='/property_example.jpg', null=True, blank=True)
    photo3 = models.ImageField(default='/property_example.jpg', null=True, blank=True)
    photo4 = models.ImageField(default='/property_example.jpg', null=True, blank=True)
    published_status = models.BooleanField(verbose_name=_('published status'), default=False)
    views = models.IntegerField(verbose_name=_('views'), default=0)

    objects = models.Manager()
    published = PropertyPublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('property')
        verbose_name_plural = _('properties')

    def save(self, *args, **kwargs):
        self.title = str.title(self.title)
        self.description = str.capitalize(self.description)
        self.ref_code = ''.join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )
        super(Property, self).save(*args, **kwargs)

    @property
    def final_property_price(self):
        property_tax_percentage = self.property_tax
        property_price = self.price
        property_tax_amount = round(property_tax_percentage * property_price, 2)
        price_after_tax = float(round(property_price + property_tax_amount, 2))
        return price_after_tax


class PropertyViews(TimeStampUUIDModel):
    ip = models.CharField(verbose_name=_('ip'), max_length=250)
    property = models.ForeignKey(Property, related_name='property_views', on_delete=models.CASCADE)

    def __str__(self):
        return (
            _(f'The total number of views {self.property.title} is equal to {self.property.views} view(s)')
        )

    class Meta:
        verbose_name = _('general views on real estate')
        verbose_name_plural = _('general property views')
