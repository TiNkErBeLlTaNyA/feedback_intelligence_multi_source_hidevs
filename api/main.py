from fastapi import FastAPI
from utils.db import load_from_db

app = FastAPI(title="Feedback Intelligence API")

# ===== HOME =====
@app.get("/")
def home():
    return {
        "message": "Feedback Intelligence API is running",
        "available_endpoints": ["/summary", "/issues", "/sources"]
    }

# ===== SUMMARY =====
@app.get("/summary")
def summary():
    df = load_from_db()

    return {
        "total_reviews": len(df),
        "positive": int((df['sentiment'] == "positive").sum()),
        "negative": int((df['sentiment'] == "negative").sum()),
        "neutral": int((df['sentiment'] == "neutral").sum())
    }

# ===== ISSUES =====
@app.get("/issues")
def issues():
    from analysis.prioritization import prioritize_issues
    df = load_from_db()

    return {
        "top_issues": prioritize_issues(df)
    }

# ===== SOURCES =====
@app.get("/sources")
def sources():
    df = load_from_db()
    return df['source'].value_counts().to_dict()