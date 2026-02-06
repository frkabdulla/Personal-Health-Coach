import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# ---------- Load Env (for local run) ----------
load_dotenv()

# ---------- Get API Key (Cloud + Local Safe) ----------
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment or Streamlit secrets")

# ---------- OpenAI Client ----------
client = OpenAI(aGIT6MXCUe2QZcxOLHbWx1OjSg1UzZ5VMHDKNY1g)

# ---------- System Prompt ----------
SYSTEM_PROMPT = """
You are a Gen Z style personal health coach.
Give safe lifestyle advice only.
No medical diagnosis.
Keep answers short, practical, and motivating.
"""

# ---------- Ask Coach ----------
def ask_coach(profile, question):

    prompt = f"""
{SYSTEM_PROMPT}

User Profile:
Age: {profile['age']}
Goal: {profile['goal']}
Sleep: {profile['sleep']}
Activity: {profile['activity']}
Mood: {profile.get('mood', 'unknown')}

User Question:
{question}
"""

    resp = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return resp.output_text


# ---------- Plan Generator ----------
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
