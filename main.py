from auth import login
from users import save_users, load_users
from logger import log_action


def menu():
    users = load_users()

    while True:
        print("\n--- User Management System ---")
        print("1. Add user")
        print("2. List users")
        print("3. Save users")
        print("4. Load users")
        print("5. Quit")
        print("6. Delete user")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            while True:
                name = input(
                    "Enter user (or type 'exit' to return to menu): "
                ).strip().capitalize()

                if name.lower() == "exit":
                    break

                if name in users:
                    print(f"{name} already exists")
                    log_action(f"ADD failed (duplicate): {name}")
                else:
                    users.append(name)
                    print(f"{name} added successfully")
                    log_action(f"ADD user {name}")

        elif choice == "2":
            if not users:
                print("No users found.")
            else:
                for user in users:
                    print(user)

        elif choice == "3":
            save_users(users)

        elif choice == "4":
            users = load_users()

        elif choice == "5":
            save_users(users)
            log_action("EXIT system")
            print("Users auto-saved. Goodbye!")
            break

        elif choice == "6":
            while True:
                name = input(
                    "Enter user to delete (or type 'exit' to return to menu): "
                ).strip().capitalize()

                if name.lower() == "exit":
                    break

                if name in users:
                    users.remove(name)
                    print(f"{name} deleted successfully")
                    log_action(f"DELETE user {name}")
                else:
                    print(f"{name} not found")
                    log_action(f"DELETE failed (not found): {name}")

        else:
            print("Invalid choice")
            log_action(f"INVALID menu choice: {choice}")


def main():
    log_action("SYSTEM started")
    login()
    menu()


main()
