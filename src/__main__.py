import os
import termcolor
import json
from encryption import *
from passwords import *

database = None


def display_help():
    banner = """
    ██╗    ██╗██╗███╗   ██╗████████╗██╗  ██╗███████╗██████╗     ███████╗████████╗ ██████╗ ██████╗  █████╗  ██████╗ ███████╗
    ██║    ██║██║████╗  ██║╚══██╔══╝██║  ██║██╔════╝██╔══██╗    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔══██╗██╔════╝ ██╔════╝
    ██║ █╗ ██║██║██╔██╗ ██║   ██║   ███████║█████╗  ██████╔╝    ███████╗   ██║   ██║   ██║██████╔╝███████║██║  ███╗█████╗  
    ██║███╗██║██║██║╚██╗██║   ██║   ██╔══██║██╔══╝  ██╔══██╗    ╚════██║   ██║   ██║   ██║██╔══██╗██╔══██║██║   ██║██╔══╝  
    ╚███╔███╔╝██║██║ ╚████║   ██║   ██║  ██║███████╗██║  ██║    ███████║   ██║   ╚██████╔╝██║  ██║██║  ██║╚██████╔╝███████╗
    ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
      Made by vapen_hem#1161 | https://github.com/vapen-hem
      Banner inspired by Ori#6338 | @therealOri_ | https://github.com/therealOri
    """
    print(termcolor.colored(banner, "magenta"))

    print(
        "database - opens the database interface.\n"
        "password - opens the password interface.\n"
        "help - displays this help message.\n"
        "encryption - opens the encryption interface.\n"
        "exit - exits the program."
    )


def main():
    os.system("color")
    clear()

    display_help()

    command = input("Enter your command of choice.\n")
    args = command.split(" ")

    if args[0] == "database":

        def print_database():
            print(
                "set - sets a value in the database. | set [key] [value]\n"
                "get - gets a value from the database. | get [key]\n"
                "delete - deletes a value from the database. | delete [key]\n"
                "list - lists all keys in the database. | list\n"
                "help - displays this help message.\n"
                "exit - exits the program.\n"
                "create - creates a new database. | create [name]\n"
                "open - opens a database. | open [name]\n"
                "close - closes the current database. | close\n"
            )

        print_database()
        choice = input("Enter your choice: ")
        args = choice.split(" ")
        if args[0] == "set":
            if database == None:
                print("You must open a database first.")

            else:
                with open(f"storage/{database}.json", "w") as f:
                    database = json.load(f)

                    database[args[1]] = args[2]
                    # dump database
                    json.dump(database, f)

        elif args[0] == "delete":
            if database == None:
                print("You must open a database first.")

            else:
                with open(f"storage/{database}.json", "w") as f:
                    database = json.load(f)

                    del database[args[1]]
                    # dump database
                    json.dump(database, f)

        elif args[0] == "get":
            if database == None:
                print("You must open a database first.")

            else:
                with open(f"storage/{database}.json", "w") as f:
                    database = json.load(f)

                    print(database[args[1]])

        elif args[0] == "help":
            print_database()
        elif args[0] == "exit":
            print("Exiting...")

        elif args[0] == "create":
            if os.path.exists(f"/storage/{args[1]}.json"):
                print("Database already exists.")
            else:
                with open(os.path.join("storage", f"{args[1]}.json"), "w") as f:
                    f.write("{}")
                    print(f"Database {args[1]} created.")

        elif args[0] == "open":
            if os.path.exists(os.path.join("storage", f"{args[1]}.json")):
                database = args[1]
                print(f"Database {args[1]} opened.")
            else:
                print("Database does not exist.")

        elif args[0] == "clear":
            clear()

        elif args[0] == "close":
            database = None
            print("Database closed.")

        elif args[0] == "list":
            if database == None:
                print("You must open a database first.")
            else:
                with open(f"storage/{database}.json", "w") as f:
                    database = json.load(f)
                    print(database.keys())

        else:
            print("Invalid command.")

    elif args[0] == "password":

        def print_password():
            print(
                "generate - generates a password.\n"
                "pincode - generates a pincode.\n"
                "help - displays this help message.\n"
                "exit - exits the program."
            )

        print_password()

        choice = input("Enter your choice: ")
        args = choice.split(" ")

        if args[0] == "generate":
            run_password_interface()

        elif args[0] == "pincode":
            run_pincode_generation()

        elif args[0] == "help":
            print_password()

        elif args[0] == "exit":
            print("Exiting...")
        else:
            print("Invalid command.")
    elif args[0] == "encryption":

        def print_encryption():
            print(
                "generate_key - generates a new key."
                "encrypt - encrypts a file.\n"
                "decrypt - decrypts a file.\n"
                "help - displays this help message.\n"
                "exit - exits the program."
            )

        print_encryption()
        choice = input("Enter your choice: ")
        args = choice.split(" ")

        if args[0] == "generate_key":
            run_encryption_key_generator()

        elif args[0] == "encrypt":
            run_file_encrypt()

        elif args[0] == "decrypt":
            run_file_decrypt()

        elif args[0] == "help":
            print_encryption()

        elif args[0] == "exit":
            print("Exiting...")

        else:
            print("Invalid command.")

    elif args[0] == "help":
        display_help()

    elif args[0] == "exit":
        print("Exiting...")
        exit(0)

    else:
        print("Invalid command.")


if __name__ == "__main__":
    while True:
        main()
