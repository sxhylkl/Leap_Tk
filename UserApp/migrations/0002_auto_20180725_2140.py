# Generated by Django 2.0.7 on 2018-07-25 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='bookID',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='BookApp.book', verbose_name='所学内容'),
        ),
    ]
