import requests
import re

def scrape_problem_from_link(problem_link: str) -> dict:
    """
    Extracts problem slug and fetches title + difficulty from leetcode
    """
    match = re.search(r"leetcode.com/problems/([^/]+)", problem_link)

    if not match:
        raise ValueError("Invalid LeetCode problem link")
    
    slug = match.group(1)

    url = "https://leetcode.com/graphql"

    query = """
    query getQuestionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug){
        title
        difficulty
        topicTags {
            name
        }
      }
    }
    """

    payload = {
        "query": query,
        "variables": {"titleSlug": slug}
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.post(url, json=payload, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()["data"]["question"]

    return {
        "title": data["title"],
        "difficulty": data["difficulty"],
        "topics": [t["name"] for t in data["topicTags"]]
    }