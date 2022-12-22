from django.contrib import admin
from dvizhenie.core.loading import get_model


Activity = get_model('activities', 'Activity')
ActivityType = get_model('activities', 'ActivityType')


class ActivityInline(admin.TabularInline):
    model = Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'activity_type']
    ordering = ('activity_type',)
    filter_horizontal = ('files',)


class ActivityTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [ActivityInline]


admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityType, ActivityTypeAdmin)
