# Generated by Django 3.2.12 on 2022-05-17 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0064_alter_support_job_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='detail_field',
            field=models.CharField(blank=True, choices=[('1', '다자녀 가정'), ('2', '한부모 가정'), ('3', '다문화 가정'), ('4', '현역 군인 및 군무원의 자녀'), ('5', '장애인, 장애우'), ('6', '기타')], default='6', max_length=6, null=True, verbose_name='스마트설계 - 분야'),
        ),
    ]
