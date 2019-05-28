# Generated by Django 2.1.7 on 2019-03-28 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20190328_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourse',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='course.Course', verbose_name='课程'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user.User', verbose_name='用户'),
        ),
    ]
