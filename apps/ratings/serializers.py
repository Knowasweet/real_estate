from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    user_rating = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ('updated', 'pkid')

    def get_user_rating(self, obj):
        return obj.user_rating.username

    def get_agent(self, obj):
        return obj.agent.user
