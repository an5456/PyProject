# Generated by Django 2.1.7 on 2019-03-26 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='user',
        ),
    ]
