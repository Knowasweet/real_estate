from django.db import models
from django.utils.translation import gettext_lazy as _
from estate.settings.base import AUTH_USER_MODEL
from apps.common.models import TimeStampUUIDModel
from apps.profiles.models import Profile


class Rating(TimeStampUUIDModel):
    class Range(models.IntegerChoices):
        RATING_1 = 1, _('terribly')
        RATING_2 = 2, _('weakly')
        RATING_3 = 3, _('satisfactory')
        RATING_4 = 4, _('well')
        RATING_5 = 5, _('great')

    user_rating = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_('the user providing the rating'),
                                    on_delete=models.SET_NULL, null=True)
    agent = models.ForeignKey(Profile, verbose_name=_('the rating agent'), related_name='agent_review',
                              on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(verbose_name=_('rating'), choices=Range.choices,
                                 help_text='1-terribly, 2-weakly, 3-satisfactory, 4-well, 5-great,', default=0)
    comment = models.TextField(verbose_name=_('comment'))

    class Meta:
        unique_together = ('user_rating', 'agent')

    def __str__(self):
        return _(f'{self.agent} rated in {self.rating}')
