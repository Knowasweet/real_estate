from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import NotYourProfile, ProfileNotFound
from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer, UpdateProfileSerializer


class AgentListAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.filter(agent=True)


class TopAgentsListAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.filter(top_agent=True)


class GetProfileAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (ProfileJSONRenderer,)

    def get(self, request):
        user_profile = Profile.objects.get(user=self.request.user)
        serializer = ProfileSerializer(user_profile, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProfileAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = UpdateProfileSerializer

    def patch(self, request, username):
        try:
            Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound

        if request.user.username != username:
            raise NotYourProfile

        serializer = UpdateProfileSerializer(instance=request.user.profile, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
