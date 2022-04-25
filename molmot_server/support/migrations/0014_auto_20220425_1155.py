# Generated by Django 3.2.12 on 2022-04-25 11:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0015_edit_solarschedule_events_choices'),
        ('support', '0013_auto_20220421_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportnotification',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='supportschedulednotification',
            name='noti_on_or_off',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='supportschedulednotification',
            name='noti_on_time',
            field=models.DateTimeField(null=True, verbose_name='푸시알림 전송할 시간'),
        ),
        migrations.AlterField(
            model_name='supportnotification',
            name='periodictask_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='django_celery_beat.periodictask'),
        ),
    ]
