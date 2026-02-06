# 🧠 GenAI Personal Health Coach — Gen Z Edition  
### 🚀 AI-Powered Conversational Wellness Assistant

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![GenAI](https://img.shields.io/badge/GenAI-Powered-green.svg)
![Status](https://img.shields.io/badge/Status-Live-success.svg)

---

## 🌟 Overview

**GenAI Personal Health Coach — Gen Z Edition** is an AI-powered conversational wellness assistant designed specifically for Gen Z users. The system uses **Generative AI + Prompt Engineering** to deliver personalized health guidance, daily fitness & diet plans, motivational support, and mood-aware coaching through an interactive chat interface.

Unlike static health apps, this platform dynamically generates lifestyle advice based on user profile, goals, sleep patterns, activity level, and mood — making wellness guidance adaptive, interactive, and personalized.

Built for **GenAI for Gen Z Challenge** as a real-world applied GenAI solution.

---

## 🎯 Problem Statement

Gen Z commonly struggles with:

- ❌ Inconsistent healthy routines  
- ❌ Low fitness motivation  
- ❌ Generic diet/workout plans  
- ❌ Lack of personalized guidance  
- ❌ Mental stress without coaching support  
- ❌ Non-interactive health apps  

Most existing tools are template-based — not conversational or adaptive.

---

## 💡 Solution

We built a **Generative AI Personal Health Coach** that:

- 💬 Chats like a real coach  
- 🧠 Understands user profile  
- 📅 Generates personalized daily plans  
- 🥗 Suggests diet & workouts  
- 🔥 Produces instant motivation  
- 😊 Adapts advice to mood  
- 📊 Calculates lifestyle health score  
- 🗣️ Uses Gen Z friendly tone  

All outputs are generated dynamically using prompt-engineered AI coaching logic.

---

## 🧠 GenAI Usage

Generative AI is used for:

| Feature | GenAI Role |
|----------|------------|
AI Chat Coach | Conversational personalized guidance |
Daily Plan | Dynamic diet + workout generation |
Motivation | On-demand Gen Z style messages |
Mood Coaching | Tone + advice adaptation |
Lifestyle Advice | Profile-aware responses |

Prompt context includes:

- Age  
- Goal  
- Sleep hours  
- Activity level  
- Mood state  

This ensures **personalized output instead of static templates**.

---

## 🏗️ Architecture

User Profile + Query
↓
Streamlit UI
↓
Prompt Builder Engine
↓
GenAI Model API
↓
Personalized Health Response



### 📦 Modules

| File | Responsibility |
|------|----------------|
app.py | UI + interaction logic |
coach_engine.py | GenAI prompt engine |
prompts/ | Prompt templates |
data/ | User data placeholder |
Streamlit Cloud | Deployment |

---

## ⚙️ Tech Stack

- 🐍 Python  
- 🎈 Streamlit  
- 🤖 OpenAI Generative AI API  
- 🧩 Prompt Engineering  
- 💾 Session Memory  
- ☁️ Streamlit Cloud  
- 🗂️ GitHub  

---

## ✨ Features

### 💬 AI Coach Chat
- Conversational GenAI coach  
- Personalized responses  
- Session chat memory  

### 📅 Daily Plan Generator
- One-day personalized plan  
- Diet + workout combined  
- Goal-based generation  

### 🔥 Motivation Engine
- Short Gen Z style motivation  
- On-demand generation  

### 📊 Health Score
- Sleep + activity based score  
- Visual progress indicator  

### 😊 Mood-Based Coaching
- Mood-aware advice  
- Adaptive tone  

### 👤 Profile Personalization
- Advice changes per user input  

---

## 🛡️ Safety Guardrails

The AI is constrained to:

✅ Lifestyle guidance  
✅ Habit improvement  
✅ Motivation  
✅ General wellness advice  

It avoids:

❌ Medical diagnosis  
❌ Drug prescriptions  
❌ Clinical claims  

Prompt guardrails enforce safe behavior.

---

## ▶️ Run Locally

Install dependencies:

pip install -r requirements.txt
Create `.env` file:

OPENAI_API_KEY=your_api_key_here
streamlit run app.py


---

## ☁️ Deploy (Streamlit Cloud)

1. Push repo to GitHub  
2. Deploy via Streamlit Cloud  
3. Add API key:

**App Settings → Secrets**

```toml
OPENAI_API_KEY = "your_key_here"

📂 Project Structure
personal-health-coach/
│
├── app.py
├── requirements.txt
├── utils/
│   └── coach_engine.py
├── prompts/
│   ├── diet_prompt.txt
│   ├── workout_prompt.txt
│   └── motivation_prompt.txt
└── data/
    └── users.json


🔬 Innovation Highlights

🧠 Prompt-engineered coaching AI

😊 Mood-adaptive responses

💬 Conversational wellness UX

⚡ Real-time plan generation

👤 Profile-aware logic

🎯 Gen Z tone optimization

☁️ Lightweight cloud deployable

🎥 Demo Flow

1️⃣ Enter profile
2️⃣ Select mood
3️⃣ Ask AI coach
4️⃣ Generate daily plan
5️⃣ View health score
6️⃣ Get motivation

🌱 Future Scope

Weekly AI planner

Habit tracking dashboard

Wearable integration

Voice interaction

PDF health reports

Multilingual Gen Z mode

Long-term AI memory

🏁 Challenge Category

GenAI for Gen Z — Applied Generative AI Solution

👨‍💻 Author

Faruk
Assistant Professor — IT & CS
GenAI Challenge Project

⭐ If You Like This Project

Give it a star ⭐ and support GenAI innovation for wellness.

