from django.contrib import admin
from .models import Company, Project


class ProjectInline(admin.TabularInline):
    extra = 0
    model = Project


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = (ProjectInline,)


