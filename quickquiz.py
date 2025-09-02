print("WELCOME TO THE QUIZ GAME 🧠")
play = input("Do you want to play? ")

if( play.lower()!="yes"):
    quit()

print("Let's start playing ")

score = 0

answer1 = input("What does RAM stands for? ")

if(answer1.lower() == "random access memory"):
    print("Correct!🎉")
    score+=1
else:
    print("Incorrect😐")   


answer2 = input("What does ROM stands for? ")

if(answer2.lower() == "read only memory"):
    print("Correct!🎉")
    score += 1
else:
    print("Incorrect😐")   


answer3 = input("What does CPU stands for? ")

if(answer3.lower() == "central processing unit"):
    print("Correct!🎉")
    score += 1
else:
    print("Incorrect😐")  

print(f"Thanks for playing ❤\nYour score is {score}/3") 

rate = int(input("Please rate us out of 5: "))
if(rate>3):
    print("Thank You, Have a nice day!")
else:print("Have a nice day!")