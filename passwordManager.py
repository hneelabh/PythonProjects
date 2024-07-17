from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()

def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, pwd = data.split(" | ")
            print("User :", user, ", Password :", fer.decrypt(pwd.encode()).decode())


def add():
    name = input("Account Name : ")
    pwd = input("Password : ")

    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("\nSelect the mode.\nPress 1 to view, 2 to add, and any other key to exit : ")
    if mode == "1":
        view()
    elif mode == "2":
        add()
    else:
        break
    continue

