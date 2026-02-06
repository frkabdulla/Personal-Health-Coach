import streamlit as st
from utils.coach_engine import ask_coach, generate_plan

# ---------- Page Setup ----------

st.set_page_config(page_title="GenZ AI Health Coach", page_icon="🧠")

st.title("🧠 GenAI Personal Health Coach (Gen Z Edition)")
st.caption("AI-powered personalized wellness coach for Gen Z 🚀")

# ---------- Health Score Logic ----------

def health_score(sleep, activity):
    score = 50

    if sleep >= 7:
        score += 20
    elif sleep >= 6:
        score += 10

    if activity == "High":
        score += 20
    elif activity == "Moderate":
        score += 10

    return min(score, 100)

# ---------- Sidebar Profile ----------

st.sidebar.header("👤 Your Profile")

age = st.sidebar.number_input("Age", 15, 60, 22)

goal = st.sidebar.selectbox(
    "Goal",
    ["Weight Loss", "Muscle Gain", "General Fitness", "Mental Wellness"]
)

sleep = st.sidebar.slider("Sleep hours", 4, 10, 7)

activity = st.sidebar.selectbox(
    "Activity Level",
    ["Low", "Moderate", "High"]
)

profile = {
    "age": age,
    "goal": goal,
    "sleep": sleep,
    "activity": activity
}

# ---------- Tabs ----------

tab1, tab2, tab3, tab4 = st.tabs([
    "💬 AI Coach Chat",
    "📅 Daily Plan",
    "🔥 Motivation",
    "📊 Health Score"
])

# ---------- CHAT TAB ----------

with tab1:
    st.subheader("Ask Your AI Coach")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_q = st.text_input("Ask about diet, workout, habits", key="chat_input")

    if st.button("Ask Coach", key="ask_btn"):
        if user_q.strip():
            with st.spinner("Coach thinking..."):
                ans = ask_coach(profile, user_q)

            st.session_state.chat_history.append(("You", user_q))
            st.session_state.chat_history.append(("Coach", ans))

    # Display chat history
    for role, msg in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"**🧑 You:** {msg}")
        else:
            st.markdown(f"**🧠 Coach:** {msg}")

# ---------- PLAN TAB ----------

with tab2:
    st.subheader("Generate Your Daily Plan")

    if st.button("Generate Plan", key="plan_btn"):
        with st.spinner("Creating your personalized plan..."):
            plan = generate_plan(goal)
        st.write(plan)

# ---------- MOTIVATION TAB ----------

with tab3:
    st.subheader("Get Instant Motivation")

    if st.button("Motivate Me", key="mot_btn"):
        with st.spinner("Charging motivation..."):
            msg = ask_coach(profile, "Give me a short health motivation")
        st.success(msg)

# ---------- HEALTH SCORE TAB ----------

with tab4:
    st.subheader("Your Lifestyle Health Score")

    score = health_score(sleep, activity)

    st.metric("Health Score", f"{score}/100")

    if score >= 85:
        st.success("Excellent habits — keep going 🔥")
    elif score >= 65:
        st.info("Good — small upgrades will help 👍")
    else:
        st.warning("Needs improvement — coach can guide you 💪")

    st.progress(score / 100)
