import random
print("Number Guessing Game")
number = random.randint(1, 100) #if not include 100 so random.randrange(1,100)
guess = None
attempts = 0
while guess != number:
    attempts+=1

    guess = input("Guess a number between 1 and 100: ")
    if guess.isdigit():
        guess=int(guess)

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! You guessed it 🎉")
    else:
        attempts -= 1 #attemps not count for non digit value
        print("Enter a number next time ")

print(f"You got it right in {attempts} attemps")    
if attempts<4:
    print("You have done a Great job 👍")
else:
    print("Now try again guessing in minimum attempts")    
