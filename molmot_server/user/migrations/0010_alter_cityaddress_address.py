# Generated by Django 3.2.12 on 2022-05-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_cityaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityaddress',
            name='address',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
