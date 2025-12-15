import requests
from bs4 import BeautifulSoup
import re

def scrape_gfg(username: str) -> dict:
    if not username:
        return 0
    
    url = f"https://auth.geeksforgeeks.org/profile/{username}?tab=activity"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        res = request.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')

        solved_label = soup.find('p', string=re.compile("Problems Solved", re.I))
        if not solved_label:
            return 0
        
        solved_value = solved_label.find_next("p")
        return int(solved_value.text.strip())
    
    except Exception as e:
        print("GFG scrape error:", e)
        return 0