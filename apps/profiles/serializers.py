from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from apps.ratings.serializers import RatingSerializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    second_name = serializers.CharField(source='user.second_name')
    email = serializers.EmailField(source='user.email')
    full_name = serializers.SerializerMethodField(read_only=True)
    country = CountryField(name_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = (
            'username',
            'first_name',
            'second_name',
            'full_name',
            'email',
            'id',
            'phone_number',
            'profile_image',
            'about_me',
            'license',
            'gender',
            'country',
            'city',
            'buyer',
            'seller',
            'agent',
            'rating',
            'count_reviews',
            'reviews',
        )

    def get_full_name(self, obj):
        first_name = obj.user.first_name
        second_name = obj.user.second_name
        return f'{first_name} {second_name}'

    def get_reviews(self, obj):
        reviews = obj.agent_review.all()
        serializer = RatingSerializer(reviews, many=True)
        return serializer.data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation['top_agent'] = True
        return representation


class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'profile_image',
            'about_me',
            'license',
            'gender',
            'country',
            'city',
            'buyer',
            'seller',
            'agent',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation['top_agent'] = True
        return representation
