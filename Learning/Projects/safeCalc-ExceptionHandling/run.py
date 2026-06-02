
try:
    #code that might throw an exception 
except:
    #code to handle the exception
else:
    # executes if there is no exception.
finally:
    # always excutes ,even when has exception has occured.


try:
    num = int("Enter a number: ")
    result = 10/num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by Zero is not allowed ")
else:
    print("No Exception has occured.")
finally:
    print("Finally block executed ")


    # -------Safe Calculator -----

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        raise ZeroDivisionError("Cannot divide by Zero")
    return x/y

def menu():
    print("\n safe calc menu :")
    print("1. Add ")
    print("2. subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. EXIT ")


while True:
    menu()
    x=input("Enter x : ")
    y=input("Enter y : ")
    choice = input(" Enter choice 1-5")

    if choice =="1":
        print("Sum : ",add(x,y))
    elif choice =="2":
        print("subtract : ",sub(x,y))
    elif choice =="3":
        print("Multiply :",mul(x,y))
    elif choice =="4":
        print("Divide:", div(x,y))
    else:
        print("Invalid Choice")
        break
    

 



