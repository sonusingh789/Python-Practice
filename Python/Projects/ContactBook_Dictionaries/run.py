my_dict ={
    "key1": "value1",
    "key2":"value2",
    "key3":"value3",
}

contact = {
    "name" : "John Doe",
    "phone" : "123-456-789",
    "email":"john@example.com"
}

#acess
#method 1
print(contact["name"])
#method 2
print(contact.get("name"))

#update
contact["name"]="Sonu Singh"
print(contact.get("name"))

#remove 
del contact['email']
print(contact)

for key ,value in contact.items():
    print(key,value)

if 'email' in contact:
    print("email found!")
else:
    print("email not found")


    #----------------contact Book Project---------------------------------

contactDetails = {}


def show_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")


def add():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")

    contactDetails[name] = {
        "phone": phone,
        "address": address
    }

    print("Contact Added Successfully!")


def view():
    if not contactDetails:
        print("No contacts found.")
        return

    for name, details in contactDetails.items():
        print(f"\nName: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Address: {details['address']}")


def search():
    name = input("Enter name to search: ")

    if name in contactDetails:
        print("\nContact Found!")
        print(f"Phone: {contactDetails[name]['phone']}")
        print(f"Address: {contactDetails[name]['address']}")
    else:
        print("Contact not found.")


def edit():
    name = input("Enter contact name to edit: ")

    if name in contactDetails:
        phone = input("Enter new phone number: ")
        address = input("Enter new address: ")

        contactDetails[name]["phone"] = phone
        contactDetails[name]["address"] = address

        print("Contact Updated Successfully!")
    else:
        print("Contact not found.")


def delete():
    name = input("Enter contact name to delete: ")

    if name in contactDetails:
        del contactDetails[name]
        print("Contact Deleted Successfully!")
    else:
        print("Contact not found.")


while True:
    show_menu()

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add()

    elif choice == "2":
        view()

    elif choice == "3":
        search()

    elif choice == "4":
        edit()

    elif choice == "5":
        delete()

    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid Choice!")