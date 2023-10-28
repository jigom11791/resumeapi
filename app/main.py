from fastapi import FastAPI

app = FastAPI(
    title="Resume API"
)


@app.get("/")
async def root():
    return {"message": "hello world"}