import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a Gen Z style personal health coach.
Give safe lifestyle advice only.
Keep answers short and motivating.
"""

def ask_coach(profile, question):

    prompt = f"""
Age: {profile['age']}
Goal: {profile['goal']}
Sleep: {profile['sleep']}
Activity: {profile['activity']}

Question: {question}
"""

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return resp.choices[0].message.content


def generate_plan(goal):
    return ask_coach(
        {"age": "young", "goal": goal, "sleep": "7", "activity": "moderate"},
        f"Create a one-day health plan for {goal}"
    )
