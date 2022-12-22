from django.contrib import admin
from dvizhenie.core.loading import get_model


News = get_model('news', 'News')


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'short_description', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    list_filter = ['title', 'created_at', 'updated_at']
    empty_value_display = '-empty-'
    filter_horizontal = ('files',)


admin.site.register(News, NewsAdmin)
