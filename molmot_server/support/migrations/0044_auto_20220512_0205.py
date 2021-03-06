# Generated by Django 3.2.12 on 2022-05-11 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0043_supportnotification_interval_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='support_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='support.support', verbose_name='관련 제도'),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='subscribe_name',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='관심있는 분야'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='organizer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='support.organization', verbose_name='관련 기관'),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='organizer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='support.organization', verbose_name='관심있는 기관'),
        ),
    ]
