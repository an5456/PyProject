# Generated by Django 2.1.7 on 2019-03-28 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_auto_20190328_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='pic',
            new_name='video',
        ),
    ]
