from django.contrib import admin
from .models import Skill, SkillLevel, LanguageLevel, Language, UserLanguageLevel


@admin.register(SkillLevel)
class SkillLevelAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageLevel)
class LanguageLevelAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(UserLanguageLevel)
class UserLanguageLevelAdmin(admin.ModelAdmin):
    pass
