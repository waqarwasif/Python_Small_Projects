name = input("👤 Enter your name: ")
print(f"✨ Welcome, {name}, to the adventurous jungle game! 🏝️🌴")
print(
    f"🎯  Listen {name}....\n"
    "You are a brave treasure hunter 🧭💎 who enters a forbidden jungle temple. "
    "Every decision changes your destiny. ⚔️\n"
    "Some paths lead to fortune 💰, others to death ☠️, and some trap you forever… 🔒\n"
)


def adv_game():
    q1 = input(
        "🏛️ You stand before the *Cursed Temple*. The gate is open, but you hear whispers... 👻\n"
        "👉 Do you:\n"
        "(A) Enter the temple directly 🚪\n"
        "(B) Search the area outside first 🌲\n"
        "Your choice (A/B): "
    ).lower()

    if q1 == "a":
        print(
            "✅ Well done! You have passed the first hurdle and entered the gate safely 🏰\n"
        )
        q1a = input(
            "⚔️ Inside, you see two bloody gates dripping with mystery... 💉\n"
            "👉 Do you:\n"
            "(A) Open Gate 1 🔑\n"
            "(B) Open Gate 2 🗝️\n"
            "Your choice (A/B): "
        ).lower()
        if q1a == "a":
            print(
                "☠️ Oh no! You entered a haunted kitchen and were killed by a ghost 👻🍽️"
            )
        elif q1a == "b":
            print(
                "🎉 You discovered a hidden warehouse full of treasure and found a way out! 🏆🚪"
            )
        else:
            print("⚠️ Invalid option ❌")

    elif q1 == "b":
        print("🌳 You are now in the middle of the dense jungle... 🐒\n")
        q1b = input(
            "Now you have two dangerous paths... 🕷️\n"
            "👉 Do you:\n"
            "(A) Explore the dark side 🌑\n"
            "(B) Search between the bushes 🌿\n"
            "Your choice (A/B): "
        ).lower()
        if q1b == "a":
            print(
                "💀 You didn’t see the broken bridge 🌉 and fell into the deep river... 🌊"
            )
        elif q1b == "b":
            print("🦁 A wild leopard attacked you! You fought bravely but lost ☠️")
        else:
            print("⚠️ Invalid option ❌")

    else:
        print("⚠️ Invalid option ❌")


while True:
    play = input("\n🔄 Do you want to play the game again? (yes/no) ").lower()

    if play == "yes":
        adv_game()
    elif play == "no":
        print("🙏 Thanks for playing! Goodbye 👋✨")
        break
    else:
        print("⚠️ Invalid input. Please type 'yes' ✅ or 'no' ❌.")
