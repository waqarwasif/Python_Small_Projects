name = input("Enter your name: ")
print(f"✨ Welcome, {name}, to the Adventurous Game 🏆")
print(
    f"🎯 Listen {name}....\n"
    "You are a treasure hunter 🧭 who enters a forbidden jungle temple 🏯.\n"
    "Every decision changes your destiny... ⚡\n"
    "Some paths lead to fortune 💰, others to death ☠️, and some trap you forever… 🔒\n"
)


def adv_game():
    
    while True:
        q1 = input(
            "🏛️ You stand before the *Cursed Temple*. The gate is open, but you hear whispers... 👻\n"
            "👉 Do you:\n"
            "(A) Enter the temple directly 🚪\n"
            "(B) Search the area outside first 🌲\n"
            "Your choice (A/B): "
        ).lower()

        if q1 == "a":
            print("✅ Well done! You entered the gate safely 🏰\n")

            
            while True:
                q1a = input(
                    "😨 In front of you, there are two gates dripping with blood 💉.\n"
                    "👉 Do you:\n"
                    "(A) Open Gate No.1 🚪\n"
                    "(B) Open Gate No.2 🗝️\n"
                    "Your choice (A/B): "
                ).lower()

                if q1a == "a":
                    print(
                        "👻 You entered a haunted kitchen... A ghost attacks and you die ☠️"
                    )
                    break
                elif q1a == "b":
                    print(
                        "🎉 You found a secret warehouse with treasure and escaped safely! 🪙✨"
                    )
                    break
                else:
                    print("⚠️ Invalid option. Please type A or B ❌")
            break

        elif q1 == "b":
            print("🌳 You wander into the middle of the jungle... 🌿\n")

            
            while True:
                q1b = input(
                    "Now you face two paths:\n"
                    "👉 Do you:\n"
                    "(A) Walk towards the dark side 🌑\n"
                    "(B) Search between the bushes 🌵\n"
                    "Your choice (A/B): "
                ).lower()

                if q1b == "a":
                    print(
                        "💀 You missed the broken bridge, fell into the river, and drowned 🌊"
                    )
                    break
                elif q1b == "b":
                    print("🦁 A leopard jumps out of the bushes and kills you ☠️")
                    break
                else:
                    print("⚠️ Invalid option. Please type A or B ❌")
            break

        else:
            print("⚠️ Invalid option. Please type A or B ❌")


while True:
    adv_game()
    play = input("\n🔄 Do you want to play the game again? (yes/no) ").lower()

    if play == "yes":
        continue
    elif play == "no":
        print("🙏 Thanks for playing, adventurer! Goodbye 👋✨")
        break
    else:
        print("⚠️ Invalid input. Please type yes or no ❌")
