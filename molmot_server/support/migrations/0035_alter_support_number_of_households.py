# Generated by Django 3.2.12 on 2022-05-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0034_auto_20220508_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='number_of_households',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='가구수'),
        ),
    ]