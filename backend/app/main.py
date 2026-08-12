from fastapi import FastAPI

app = FastAPI(
    title="ResearchMind AI",
    description="AI-powered Research Intelligence Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "ResearchMind AI Backend is running",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }