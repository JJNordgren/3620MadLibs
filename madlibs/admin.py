from django.contrib import admin
from .models import StoryTemplate, Submission


@admin.register(StoryTemplate)
class StoryTemplateAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "template_text")


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "story", "user", "created_at")
    list_filter = ("story", "created_at")
    search_fields = ("rendered_text",)
