# Generated by Django 3.2.12 on 2022-05-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0066_alter_support_detail_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='job_info',
            field=models.CharField(blank=True, choices=[('대학생', '대학생'), ('직장인', '직장인'), ('프리랜서', '프리랜서')], default='학생', max_length=6, null=True, verbose_name='직업'),
        ),
    ]
