import random
import string

def pass_generator(min_len,digits,special):

    pool = list(string.ascii_letters)
    if digits:
        pool+=list(string.digits)
    if special:
        pool+=list(string.punctuation)

    pwd = []
    if digits:
        pwd.append(random.choice(string.digits))
    if special:
        pwd.append(random.choice(string.punctuation))    

    while len(pwd)< min_len:
        pwd.append(random.choice(pool))

    random.shuffle(pwd) 
    return"".join(pwd)

min_len = int(input("Enter password length : "))
digits = input("Do you want to add digits to password? (yes/no)").lower()=="yes"
special = input("Do you want to add special characters to password? (yes/no)").lower() == "yes"

password = pass_generator(min_len,digits,special)
print(f"Your secure password is: {password}")
