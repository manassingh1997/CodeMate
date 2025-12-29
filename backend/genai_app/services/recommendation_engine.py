import json
from analytics.services.coding_analytics import get_user_coding_analytics 
from genai_app.services.groq_client import call_groq

def build_prompt(analytics: dict) -> str:
    return f"""
You are an AI backend service.

STRICT RULES:
- Return ONLY valid JSON
- Do NOT include markdown
- Do NOT include explanations
- Do NOT include extra text
- Follow the schema EXACTLY

JSON schema:
{{
  "focus_summary": string,
  "today_plan": {{
    "daily_problem_target": number,
    "difficulty_focus": string
  }},
  "recommended_problems": [
    {{
      "title": string,
      "difficulty": "Easy" | "Medium" | "Hard",
      "reason": string
    }}
  ]
}}

User analytics (DO NOT return these, only use internally):
- Total solved: {analytics['total_solved']}
- Difficulty breakdown: {analytics['difficulty_breakdown']}
- Top topics: {analytics['top_topics']}
- Last 7 days solved: {analytics['last_7_days_solved']}

Task:
1. Decide TODAY's focus based on weaknesses
2. Suggest a realistic daily target
3. Recommend ONLY 3 problems (prioritized)
"""



def get_ai_recommendations(user):
    analytics = get_user_coding_analytics(user)
    prompt = build_prompt(analytics)

    raw_response = call_groq(prompt)

    try:
        parsed = json.loads(raw_response)
    except json.JSONDecodeError:
        return {
            "focus_summary": "Unable to generate recommendations right now.",
            "today_plan": {
                "daily_problem_target": 0,
                "difficulty_focus": "N/A"
            },
            "recommended_problems": []
        }

    return parsed
