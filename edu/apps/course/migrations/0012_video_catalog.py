# Generated by Django 2.1.7 on 2019-03-28 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_usercourse_dopercent'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='Catalog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='course.Catalog', verbose_name='目录项'),
        ),
    ]
