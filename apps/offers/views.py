from django.core.mail import send_mail

from estate.settings.dev import DEFAULT_FROM_EMAIL
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from .serializers import OfferSerializer


@api_view(['POST'])
@permission_classes((AllowAny,))
def send_offer_email(request):
    serializer = OfferSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        send_mail(request.data['subject'], request.data['message'], request.data['email'], (DEFAULT_FROM_EMAIL,),
                  fail_silently=True)
        return Response({'success': _('Your request has been successfully sent')})
    return Response({'fail': _('The request was not sent. Please try again')})
