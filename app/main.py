from fastapi import FastAPI

SERVICE_NAME = "renewal-demo-service"
SUPPORTED_LINES = ["auto", "home", "umbrella"]

app = FastAPI(title=SERVICE_NAME)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/config")
def config():
    return {
        "service": SERVICE_NAME,
        "supported_lines": SUPPORTED_LINES,
    }
