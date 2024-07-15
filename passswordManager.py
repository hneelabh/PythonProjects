pwd = input("\nWhat is the master password? ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, pwd = data.split(" | ")
            print("User :", user, ", Password :", pwd)

def add():
    name = input("Account Name : ")
    pwd = input("Password : ")

    with open('passwords.txt', 'a') as f:
        f.write(name + " | " +  pwd + "\n")

while True:
    mode = input("\nSelect the mode.\nPress 1 to view, 2 to add, and any other key to exit : ")
    if mode == "1":
        view()
    elif mode == "2":
        add()
    else:
        break
    continue

