# Generated by Django 4.0.3 on 2022-03-29 15:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField(choices=[(1, 'terribly'), (2, 'weakly'), (3, 'satisfactory'), (4, 'well'), (5, 'great')], default=0, help_text='1-terribly, 2-weakly, 3-satisfactory, 4-well, 5-great,', verbose_name='rating')),
                ('comment', models.TextField(verbose_name='comment')),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_review', to='profiles.profile', verbose_name='the rating agent')),
            ],
        ),
    ]