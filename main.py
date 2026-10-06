from fastapi import FastAPI

app = FastAPI(title="FastAPI starter")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello from your own server"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
