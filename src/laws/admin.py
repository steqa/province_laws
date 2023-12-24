from django.contrib import admin

from .models import AdministrativeOffencesCodeChapter, AdministrativeOffencesCode


@admin.register(AdministrativeOffencesCodeChapter)
class AdministrativeOffencesCodeChapterAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'created_at', 'updated_at')
    ordering = ('created_at',)


@admin.register(AdministrativeOffencesCode)
class AdministrativeOffencesCodeAdmin(admin.ModelAdmin):
    list_display = (
        'chapter', 'number',
        'notification', 'conjunction_1',
        'penalty', 'conjunction_2',
        'deprivation_driver_license', 'conjunction_3',
        'arrest', 'created_at', 'updated_at'
    )
    ordering = ('chapter', 'number')