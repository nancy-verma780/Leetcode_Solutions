import requests
import re

USERNAME = "nancyverma780"

query = """
query getUserProfile($username: String!) {
  matchedUser(username: $username) {
    submitStats: submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
"""

response = requests.post(
    "https://leetcode.com/graphql",
    json={
        "query": query,
        "variables": {"username": USERNAME}
    },
    headers={
        "Content-Type": "application/json"
    }
)

data = response.json()

stats = data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]

easy = medium = hard = 0

for item in stats:
    if item["difficulty"] == "Easy":
        easy = item["count"]
    elif item["difficulty"] == "Medium":
        medium = item["count"]
    elif item["difficulty"] == "Hard":
        hard = item["count"]

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = re.sub(
    r'https://img\.shields\.io/badge/Easy-\d+-22C55E\?style=for-the-badge',
    f'https://img.shields.io/badge/Easy-{easy}-22C55E?style=for-the-badge',
    readme
)

readme = re.sub(
    r'https://img\.shields\.io/badge/Medium-\d+-FBBF24\?style=for-the-badge',
    f'https://img.shields.io/badge/Medium-{medium}-FBBF24?style=for-the-badge',
    readme
)

readme = re.sub(
    r'https://img\.shields\.io/badge/Hard-\d+-EF4444\?style=for-the-badge',
    f'https://img.shields.io/badge/Hard-{hard}-EF4444?style=for-the-badge',
    readme
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("README updated successfully!")
