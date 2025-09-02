import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="🎮", layout="centered")

# Title
st.markdown(
    "<h1 style='text-align: center; color: #FF5733;'>🎮 Rock – Paper – Scissors ⚡</h1>",
    unsafe_allow_html=True,
)

# Initialize session state
if "userwin" not in st.session_state:
    st.session_state.userwin = 0
if "compwin" not in st.session_state:
    st.session_state.compwin = 0
if "rounds" not in st.session_state:
    st.session_state.rounds = []

# Game Choices
choices = {"🪨 Rock": 1, "📄 Paper": 0, "✂️ Scissors": -1}
choices_rev = {1: "Rock", 0: "Paper", -1: "Scissors"}

# Step 1: User chooses
st.subheader("🎮 Choose Your Move")
user_choice = st.radio("Pick one:", list(choices.keys()), horizontal=True, index=None)

# Step 2: Play button
if st.button("▶️ Play Round", use_container_width=True):
    if user_choice is not None:
        you = choices[user_choice]
        comp = random.choice([1, 0, -1])

        # Show choices
        st.markdown(
            f"<h3 style='text-align:center;'>👉 You chose <b>{choices_rev[you]}</b></h3>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<h3 style='text-align:center;'>🤖 Computer chose <b>{choices_rev[comp]}</b></h3>",
            unsafe_allow_html=True,
        )

        # Decide winner
        if you == comp:
            st.markdown(
                "<h2 style='color: orange; text-align:center;'>😐 It's a Tie!</h2>",
                unsafe_allow_html=True,
            )
            result = "Tie"
        elif (
            (comp == 1 and you == 0)
            or (comp == -1 and you == 1)
            or (comp == 0 and you == -1)
        ):
            st.session_state.userwin += 1
            st.markdown(
                "<h2 style='color: green; text-align:center;'>🎉 YOU WIN!</h2>",
                unsafe_allow_html=True,
            )
            result = "You"
        else:
            st.session_state.compwin += 1
            st.markdown(
                "<h2 style='color: red; text-align:center;'>❌ Computer Wins!</h2>",
                unsafe_allow_html=True,
            )
            result = "Computer"

        # Save history
        st.session_state.rounds.append((choices_rev[you], choices_rev[comp], result))

    else:
        st.warning("⚠️ Please choose Rock, Paper, or Scissors before playing.")

# Scoreboard
st.subheader("🏆 Scoreboard")
st.markdown(
    f"<h3 style='text-align:center;'>😊 You: {st.session_state.userwin} | 🤖 Computer: {st.session_state.compwin}</h3>",
    unsafe_allow_html=True,
)

# Round history
if st.session_state.rounds:
    st.subheader("📜 Game History")
    for idx, (u, c, r) in enumerate(st.session_state.rounds[::-1], 1):
        st.write(
            f"Round {len(st.session_state.rounds) - idx + 1}: You → {u}, Computer → {c}, Result → {r}"
        )

# Reset button
if st.button("🔄 Reset Game"):
    st.session_state.userwin = 0
    st.session_state.compwin = 0
    st.session_state.rounds = []
    st.success("Game has been reset! 🚀")
