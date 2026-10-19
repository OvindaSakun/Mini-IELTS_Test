import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from google import genai
from google.genai import types
from tenacity import retry, wait_exponential, stop_after_attempt

app = FastAPI()

# Automatically picks up GEMINI_API_KEY from your environment variables
client = genai.Client()

# 1. Define the exact JSON structure we need using Pydantic
class Question(BaseModel):
    id: str
    prompt: str
    answer: str
    options: list[str]

class ListeningSection(BaseModel):
    speechText: str
    notes: str
    questions: list[Question]

class Paragraph(BaseModel):
    tag: str
    text: str

class ReadingSection(BaseModel):
    title: str
    paragraphs: list[Paragraph]
    questions: list[Question]

class WritingSection(BaseModel):
    prompt: str

class SpeakingSection(BaseModel):
    cueCard: str

class ExamModel(BaseModel):
    id: str
    listening: ListeningSection
    reading: ReadingSection
    writing: WritingSection
    speaking: SpeakingSection

@app.get("/")
def read_root():
    # Serves your HTML file directly from the same directory
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

@retry(stop=stop_after_attempt(4), wait=wait_exponential(multiplier=1, min=2, max=10), reraise=True)
def fetch_exam_from_gemini():
    return client.models.generate_content(
        model='gemini-3.5-flash-lite',
        contents='Generate a completely unique IELTS Academic mock test. Ensure the output strictly follows the required JSON schema.',
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ExamModel,
            temperature=0.9 # Higher temperature forces more diverse randomization
        )
    )

@app.get("/api/generate-exam")
def generate_exam():
    try:
        response = fetch_exam_from_gemini()
        
        # response.parsed contains the validated Pydantic object, completely bypassing JSON decoding errors
        return JSONResponse(content=response.parsed.model_dump())
        
    except Exception as e:
        print(f"Backend Generation Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
