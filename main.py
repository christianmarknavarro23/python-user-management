from auth import login
from users import load_users
from logger import log_action
from menu_ui import show_menu, get_choice
from actions import (
    add_user,
    list_users,
    save_users_action,
    reload_users,
    delete_user,
    quit_program,
)


def menu():
    users = load_users()

    actions = {
        "1": add_user,
        "2": list_users,
        "3": save_users_action,
        "4": reload_users,
        "5": quit_program,
        "6": delete_user,
    }

    while True:
        show_menu()
        choice = get_choice()

        action = actions.get(choice)
        if action:
            users = action(users)
        else:
            print("Invalid choice")
            log_action(f"INVALID menu choice: {choice}")


def main():
    log_action("SYSTEM started")
    login()
    menu()


main()
