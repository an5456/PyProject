# Generated by Django 2.1.7 on 2019-03-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ManyToManyField(to='user.User'),
        ),
    ]
