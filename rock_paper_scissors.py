import random
print("⚡ Battle Time: You 🆚 Computer! 🤖")

you_dict = {"r ": 1, "s": -1, "p": 0 , "q":2}
you_dict_rev = {1: "Rock", -1: "Scissors", 0: "Paper" ,2:"q" }

userwin = 0 
compwin = 0


while True:
    comp = random.choice([1, -1, 0])
    you_str = input("Enter your choice R/P/S to play game or Q for quit: ").lower()
    you = you_dict.get(you_str)

    if you==2:
        break

    print(f"you chose {you_dict_rev[you]}\ncomputer chose {you_dict_rev[comp]}")

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

print(f"RESULTS:\nYou win {userwin} times and Computer win {compwin} times ")

# this logic can also be implemented like this: but this may affect readability of the program
"""if(comp-you==-2 or comp-you==1):
        print("you win ")
else:
        print("you lose")"""
