from fastapi import FastAPI
import requests

app = FastAPI()

NASA_API_KEY = "DEMO_KEY"  # replace with your real key later

@app.get("/")
def read_root():
    return {"message": "Welcome to Space Discovery AI 🚀"}

@app.get("/facts")
def get_space_facts():
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    return {
        "title": data.get("title"),
        "date": data.get("date"),
        "explanation": data.get("explanation"),
        "image_url": data.get("url")
    }
