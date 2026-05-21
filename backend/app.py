from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from recommendation import recommend

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message":"AI Recommendation System Running"
    }

@app.get("/recommend")
def get_recommendation(query:str):

    result = recommend(query)

    return {
        "recommendations": result
    }