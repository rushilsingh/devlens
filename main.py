from fastapi import FastAPI, Request
from pydantic import BaseModel
from github import fetch_repo_data
from summarizer import summarize_repo

app = FastAPI()

class RepoRequest(BaseModel):
    repo: str  # e.g. "rushilsingh/luma-backend"

@app.post("/analyze")
async def analyze_repo(body: RepoRequest):
    data = await fetch_repo_data(body.repo)
    summary = await summarize_repo(data)
    return summary