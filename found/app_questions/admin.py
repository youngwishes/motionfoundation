from django.contrib import admin
from dvizhenie.core.loading import get_model

Question = get_model('questions', 'Question')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'answer']


admin.site.register(Question, QuestionAdmin)
