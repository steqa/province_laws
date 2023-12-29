from django.contrib import admin

from .models import (AdministrativeOffencesCode,
                     AdministrativeOffencesCodeChapter, CriminalCode,
                     CriminalCodeChapter)


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


@admin.register(CriminalCodeChapter)
class CriminalCodeChapterAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'created_at', 'updated_at')
    ordering = ('created_at',)


@admin.register(CriminalCode)
class CriminalCodeAdmin(admin.ModelAdmin):
    list_display = (
        'chapter', 'number',
        'penalty', 'conjunction',
        'compensation', 'conjunction_2',
        'arrest', 'created_at', 'updated_at'
    )
    ordering = ('chapter', 'number')