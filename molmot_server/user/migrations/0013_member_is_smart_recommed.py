# Generated by Django 3.2.12 on 2022-05-15 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_member_privacy_agreement'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_smart_recommed',
            field=models.BooleanField(default=False, verbose_name='스마트 맞춤 설계 이력'),
        ),
    ]
