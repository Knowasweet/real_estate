from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _


class ProfileNotFound(APIException):
    status_code = 404
    default_detail = _('The requested profile does not exist')


class NotYourProfile(APIException):
    status_code = 403
    default_detail = _('You cant edit a profile that doesnt belong to you')
