from django.contrib import admin
from .models import Project, Inquiry

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'project_type', 'created_at')
    readonly_fields = ('created_at',)