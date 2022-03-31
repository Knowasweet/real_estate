from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from apps.profiles.models import Profile
from apps.users.models import User
from .models import Rating


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_agent_review(request, profile_id):
    agent_profile = Profile.objects.get(id=profile_id, agent=True)
    profile_user = User.objects.get(pkid=agent_profile.user.pkid)
    if profile_user.email == request.user.email:
        return Response({'message': _('it is impossible to vote for yourself')}, status=status.HTTP_403_FORBIDDEN)
    if agent_profile.agent_review.filter(agent__pkid=profile_user.pkid).exists():
        return Response({'detail': _('the profile has already been viewed')}, status=status.HTTP_400_BAD_REQUEST)
    elif request.data['rating'] == 0:
        return Response({'detail': _('please choose a rating')}, status=status.HTTP_400_BAD_REQUEST)
    else:
        Rating.objects.create(
            user_rating=request.user,
            agent=agent_profile,
            rating=request.data['rating'],
            comment=request.data['comment'],
        )
        reviews = agent_profile.agent_review.all()
        agent_profile.num_reviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating

        agent_profile.rating = round(total / len(reviews), 2)
        agent_profile.save()
        return Response({'success': _('agent review was created')})
