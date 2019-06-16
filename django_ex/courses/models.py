from django.db import models

# Create your models here.
class Techer(models.Model):
    name = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name='教师名')
    introduction = models.TextField(default='我很懒, 没有个性签名', verbose_name='简介')
    fans = models.PositiveIntegerField(default=0, verbose_name='粉丝数')
    created_at = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '老师信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100, primary_key=True, db_index=True, verbose_name='课程名')
    teacher = models.ForeignKey(Techer, null=True, blank=True, on_delete=models.CASCADE, verbose_name='课程讲师')
    type = models.CharField(choices=((1, '实战课'), (2, '免费课'), (0, '其他')), max_length=1, default=0, verbose_name='课程类型')
    price = models.PositiveIntegerField(verbose_name='价格')
    volume = models.BigIntegerField(verbose_name='销量')
    online = models.DateField(verbose_name='上线时间')
    created_at = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        # 获取type字段代表的信息 1, 实战课. 2, 免费课. 3, 其他
        return f"{self.get_type_display()} - {self.title}"


class Student(models.Model):
    name = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name='教师名')
    course = models.ManyToManyField(Course, verbose_name='课程名')
    age = models.PositiveSmallIntegerField(verbose_name='Age')
    gender = models.CharField(choices=((1, 'Male'), (2, 'Female'), (0, 'Secret')), max_length=1, default=0, verbose_name='Gender')
    study_hour = models.PositiveIntegerField(default=0, verbose_name='学习时间(h)')
    created_at = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '学生信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TecherAssistant(models.Model):
    name = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name='教师名')
    teacher = models.OneToOneField(Techer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='教师')
    gender = models.CharField(choices=((1, 'Male'), (2, 'Female'), (0, 'Secret')), max_length=1, default=0, verbose_name='Gender')
    created_at = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '助教信息'
        db_table = "courses_assistant"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name