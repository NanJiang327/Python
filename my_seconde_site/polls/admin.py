from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 使在admin中pub_date排序在question_text前
    # fields = ['pub_date', 'question_text']


    # 将表单分为几个字段集：
    fieldsets = [
        ('Question information', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    # 将choice选项添加进question中
    inlines = [ChoiceInline]

    # 默认情况下，Django 显示每个对象的 str() 返回的值。
    # 但有时如果我们能够显示单个字段，它会更有帮助。
    # 为此，使用 list_display 后台选项，它是一个包含要显示的字段名的元组，在更改列表页中以列的形式展示这个对象：
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # was_published_recently 需要在models.Question中设置

    # 添加一个过滤器侧边栏
    list_filter = ['pub_date']

    # 添加一个搜索栏
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)