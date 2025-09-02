import streamlit as st
import random

# App title
st.title("⚡ Rock – Paper – Scissors Game  ")
st.write("Play against the computer and see who wins! 🚀")

# Score state
if "userwin" not in st.session_state:
    st.session_state.userwin = 0
if "compwin" not in st.session_state:
    st.session_state.compwin = 0

# Choices
choices = {"Rock": 1, "Scissors": -1, "Paper": 0}
choices_rev = {1: "Rock", -1: "Scissors", 0: "Paper"}

# Layout: buttons for user
st.subheader("🎮 Your Move")
col1, col2, col3 = st.columns(3)
user_choice = None

if col1.button("🪨 Rock"):
    user_choice = 1
elif col2.button("📄 Paper"):
    user_choice = 0
elif col3.button("✂️ Scissors"):
    user_choice = -1

# When user makes a choice
if user_choice is not None:
    comp_choice = random.choice([1, 0, -1])

    st.write(f"👉 You chose **{choices_rev[user_choice]}**")
    st.write(f"🤖 Computer chose **{choices_rev[comp_choice]}**")

    # Decide winner
    if comp_choice == user_choice:
        st.info("It's a Tie! 😐")
    elif (
        (comp_choice == 1 and user_choice == 0)
        or (comp_choice == -1 and user_choice == 1)
        or (comp_choice == 0 and user_choice == -1)
    ):
        st.success("🎉 You Win!")
        st.session_state.userwin += 1
    else:
        st.error("Computer Wins! 😐")
        st.session_state.compwin += 1

# Scoreboard
st.subheader("🏆 Scoreboard")
st.write(f"😊 You: {st.session_state.userwin}")
st.write(f"🤖 Computer: {st.session_state.compwin}")

# Show Python code
st.subheader("📌 Original Python Code")
st.code(
    """
import random
print("⚡ Battle Time: You 🆚 Computer! 🤖")

you_dict = {"r": 1, "s": -1, "p": 0 , "q":2}
you_dict_rev = {1: "Rock", -1: "Scissors", 0: "Paper" ,2:"q" }

userwin = 0 
compwin = 0

while True:
    comp = random.choice([1, -1, 0])
    you_str = input("Enter your choice R/P/S to play game or Q for quit: ").lower()
    you = you_dict.get(you_str)

    if you==2:
        break

    print(f"you chose {you_dict_rev[you]}\\ncomputer chose {you_dict_rev[comp]}")

    if comp==you:
        print("It's a Tie")

    elif comp == 1 and you == 0:
        print("You win 🎉")
        userwin+=1

    elif comp == -1 and you == 1:
        print("You win 🎉")
        userwin += 1

    elif comp == 0 and you == -1:
        print("You win 🎉")
        userwin += 1

    else:
        compwin += 1
        print("Computer win 😐")

print(f"RESULTS:\\nYou win {userwin} times and Computer win {compwin} times ")
""",
    language="python",
)

# Explanation
st.subheader("💡 Explanation")
st.write(
    """
- We use **dictionary mapping** to assign values to Rock, Paper, and Scissors.
- The **computer's choice** is generated randomly.
- Conditions decide the winner based on the rules of the game.
- In this app, buttons replace `input()` so it's user-friendly for LinkedIn showcase.
"""
)
