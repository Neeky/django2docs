from django.contrib import admin

# Register your models here.
from .models import Question,Choice

#admin.site.register(Question) # 把Question纳入admin站点的管理
#admin.site.register(Choice)   # 把Choice纳入admin站点的管理

#class QuestionAdmin(admin.ModelAdmin):
#    """
#    调整Question字段的默认次序由 question_text pub_date 到 pub_date question_text
#    """
#    fields = ['pub_date', 'question_text']
#
#
#admin.site.register(Question, QuestionAdmin) # 注册变更

#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question_text']}),
#        ('Date information', {'fields': ['pub_date']}),
#    ]
#
#admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)   # 把Choice纳入admin站点的管理

#class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 3
#
#
#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question_text']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#    inlines = [ChoiceInline]
#
#admin.site.register(Question, QuestionAdmin)

#class ChoiceInline(admin.TabularInline):
#    model = Choice
#    extra = 3
#
#
#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question_text']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#    inlines = [ChoiceInline]
#    list_display = ('question_text', 'pub_date')
#
#admin.site.register(Question, QuestionAdmin)

#class ChoiceInline(admin.TabularInline):
#    model = Choice
#    extra = 3
#
#
#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question_text']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#    inlines = [ChoiceInline]
#    list_display = ('question_text', 'pub_date','was_published_recently')
#
#admin.site.register(Question, QuestionAdmin)

#class ChoiceInline(admin.TabularInline):
#    model = Choice
#    extra = 3
#
#
#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question_text']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#    inlines = [ChoiceInline]
#    list_display = ('question_text', 'pub_date','was_published_recently')
#    list_filter = ['pub_date'] #根据pub_date过滤
#
#admin.site.register(Question, QuestionAdmin)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date'] #根据pub_date过滤
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


