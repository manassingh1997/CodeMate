from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    #user_input
    leetcode_username = models.CharField(max_length=100, blank=True)
    gfg_username = models.CharField(max_length=100,blank=True)

    # scraped stats (updated later)
    leetcode_total_solved = models.IntegerField(default=0)
    gfg_total_solved = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    last_stats_updated = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} profile"
    


