# Generated by Django 3.2.12 on 2022-05-01 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uiphoto',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]