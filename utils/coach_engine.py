import os
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()

# ---------- API KEY ----------
api_key = os.getenv("SCALEDOWN_API_KEY") or st.secrets.get("SCALEDOWN_API_KEY")

# ---------- CONFIG ----------
BASE_URL = "https://api.scaledown.ai/v1/chat/completions"
MODEL = "gpt-4o-mini"

HEADERS = {
    "Authorization": f"Bearer {api_key}" if api_key else "",
    "Content-Type": "application/json"
}

SYSTEM_PROMPT = """
You are a Gen Z style personal health coach.
Give only safe lifestyle advice.
No medical diagnosis.
Short, motivating, practical answers.
"""

# ---------- FALLBACK (Demo Safe) ----------
def fallback_answer(question):
    q = question.lower()

    if "diet" in q:
        return "🥗 Eat simple home food, add protein, reduce sugar, drink more water."
    if "workout" in q or "exercise" in q:
        return "🏃 20–30 min walk + basic bodyweight workout is a great start."
    if "motivation" in q:
        return "🔥 Small daily actions beat perfect plans. Just start today."
    if "plan" in q:
        return "📅 Wake early, move daily, eat clean, sleep 7+ hours."

    return "💡 Stay consistent, hydrate well, move your body daily."

# ---------- Core API Call ----------
def call_ai(prompt):

    if not api_key:
        return fallback_answer(prompt)

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        r = requests.post(
            BASE_URL,
            headers=HEADERS,
            json=payload,
            timeout=25
        )

        if r.status_code != 200:
            return fallback_answer(prompt)

        data = r.json()
        return data["choices"][0]["message"]["content"]

    except requests.exceptions.ConnectionError:
        return fallback_answer(prompt)

    except Exception:
        return fallback_answer(prompt)


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
