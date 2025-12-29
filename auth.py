from logger import log_action

def login():
    password = None
    while password != "admin3212":
        password = input("Enter password: ")
        if password != "admin3212":
            log_action("LOGIN failed attempt")

    print("Login successful")
    log_action("LOGIN successful")
