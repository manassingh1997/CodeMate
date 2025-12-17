from rest_framework import serializers
from coding_logs.models import CodingLog

class CodingLogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodingLog
        fields = [
            'problem_link',
        ]

    def validate_problem_link(self, value):
        if "leetcode.com/problems/" not in value:
            raise serializers.ValidationError("Only leetcode problem links are allowed")
        return value