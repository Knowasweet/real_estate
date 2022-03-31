from django_countries.serializer_fields import CountryField
from .models import Property, PropertyViews
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        fields = (
            'id',
            'user',
            'title',
            'slug',
            'ref_code',
            'description',
            'country',
            'city',
            'postal_code',
            'property_street',
            'property_number',
            'price',
            'property_tax',
            'final_property_price',
            'plot_area',
            'number_of_floors',
            'bedrooms',
            'bathrooms',
            'advert_type',
            'property_type',
            'main_photo',
            'photo1',
            'photo2',
            'photo3',
            'photo4',
            'published_status',
            'views',
        )

    def get_user(self, obj):
        return obj.user.username

    def get_main_photo(self, obj):
        return obj.main_photo.url

    def get_photo1(self, obj):
        return obj.photo1.url

    def get_photo2(self, obj):
        return obj.photo2.url

    def get_photo3(self, obj):
        return obj.photo3.url

    def get_photo4(self, obj):
        return obj.photo4.url


class PropertyCreateSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        exclude = ('updated_at', 'pkid')
