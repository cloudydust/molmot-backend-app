# Generated by Django 3.2.12 on 2022-05-19 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_alter_smartresultqrphoto_photo_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uiphoto',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='uiphoto',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
