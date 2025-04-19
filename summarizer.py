import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

openai = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def summarize_repo(data: dict):
    repo_name = data.get("full_name", "this repository")
    readme = data.get("readme", "")[:5000]  # Trim for token safety
    languages = data.get("languages", {})
    lang_list = ", ".join(languages.keys()) or "Unknown"

    prompt = f"""
You are a senior software engineer analyzing a GitHub repository.

Repository: {repo_name}
Languages: {lang_list}

README (truncated if too long):
{readme}

Tasks:
1. Summarize what this repository does in plain English (1–2 sentences).
2. Identify the tech stack (based on code and README).
3. Suggest a strong resume bullet point for the main contributor.

Respond in this JSON format:

{{
  "summary": "...",
  "stack": ["Tech1", "Tech2", ...],
  "resumeBullet": "..."
}}
"""

    response = await openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{ "role": "user", "content": prompt }],
        temperature=0.7
    )

    content = response.choices[0].message.content.strip()

    try:
        return eval(content)  # assuming GPT follows the format
    except Exception:
        return { "error": "Failed to parse GPT response", "raw": content }

