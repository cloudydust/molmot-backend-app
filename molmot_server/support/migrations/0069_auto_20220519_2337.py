# Generated by Django 3.2.12 on 2022-05-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0068_alter_support_job_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='in_progress',
            field=models.CharField(blank=True, choices=[('재학생', '재학생'), ('석/박사', '석/박사')], default='재학생', max_length=6, null=True, verbose_name='스마트설계 - 대학 과정'),
        ),
        migrations.AlterField(
            model_name='support',
            name='detail_field',
            field=models.CharField(blank=True, choices=[('1', '저소득층'), ('2', '다자녀 가정'), ('3', '군인'), ('4', '코로나 19 지원 대상'), ('5', '장애인, 장애우'), ('6', '해당 없음')], default='6', max_length=6, null=True, verbose_name='스마트설계 - 분야'),
        ),
        migrations.AlterField(
            model_name='support',
            name='job_info',
            field=models.CharField(blank=True, choices=[('학생', '학생'), ('직장인', '직장인'), ('프리랜서', '프리랜서'), ('자영업자', '자영업자')], default='학생', max_length=6, null=True, verbose_name='직업'),
        ),
    ]
