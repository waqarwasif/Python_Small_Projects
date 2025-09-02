import random

comp = random.choice([1, -1, 0])
you_str = input(" Enter your choice g/s/w to play game: ")
you_dict = {"g": 1, "s": -1, "w": 0}
you_dict_rev = {1: "Gun🔫", -1: "Snake🐍", 0: "Water🌊"}
you = you_dict[you_str]

print(f"you chose {you_dict_rev[you]}\ncomputer chose {you_dict_rev[comp]}")

if comp == you:
    print("It's a Tie")
else:
    if comp == 1 and you == 0:
        print("You win 🎉")
    elif comp == 1 and you == -1:
        print("Computer win 😐")
    elif comp == -1 and you == 0:
        print(" Computer win 😐")
    elif comp == -1 and you == 1:
        print("You win 🎉")
    elif comp == 0 and you == 1:
        print("You win 🎉")
    elif comp == 0 and you == -1:
        print("Computer win 😐")
    else:
        print("Something went wrong!")

    # this logic can also be implemented like this: but this may affect readability of the program

    """if(comp+you==0 or comp+you==1):
        print("you win ")
    else:
        print("you lose")"""
