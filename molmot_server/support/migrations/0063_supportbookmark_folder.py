# Generated by Django 3.2.12 on 2022-05-15 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0062_alter_category_colored'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportbookmark',
            name='folder',
            field=models.CharField(choices=[('smart', '스마트 맞춤 설계 결과'), ('general', '일반 북마크')], default='general', max_length=10, verbose_name='분류 폴더'),
        ),
    ]
