from rest_framework import serializers
from users_app.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'email',
            'leetcode_username',
            'leetcode_total_solved',
            'leetcode_easy_solved',
            'leetcode_medium_solved',
            'leetcode_hard_solved',
            ]
        read_only_fields = [
            "leetcode_total_solved",
            'leetcode_easy_solved',
            'leetcode_medium_solved',
            'leetcode_hard_solved',
        ]