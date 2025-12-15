import requests


def scrape_leetcode(username: str) -> int:
    if not username:
        return 0

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

        for item in stats:
            if item.get("difficulty") == "All":
                return item.get("count", 0)

        return 0

    except Exception:
        return 0
