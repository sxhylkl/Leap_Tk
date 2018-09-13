# Generated by Django 2.0.7 on 2018-07-30 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_auto_20180730_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='experience',
            field=models.IntegerField(verbose_name='经验'),
        ),
        migrations.AlterField(
            model_name='information',
            name='gender',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], max_length=30, verbose_name='性别'),
        ),
    ]
