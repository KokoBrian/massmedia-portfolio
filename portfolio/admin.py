from django.contrib import admin
from .models import Project, GalleryItem

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('media_type',)

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('caption', 'created_at')
