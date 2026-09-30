from fastapi import FastAPI
from routes import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "LegalEase API is running"}

app.include_router(router)
