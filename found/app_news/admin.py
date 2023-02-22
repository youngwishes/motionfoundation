from django.contrib import admin
from django.utils.safestring import mark_safe

from dvizhenie.core.loading import get_model


News = get_model('news', 'News')


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'get_html_photo']
    date_hierarchy = 'created_at'
    list_filter = ['title', 'created_at', 'updated_at']
    empty_value_display = '-empty-'

    @admin.decorators.display(description="Photo")
    def get_html_photo(self, instance):
        if instance.picture:
            return mark_safe(
                f"<a href='{instance.picture.url}'>"
                f"<img src='{instance.picture.url}' width=75>"
                f"</a>"
            )


admin.site.register(News, NewsAdmin)
