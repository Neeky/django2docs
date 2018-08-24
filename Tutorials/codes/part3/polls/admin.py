from django.contrib import admin

# Register your models here.
from .models import Question,Choice

admin.site.register(Question) # 把Question纳入admin站点的管理
admin.site.register(Choice)   # 把Choice纳入admin站点的管理
