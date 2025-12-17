from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class CodingLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem_link = models.URLField(unique=True)
    problem_title = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=30)
    topics = models.JSONField(default=list, blank=True)
    logged_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-logged_at"]
        unique_together = ("user", "problem_link")

    def __str__(self):
        return f"{self.user} - {self.problem_title}"