# Generated by Django 3.2.12 on 2022-05-12 08:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0049_auto_20220512_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='member_id',
        ),
        migrations.AddField(
            model_name='channel',
            name='member_id',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
