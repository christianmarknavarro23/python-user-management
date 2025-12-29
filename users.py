from pathlib import Path
from logger import log_action

FILE_PATH = r"C:\Projects\user_management\users.txt"

def save_users(users):
    with open(FILE_PATH, "w") as file:
        for user in users:
            file.write(user + "\n")
    print("Users saved successfully")
    log_action(f"SAVE users ({len(users)})")


def load_users():
    users = []
    path = Path(FILE_PATH)

    if not path.is_file():
        print("No saved users found")
        log_action("LOAD users failed (file not found)")
        return users

    with open(FILE_PATH, "r") as file:
        for line in file:
            cleaned = line.strip()
            if cleaned:
                users.append(cleaned)

    print(f"Loaded {len(users)} users")
    log_action(f"LOAD users ({len(users)})")
    return users
