from cryptography.fernet import Fernet
'''def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)


def view():
    with open("pass.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            platform,user,password = data.split("|")
            print("Platform: "+ platform+" User: "+user," Password: "+ fer.decrypt(password.encode()).decode)


def add():
    platform = input("Enter the account platform: ")
    name = input("Enter your name: ")
    pwd = input(f"Enter your {platform} password: ")

    with open("pass.txt","a") as f:
        f.write(name + "|" + platform + "|" + fer.encrypt(pwd.encode()).decode + "\n")


while True:
    view_add = input("Would you like to add new password or view the existing ones? (add,view): ").lower()
    if view_add=="add":
        pass
    elif view_add=="view":
        pass
    else:
        print("Invalid mode.")