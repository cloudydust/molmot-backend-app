# Generated by Django 3.2.12 on 2022-04-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0026_channel_organizer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='hits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]