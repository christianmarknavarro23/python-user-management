from logger import log_action
from users import save_users, load_users


def add_user(users):
    while True:
        name = input(
            "Enter user (or type 'exit' to return to menu): "
        ).strip().capitalize()

        if name.lower() == "exit":
            return users

        if name in users:
            print(f"{name} already exists")
            log_action(f"ADD failed (duplicate): {name}")
        else:
            users.append(name)
            print(f"{name} added successfully")
            log_action(f"ADD user {name}")


def list_users(users):
    if not users:
        print("No users found.")
    else:
        for user in users:
            print(user)
    return users


def save_users_action(users):
    save_users(users)
    return users


def reload_users(_):
    return load_users()


def delete_user(users):
    while True:
        name = input(
            "Enter user to delete (or type 'exit' to return to menu): "
        ).strip().capitalize()

        if name.lower() == "exit":
            return users

        if name in users:
            users.remove(name)
            print(f"{name} deleted successfully")
            log_action(f"DELETE user {name}")
        else:
            print(f"{name} not found")
            log_action(f"DELETE failed (not found): {name}")


def quit_program(users):
    save_users(users)
    log_action("EXIT system")
    print("Users auto-saved. Goodbye!")
    exit()
