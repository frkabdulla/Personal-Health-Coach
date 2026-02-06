import streamlit as st
from utils.coach_engine import ask_coach, generate_plan

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

    q = st.text_input("Ask about diet, workout, habits")

    if st.button("Ask Coach"):
        if q:
            with st.spinner("Thinking..."):
                ans = ask_coach(profile, q)
            st.write(ans)

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
