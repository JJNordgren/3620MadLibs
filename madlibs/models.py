from django.conf import settings
from django.db import models


class StoryTemplate(models.Model):
    title = models.CharField(max_length=120)
    template_text = models.TextField()

    def __str__(self):
        return self.title


class Submission(models.Model):
    story = models.ForeignKey(StoryTemplate, on_delete=models.CASCADE, related_name="submissions")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    data = models.JSONField()
    rendered_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        owner = self.user.username if self.user else "Anonymous"
        return f"{owner} - {self.story.title} ({self.created_at:%Y-%m-%d %H:%M})"
