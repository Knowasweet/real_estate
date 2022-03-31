# Generated by Django 4.0.3 on 2022-03-29 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ratings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='user_rating',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='the user providing the rating'),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user_rating', 'agent')},
        ),
    ]