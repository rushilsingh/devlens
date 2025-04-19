import httpx
import os
import base64
from dotenv import load_dotenv

load_dotenv()

GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

async def fetch_repo_data(repo_full_name: str):
    """
    Fetch metadata, README, and language stats for a GitHub repo.
    Returns None if the repo is invalid or inaccessible.
    """
    async with httpx.AsyncClient() as client:
        # Fetch basic repo info (fail fast if invalid)
        repo_url = f"{GITHUB_API}/repos/{repo_full_name}"
        repo_res = await client.get(repo_url, headers=headers)
        if repo_res.status_code != 200:
            print(f"[ERROR] Repo not found: {repo_full_name}")
            return None
        repo_info = repo_res.json()

        # Fetch and decode README
        readme_text = ""
        readme_url = f"{GITHUB_API}/repos/{repo_full_name}/readme"
        readme_res = await client.get(readme_url, headers=headers)
        if readme_res.status_code == 200:
            readme_data = readme_res.json()
            encoded = readme_data.get("content", "")
            if readme_data.get("encoding") == "base64":
                try:
                    readme_text = base64.b64decode(encoded).decode("utf-8", errors="ignore")
                except Exception as e:
                    print(f"[WARN] Failed to decode README: {e}")

        # Fetch language breakdown
        languages = {}
        lang_url = f"{GITHUB_API}/repos/{repo_full_name}/languages"
        lang_res = await client.get(lang_url, headers=headers)
        if lang_res.status_code == 200:
            languages = lang_res.json()

        return {
            "name": repo_info.get("name"),
            "full_name": repo_info.get("full_name"),
            "description": repo_info.get("description"),
            "html_url": repo_info.get("html_url"),
            "languages": languages,
            "readme": readme_text
        }

