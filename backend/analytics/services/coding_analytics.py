from collections import Counter
from datetime import timedelta
from django.utils.timezone import now

from coding_logs.models import CodingLog

def get_user_coding_analytics(user):
    logs = CodingLog.objects.filter(user=user)

    total_solved = logs.count()

    difficulty_count = Counter(logs.values_list('difficulty', flat=True))

    topic_counter = Counter()
    for log in logs:
        topic_counter.update(log.topics or [])

    last_7_days = logs.filter(
        logged_at__gte=now() - timedelta(days=7)
    ).count()

    return {
        "total_solved": total_solved,
        "difficulty_breakdown": {
            "easy": difficulty_count.get('Easy', 0),
            "medium": difficulty_count.get("Medium", 0),
            "hard": difficulty_count.get("Hard", 0),
        },
        "top_topics": [
            {"topic": topic, "count": count}
            for topic, count in topic_counter.most_common(5)
        ],
        "last_7_days_solved": last_7_days
    }