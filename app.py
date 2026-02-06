import streamlit as st
from utils.coach_engine import ask_coach, generate_plan
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


st.set_page_config(page_title="GenZ AI Health Coach")

st.title("🧠 GenAI Personal Health Coach (Gen Z Edition)")

# -------- Sidebar --------

st.sidebar.header("Your Profile")

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

# -------- Tabs --------

tab1, tab2, tab3 = st.tabs([
    "💬 AI Coach Chat",
    "📅 Daily Plan",
    "🔥 Motivation"
])

# -------- Chat --------

with tab1:
    st.subheader("Ask AI Coach")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_q = st.text_input("Ask about diet, workout, habits")

    if st.button("Ask Coach"):
        if user_q:
            with st.spinner("Thinking..."):
                ans = ask_coach(profile, user_q)

            st.session_state.chat_history.append(("You", user_q))
            st.session_state.chat_history.append(("Coach", ans))

    for role, msg in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"**🧑 You:** {msg}")
        else:
            st.markdown(f"**🧠 Coach:** {msg}")


# -------- Plan --------

with tab2:
    st.subheader("Daily Plan")

    if st.button("Generate Plan"):
        with st.spinner("Building plan..."):
            plan = generate_plan(goal)
        st.write(plan)

# -------- Motivation --------

with tab3:
    st.subheader("Motivation")

    if st.button("Motivate Me"):
        msg = ask_coach(profile, "Give me a short health motivation")
        st.success(msg)
