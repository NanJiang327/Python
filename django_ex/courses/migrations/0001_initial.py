# Generated by Django 2.2.2 on 2019-06-16 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('title', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False, verbose_name='课程名')),
                ('type', models.CharField(choices=[(1, '实战课'), (2, '免费课'), (0, '其他')], default=0, max_length=1, verbose_name='课程类型')),
                ('price', models.PositiveIntegerField(verbose_name='价格')),
                ('volume', models.BigIntegerField(verbose_name='销量')),
                ('online', models.DateField(verbose_name='上线时间')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(db_index=True, max_length=30, primary_key=True, serialize=False, verbose_name='教师名')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Age')),
                ('gender', models.CharField(choices=[(1, 'Male'), (2, 'Female'), (0, 'Secret')], default=0, max_length=1, verbose_name='Gender')),
                ('study_hour', models.PositiveIntegerField(default=0, verbose_name='学习时间(h)')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '学生信息表',
                'verbose_name_plural': '学生信息表',
            },
        ),
        migrations.CreateModel(
            name='Techer',
            fields=[
                ('name', models.CharField(db_index=True, max_length=30, primary_key=True, serialize=False, verbose_name='教师名')),
                ('introduction', models.TextField(default='我很懒, 没有个性签名', verbose_name='简介')),
                ('fans', models.PositiveIntegerField(default=0, verbose_name='粉丝数')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '老师信息表',
                'verbose_name_plural': '老师信息表',
            },
        ),
        migrations.CreateModel(
            name='TecherAssistant',
            fields=[
                ('name', models.CharField(db_index=True, max_length=30, primary_key=True, serialize=False, verbose_name='教师名')),
                ('gender', models.CharField(choices=[(1, 'Male'), (2, 'Female'), (0, 'Secret')], default=0, max_length=1, verbose_name='Gender')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '助教信息',
                'verbose_name_plural': '助教信息',
                'db_table': 'courses_assistant',
            },
        ),
    ]
