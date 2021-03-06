# Generated by Django 2.1.7 on 2019-03-29 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_auto_20190328_2139'),
        ('user', '0003_auto_20190327_1110'),
        ('task', '0003_auto_20190327_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='task',
            name='vid',
        ),
        migrations.AddField(
            model_name='task',
            name='catlog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='course.Catalog', verbose_name='目录'),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user.User', verbose_name='用户'),
        ),
    ]
