# Generated by Django 3.2.12 on 2022-05-05 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_memberfcmdevice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='locatedin',
        ),
        migrations.AddField(
            model_name='member',
            name='city_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='시/군/구'),
        ),
        migrations.AddField(
            model_name='member',
            name='colleage',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='학교'),
        ),
        migrations.AddField(
            model_name='member',
            name='colleage_locatedin',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='소재지'),
        ),
    ]
