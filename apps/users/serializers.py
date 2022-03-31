from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='profile.gender')
    phone_number = PhoneNumberField(source='profile.phone_number')
    profile_image = serializers.ImageField(source='profile.profile_image')
    country = CountryField(source='profile.country')
    city = serializers.CharField(source='profile.city')
    top_seller = serializers.BooleanField(source='profile.top_seller')
    full_name = serializers.SerializerMethodField(source='get_full_name')

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'full_name',
            'gender',
            'phone_number',
            'profile_image',
            'country',
            'city',
            'top_seller',
        )

    def get_first_name(self, obj):
        return obj.first_name

    def get_second_name(self, obj):
        return obj.second_name

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation['admin'] = True
        return representation


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'second_name', 'password')
