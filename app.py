
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from datetime import datetime
import sqlite3
import os

app = FastAPI()

# Static files and templates setup
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database setup
DATABASE = 'sentiment_analysis.db'

# Ensure database and tables are created
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE sentiment_analysis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        text TEXT NOT NULL,
        sentiment TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')
    # Seed data
    cursor.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')")
    cursor.execute("INSERT INTO sentiment_analysis (user_id, text, sentiment) VALUES (1, 'I love this product!', 'positive')")
    conn.commit()
    conn.close()

# Pydantic models
class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    id: int
    user_id: int
    text: str
    sentiment: str
    created_at: datetime

# Utility function to analyze sentiment
# For demonstration, this is a simple mock function
# Replace with actual sentiment analysis logic

def analyze_sentiment(text: str) -> str:
    if 'love' in text.lower():
        return 'positive'
    elif 'hate' in text.lower():
        return 'negative'
    else:
        return 'neutral'

# Routes
@app.get('/', response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get('/analysis', response_class=HTMLResponse)
async def read_analysis(request: Request):
    return templates.TemplateResponse("analysis.html", {"request": request})

@app.get('/history', response_class=HTMLResponse)
async def read_history(request: Request):
    return templates.TemplateResponse("history.html", {"request": request})

@app.get('/api-docs', response_class=HTMLResponse)
async def read_api_docs(request: Request):
    return templates.TemplateResponse("api_docs.html", {"request": request})

@app.post('/api/analyze', response_model=SentimentResponse)
async def analyze_text(request: SentimentRequest):
    sentiment = analyze_sentiment(request.text)
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sentiment_analysis (user_id, text, sentiment) VALUES (?, ?, ?)", (1, request.text, sentiment))
    conn.commit()
    analysis_id = cursor.lastrowid
    cursor.execute("SELECT * FROM sentiment_analysis WHERE id = ?", (analysis_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return SentimentResponse(id=row[0], user_id=row[1], text=row[2], sentiment=row[3], created_at=row[4])
    raise HTTPException(status_code=404, detail="Analysis not found")

@app.get('/api/history', response_model=List[SentimentResponse])
async def get_history():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sentiment_analysis")
    rows = cursor.fetchall()
    conn.close()
    return [SentimentResponse(id=row[0], user_id=row[1], text=row[2], sentiment=row[3], created_at=row[4]) for row in rows]

@app.get('/api/history/{id}', response_model=SentimentResponse)
async def get_history_item(id: int):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sentiment_analysis WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return SentimentResponse(id=row[0], user_id=row[1], text=row[2], sentiment=row[3], created_at=row[4])
    raise HTTPException(status_code=404, detail="Analysis not found")
