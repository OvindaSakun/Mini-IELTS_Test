# Mini IELTS Test Practice

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-005571?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Google Gemini API](https://img.shields.io/badge/Google%20GenAI-Gemini-8E75B2?logo=google&logoColor=white)](https://ai.google.dev/)
[![Uvicorn](https://img.shields.io/badge/Server-Uvicorn-499848?logo=gunicorn&logoColor=white)](https://www.uvicorn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Description

A lightweight mini IELTS practice web application built with FastAPI and Google Gemini. It generates quick sample exercises for all 4 skills (Listening, Reading, Writing, and Speaking) to help users practice the test format with browser-based text-to-speech, audio recording, word counting, and an instant band score summary.

---

## Project Structure

```text
.
├── main.py              # FastAPI server and Gemini API test generation
├── index.html           # Simple frontend interface with audio and scoring
├── data.json            # Sample reading test data reference
├── requirements.txt     # Python package dependencies
├── .gitignore           # Git ignore file
└── README.md            # Project documentation
```

---

## Installation Instructions

### 1. Clone the repository
```bash
git clone https://github.com/OvindaSakun/Mini-IELTS_Test.git
cd Mini-IELTS_Test
```

### 2. Create and activate a virtual environment
- **Windows:**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your Gemini API key
Get an API key from [Google AI Studio](https://aistudio.google.com/) and set the environment variable:

- **Windows (PowerShell):**
  ```powershell
  $env:GEMINI_API_KEY="your_api_key_here"
  ```
- **Windows (CMD):**
  ```cmd
  set GEMINI_API_KEY=your_api_key_here
  ```
- **macOS / Linux:**
  ```bash
  export GEMINI_API_KEY="your_api_key_here"
  ```

---

## Running the Server

Start the local development server:

```bash
uvicorn main:app --port 8000 --reload
```

Then open your browser and navigate to:
```text
http://localhost:8000
```

---

## Scoring Methodology

The overall band score is calculated by taking the average of all four skill section scores and rounding to the nearest half or whole band using standard IELTS rules:

- If the decimal remainder is less than **0.25**, it rounds **down** to the nearest whole band (e.g., 6.1 $\rightarrow$ 6.0).
- If the decimal remainder is between **0.25** and **0.74**, it rounds to the **half band** (e.g., 6.25 $\rightarrow$ 6.5, 6.6 $\rightarrow$ 6.5).
- If the decimal remainder is **0.75** or higher, it rounds **up** to the next whole band (e.g., 6.75 $\rightarrow$ 7.0).

---

## License

This project is licensed under the [MIT License](LICENSE).
