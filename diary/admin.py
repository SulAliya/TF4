from django.contrib import admin

# Register your models here.
from django.contrib import admin

from diary.models import DiaryEntry


# Register your models here.
@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
    list_filter = ('name', 'description', 'created_at',)
    search_fields = ('name',)
