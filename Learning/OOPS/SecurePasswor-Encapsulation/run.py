class User:
    def __init__(self,username,password):
        self.username = username
        self.__password=password
        # privat _ _  two underscores / only parent can access
        # protected _ single underscores  the subclass can access it.

    
    def get_password(self):
        return "*****"
    
    def set_password(self,new_password):
        if len(new_password)>=8:
            self.__password = new_password
            print("password updated sucessfully")
        else:
            print("Password must be at least 8 characters")
    
user = User("Rohan","Secure123")
print(user.username)
print(user.get_password())
user.set_password("New Password")


class Account:
    def __init__(self,balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def get_balance(self):
        return self.__balance

    def set_balance(self,new_balance):
        if new_balance>=0:
            self.__balance = new_balance
            print("Balance updated sucessfully")
        else:
            print("Invalid balance !")

account = Account(1000)
print(account.get_balance())
account.set_balance(1500)
print(account.get_balance())


class User:
    def __init__(self,username):
        self.__username = username
        self.__password = None

    def set_password(self,password):
        if len(password)<6:
            print("Password must be at least 6 characters long ")
        else:
            self.__password = password
            print("Password set sucessfully")
    def get_password(self):
        return self.__password
 
user =User("Alice")
user.set_password("Password123")
print(user.get_password())




#---------------The Secure User Profile App -----------------????


class UserProfile:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = None
        self.set_password(password)

    def get_email(self):
        return self._email

    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self._email = new_email
            print("Email updated successfully")
        else:
            print("Invalid email format")

    def set_password(self, new_password):
        if len(new_password) < 6:
            print("Password must be at least 6 characters long")
        else:
            self.__password = new_password
            print("Password set successfully")

    def display_profile(self):
        print("\n-- User Profile --")
        print(f"Username: {self.username}")
        print(f"Email: {self._email}")
        print(f"Password: {self.__password}")


# Global user list
users = []


def create_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    user = UserProfile(username, email, password)
    users.append(user)
    print("User created successfully!")


def view_profiles():
    if not users:
        print("No users found")
    else:
        for user in users:
            user.display_profile()


def update_email():
    email = input("Enter current email to update: ")
    for user in users:
        if user.get_email() == email:
            new_email = input("Enter new email: ")
            user.set_email(new_email)
            return
    print("User not found")


# Main loop
while True:
    print("\n----- Secure User Profile App -----")
    print("1. Create User")
    print("2. View All Profiles")
    print("3. Update Email")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        create_user()
    elif choice == "2":
        view_profiles()
    elif choice == "3":
        update_email()
    elif choice == "4":
        print("Exiting the program")
        break
    else:
        print("Invalid choice. Please try again")
