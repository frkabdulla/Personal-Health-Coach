import os
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()

# ---------- Read API key securely ----------
api_key = os.getenv("SCALEDOWN_API_KEY")

if not api_key:
    api_key = st.secrets.get("SCALEDOWN_API_KEY")

if not api_key:
    raise ValueError("Missing SCALEDOWN_API_KEY in Streamlit Secrets")

# ---------- Config ----------
BASE_URL = "https://api.scaledown.ai/v1/chat/completions"
MODEL = "gpt-4o-mini"

HEADERS = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

SYSTEM_PROMPT = """
You are a Gen Z style personal health coach.
Give only safe lifestyle advice.
No medical diagnosis.
Short, motivating, practical answers.
"""

# ---------- Core API Call ----------
def call_ai(prompt):

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    r = requests.post(BASE_URL, headers=HEADERS, json=payload, timeout=60)

    if r.status_code != 200:
        return f"API Error {r.status_code}: {r.text}"

    data = r.json()
    return data["choices"][0]["message"]["content"]


# ---------- Public Functions ----------
def ask_coach(profile, question):

    prompt = f"""
User Profile:
Age: {profile['age']}
Goal: {profile['goal']}
Sleep: {profile['sleep']}
Activity: {profile['activity']}
Mood: {profile.get('mood','unknown')}

Question:
{question}
"""

    return call_ai(prompt)


def generate_plan(goal):
    return ask_coach(
        {
            "age": "young",
            "goal": goal,
            "sleep": "7",
            "activity": "moderate"
        },
        f"Create a one-day diet and workout plan for {goal}"
    )
