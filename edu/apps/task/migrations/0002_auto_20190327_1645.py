# Generated by Django 2.1.7 on 2019-03-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('已完成', '已完成'), ('未完成', '未完成')], default='未完成', max_length=32),
        ),
    ]
