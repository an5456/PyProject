# Generated by Django 2.1.7 on 2019-03-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20190327_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='stick',
            field=models.CharField(choices=[('stick', '置顶'), ('unstick', '未置顶')], default='未置顶', max_length=32),
        ),
    ]
