import requests


def scrape_leetcode(username: str) -> int:
    if not username:
        return {
            "total": 0,
            "easy": 0,
            "medium": 0,
            "hard": 0,
        }

    url = "https://leetcode.com/graphql"

    query = """
    query getUserProfile($username: String!) { matchedUser(username: $username) { submitStatsGlobal { acSubmissionNum { difficulty count } } } }
    """

    payload = {
        "query": query,
        "variables": {"username": username},
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()

        stats = (
            data.get("data", {})
            .get("matchedUser", {})
            .get("submitStatsGlobal", {})
            .get("acSubmissionNum", [])
        )

        result = {
            "total": 0,
            "easy": 0,
            "medium": 0,
            "hard": 0,
        }

        for item in stats:
            diff = item.get("difficulty")
            count = item.get("count", 0)

            if diff == "All":
                result["total"] = count
            elif diff == "Easy":
                result["easy"] = count
            elif diff == "Medium":
                result["medium"] = count
            elif diff == "Hard":
                result["hard"] = count

        return result

    except Exception:
        return 0
