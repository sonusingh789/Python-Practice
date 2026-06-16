
def using_list():
    tasks = []
    status = []

    def create_task():
        name = input("Enter Name of TASK: ")
        tasks.append(name)
        status.append(0)
        print("Task Added Successfully")

    def update_status():
        task_name = input("Enter Name of your task: ")

        if task_name in tasks:
            index = tasks.index(task_name)

            response = input("Is it completed? YES or NO: ").strip().lower()

            if response == "yes":
                status[index] = 1
            elif response == "no":
                status[index] = 0
            else:
                print("Invalid Response")
        else:
            print("Task Not Found")

    def delete_task():
        task_name = input("Enter Name of your task: ")

        if task_name in tasks:
            index = tasks.index(task_name)
            tasks.pop(index)
            status.pop(index)
            print("Task Deleted Successfully")
        else:
            print("Task Not Found")

    def view_task():
        print("\nTask List:")
        for index, task in enumerate(tasks):
            status_code = status[index]
            track = "Completed" if status_code == 1 else "Not Completed"
            print(f"{index}. {task} - {track}")

    def show_menu():
        print("\n1. Create Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

    while True:
        show_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_task()
        elif choice == 2:
            update_status()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            view_task()
        elif choice == 5:
            break
        else:
            print("Invalid Choice")

def using_dict():
    tasks = {}

    def create_task():
        name = input("Enter Name of TASK: ").strip().lower()

        if name in tasks:
            print("Task already exists!")
        else:
            tasks[name] = 0
            print("Task Added Successfully")

    def update_status():
        task_name = input("Enter Name of your task: ").strip().lower()

        if task_name in tasks:
            response = input("Is it completed? YES or NO: ").strip().lower()

            if response == "yes":
                tasks[task_name] = 1
            elif response == "no":
                tasks[task_name] = 0
            else:
                print("Invalid Response")
        else:
            print("Task Not Found")

    def delete_task():
        task_name = input("Enter Name of your task: ").strip().lower()

        if task_name in tasks:
            del tasks[task_name]
            print("Task Deleted Successfully")
        else:
            print("Task Not Found")

    def view_task():
        print("\nTask List:")

        if not tasks:
            print("No tasks available")
            return

        for task, status in tasks.items():
            track = "Completed" if status == 1 else "Not Completed"
            print(f"{task} - {track}")

    def show_menu():
        print("\n1. Create Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

    while True:
        show_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_task()
        elif choice == 2:
            update_status()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            view_task()
        elif choice == 5:
            break
        else:
            print("Invalid Choice")

def main():
    using_dict()

if __name__ == "__main__":
    main()