from django.contrib import admin
from dvizhenie.core.loading import get_model

Question = get_model('questions', 'Question')
Answer = get_model('questions', 'Answer')


class AnswerInline(admin.TabularInline):
    model = Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'answer', 'question']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
