# Generated by Django 3.2.12 on 2022-05-12 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0047_rename_colored_subscribe_channel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='channel_name',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='organizer_id',
        ),
        migrations.AddField(
            model_name='subscribe',
            name='colored',
            field=models.CharField(choices=[('pink', 'pink'), ('yellow', 'yellow ')], max_length=10, null=True, verbose_name='색깔 분류'),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='support_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='support.support', verbose_name='관심있는 기관'),
        ),
    ]