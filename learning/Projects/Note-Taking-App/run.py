# Note Taking App

FILE_NAME = "MyNotes.txt"


def show_menu():
    print("\nMenu:")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")


def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("Note added successfully!")


def view():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.read()

        if notes:
            print("\nYour Notes:\n")
            print(notes)
        else:
            print("No notes found")

    except Exception as e:
        print(e)


def delete():
    confirm = input("Are you sure you want to delete all notes? (yes/no): ")

    if confirm.lower() == "yes":
        with open(FILE_NAME, "w") as file:
            pass
        print("All notes have been deleted!")
    else:
        print("Deletion cancelled")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view()
    elif choice == "3":
        delete()
    elif choice == "4":
        break
    else:
        print("Invalid choice, try again.")