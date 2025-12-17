from rest_framework import serializers
from coding_logs.models import CodingLog

class CodingLogCreateSerializer(serializers.ModelSerializer):
    notes = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    class Meta:
        model = CodingLog
        fields = [
            'problem_link',
            'notes',
        ]

    def validate_problem_link(self, value):
        if "leetcode.com/problems/" not in value:
            raise serializers.ValidationError("Only leetcode problem links are allowed")
        return value
    

class CodingLogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodingLog
        fields = [
            'id',
            'problem_title',
            'problem_link',
            'difficulty',
            'topics',
            'notes',
            'logged_at',
        ]