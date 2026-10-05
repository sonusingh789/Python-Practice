
# shopping_list = ["Milk","Eggs","Bread"]

# shopping_list.append("Butter")
# shopping_list.insert(1,"Juice")

# # for items in shopping_list:
# #     print(f"- {items}")

# for index , items in enumerate(shopping_list):
#     print(f"{index+1}.{items}")



# Shopping List APP

shopping_list = []

def view():
    print(shopping_list)

def add():
    data = input("Enter item: ")
    shopping_list.append(data)

def remove():
    shopping_list.pop()

def show_menu():
    print("\n--- Shopping List Menu ---")
    print("1. View Shopping List")
    print("2. Add an Item")
    print("3. Remove an Item")
    print("4. Clear List")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        view()
    elif choice == "2":
        add()
    elif choice == "3":
        remove()
    elif choice == "4":
        shopping_list.clear()
    elif choice == "5":
        break
    else:
        print("choice not found")
        

    