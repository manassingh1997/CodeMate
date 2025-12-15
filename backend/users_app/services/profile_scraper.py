from scraper_app.services.leetcode import scrape_leetcode 
from scraper_app.services.gfg import scrape_gfg
from users_app.models import UserProfile
from django.utils import timezone
from datetime import timedelta


STATS_TTL = timedelta(hours=6)


def update_profile_stats(profile, force=False):
    '''if not force and profile.last_stats_updated:
        if timezone.now() - profile.last_stats_updated < STATS_TTL:
            return
     '''   

    if profile.leetcode_username:
        profile.leetcode_total_solved = scrape_leetcode(
            profile.leetcode_username
        )

    if profile.gfg_username:
        profile.gfg_total_solved = scrape_gfg(
            profile.gfg_username
        )

    profile.last_stats_updated = timezone.now()
    profile.save()
