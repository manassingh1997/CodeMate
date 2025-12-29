from scraper_app.services.leetcode import scrape_leetcode 
from users_app.models import UserProfile
from django.utils import timezone
from datetime import timedelta


STATS_TTL = timedelta(hours=6)


def update_profile_stats(profile, force=False):
    '''if not force and profile.last_stats_updated:
        if timezone.now() - profile.last_stats_updated < STATS_TTL:
            return
     '''   
    print("Updating profile stats...-----------\n",profile.leetcode_username)
    if profile.leetcode_username:
        data = scrape_leetcode(
            profile.leetcode_username
        )
        profile.leetcode_total_solved = data['total']
        profile.leetcode_easy_solved = data['easy']
        profile.leetcode_medium_solved = data['medium']
        profile.leetcode_hard_solved = data['hard']

    profile.last_stats_updated = timezone.now()
    profile.save()
