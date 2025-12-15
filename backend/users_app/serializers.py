from rest_framework import serializers
from users_app.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'email',
            'leetcode_username',
            'gfg_username',
            'leetcode_total_solved',
            'gfg_total_solved',
            ]
        read_only_fields = [
            "leetcode_total_solved",
            'gfg_total_solved',
        ]