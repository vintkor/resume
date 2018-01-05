from django.contrib import admin
from .models import Profile, HobieUser, Hobie
from skills_re.models import SkillLevel, UserLanguageLevel
from projects_re.models import Project


class ProjectInline(admin.TabularInline):
    extra = 0
    model = Project


class SkillLevelInline(admin.TabularInline):
    extra = 0
    model = SkillLevel


class UserLanguageLevelInline(admin.TabularInline):
    extra = 0
    model = UserLanguageLevel


class HobieUserInline(admin.TabularInline):
    extra = 0
    model = HobieUser


@admin.register(HobieUser)
class HobieUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Hobie)
class HobieAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created',)
    inlines = (SkillLevelInline, UserLanguageLevelInline, HobieUserInline, ProjectInline)
