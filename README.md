# DevLens 🧠

**DevLens** is an AI-powered tool that analyzes any public GitHub repository and generates a human-readable summary, identifies the tech stack, and suggests a strong resume bullet point for the main contributor.

> Ideal for developers refining their portfolios, recruiters scanning repos, or anyone trying to understand what a repo *actually* does.

---

## ✨ What It Does

- 🔍 Pulls README, languages, and metadata from any public GitHub repo
- 🧠 Uses GPT-3.5 to:
  - Summarize the repo in plain English
  - Identify technologies used
  - Generate a polished resume bullet

---

## 📦 API Usage

### Endpoint

```
POST /analyze
```

### Request Body

```json
{
  "repo": "rushilsingh/luma-backend"
}
```

### Example Response

```json
{
  "summary": "A backend service that audits website performance using Lighthouse and summarizes results using OpenAI.",
  "stack": ["Node.js", "Express", "Puppeteer", "OpenAI API"],
  "resumeBullet": "Built a backend tool that integrates Lighthouse and GPT-3.5 to generate website performance summaries."
}
```

---

## ⚙️ Running Locally

### 1. Clone the repo

```bash
git clone https://github.com/rushilsingh/devlens.git
cd devlens
```

### 2. Create a `.env` file

```env
GITHUB_TOKEN=ghp_...      # GitHub personal access token (classic)
OPENAI_API_KEY=sk-...     # Your OpenAI key
```

> Get your GitHub token [here](https://github.com/settings/tokens)

### 3. Install and run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### 4. Test it out

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"repo": "rushilsingh/luma-backend"}' | jq
```

Or visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

---

## 🛠 Tech Stack

- FastAPI + Uvicorn
- GitHub API (README, languages, metadata)
- OpenAI GPT-3.5
- httpx + python-dotenv

---

## 🧠 Future Ideas

- [ ] VS Code extension
- [ ] Batch analysis for all repos under a user/org
- [ ] Slack/CLI bot for team usage
- [ ] Auto-generate summaries for your starred repos

---

## 📄 License

MIT
