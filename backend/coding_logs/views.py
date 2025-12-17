from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from coding_logs.serializers import CodingLogCreateSerializer
from coding_logs.models import CodingLog
from scraper_app.services.leetcode_problem import scrape_problem_from_link
# Create your views here.


class CodingLogCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CodingLogCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        problem_link = serializer.validated_data['problem_link']

        # prevent duplicates
        if CodingLog.objects.filter(
            user = request.user,
            problem_link = problem_link
        ).exists():
            return Response(
                {"error": "Problem already looged"},
                status=400
            )
        
        scraped = scrape_problem_from_link(problem_link)

        log = CodingLog.objects.create(
            user=request.user,
            problem_link=problem_link,
            problem_title=scraped['title'],
            difficulty=scraped['difficulty'],
            topics=scraped['topics']
        )

        return Response(
            {
                "message": "Problem logged successfully",
                "data": {
                    "title": log.problem_title,
                    "difficulty": log.difficulty,
                    "topics": log.topics,
                }
            }, status=201
        )