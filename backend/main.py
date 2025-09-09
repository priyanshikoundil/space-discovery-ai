from fastapi import FastAPI
import requests
from transformers import pipeline
app = FastAPI()

NASA_API_KEY = "CBDN5eQ6onNIjoj9jzcJEDsg7SQ5qtKpKpfhhoZg" 
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
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
@app.get("/summarize")
def summarize_fact():
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    explanation = data.get("explanation", "")
    summary = summarizer(explanation, max_length=50, min_length=20, do_sample=False)
    
    return {
        "title": data.get("title"),
        "summary": summary[0]['summary_text']
    }