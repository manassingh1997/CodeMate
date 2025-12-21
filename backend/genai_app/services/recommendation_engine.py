import json
from analytics.services.coding_analytics import get_user_coding_analytics 
from genai_app.services.groq_client import call_groq

def build_prompt(analytics: dict) -> str:
    if analytics["total_solved"] == 0:
        return """
You are an AI backend service.

STRICT RULES:
- Return ONLY valid JSON
- Do NOT include markdown
- Do NOT include explanations
- Do NOT include extra text

JSON schema (must match exactly):
{
  "level": "beginner",
  "daily_problem_target": number,
  "roadmap": [string],
  "recommended_problems": [
    {
      "title": string,
      "difficulty": "easy" | "medium",
      "reason": string
    }
  ]
}

User status:
- Solved problems: 0

Task:
1. Create a beginner DSA roadmap
2. Suggest daily problem count
3. Recommend first 10 LeetCode problems
"""
    return f"""
You are an AI backend service.

STRICT RULES:
- Return ONLY valid JSON
- Do NOT include markdown
- Do NOT include explanations
- Do NOT include extra text

JSON schema (must match exactly):
{{
  "weak_topics": [string],
  "recommended_problems": [
    {{
      "topic": string,
      "difficulty": "easy" | "medium" | "hard",
      "description": string
    }}
  ],
  "improvement_strategy": {{
    "short_term": {{
      "goal": string,
      "action": string
    }},
    "long_term": {{
      "goal": string,
      "action": string
    }}
  }}
}}

User analytics:
- Total solved: {analytics['total_solved']}
- Difficulty breakdown: {analytics['difficulty_breakdown']}
- Top topics: {analytics['top_topics']}
- Last 7 days solved: {analytics['last_7_days_solved']}

Task:
1. Identify weak topics
2. Recommend next problems
3. Suggest improvement strategy
"""


def get_ai_recommendations(user):
    analytics = get_user_coding_analytics(user)
    prompt = build_prompt(analytics)
    
    raw_response = call_groq(prompt)

    try:
        parsed = json.loads(raw_response)
    except json.JSONDecodeError:
        return {
            "error": "AI returned invalid JSON",
            "raw_response": raw_response
        }
    
    return {
        "analytics_snapshot": analytics,
        "recommendations": parsed
    }