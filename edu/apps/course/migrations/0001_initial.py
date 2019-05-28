# Generated by Django 2.1.7 on 2019-03-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('class_type', models.CharField(choices=[('video', '视频'), ('question', '问题'), ('article', '文章'), ('data', '资料')], default='视频', max_length=32)),
                ('status', models.CharField(choices=[('public', '已发布'), ('unpublic', '未发布')], default='未发布', max_length=32)),
                ('type', models.CharField(choices=[('chapter', '章'), ('section', '节')], default='节', max_length=32)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=500)),
                ('contentid', models.IntegerField(default=0)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('u_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '目录',
                'verbose_name_plural': '目录',
                'db_table': 'catalog',
                'ordering': ['c_time'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('status', models.CharField(choices=[('public', '已发布'), ('unpublic', '未发布')], default='未发布', max_length=32)),
                ('level', models.CharField(choices=[('good', '精品'), ('height', '高级'), ('simple', '基础'), ('feel', '免费')], default='免费', max_length=32)),
                ('stick', models.CharField(choices=[('stick', '置顶'), ('unstick', '未置顶')], default='未置顶', max_length=32)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('max_people_num', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=500)),
                ('last_time', models.DateTimeField()),
                ('next_time', models.DateTimeField()),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('u_time', models.DateTimeField(auto_now=True)),
                ('teacher', models.ManyToManyField(to='teacher.teacher')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
                'db_table': 'course',
                'ordering': ['c_time'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128, null=True)),
                ('over_time', models.CharField(max_length=128)),
                ('url', models.CharField(max_length=500)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('u_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
                'db_table': 'video',
                'ordering': ['c_time'],
            },
        ),
    ]
