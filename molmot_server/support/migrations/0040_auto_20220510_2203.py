# Generated by Django 3.2.12 on 2022-05-10 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0039_auto_20220510_0248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='support',
            options={'ordering': ['-end_date']},
        ),
        migrations.RemoveField(
            model_name='support',
            name='notice',
        ),
    ]
