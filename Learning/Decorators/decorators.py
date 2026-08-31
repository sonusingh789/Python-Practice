def greet(fx):
    def mfx(name):
        print("Hii")
        result = fx(name)
        print(result)
        print("Bye")
        return result
    return mfx


@greet
def greeting(name: int):
    return f"My Name is {name}."
greeting("Sonu")

    # Hii
    # My Name is Sonu.
    # Bye
# ------------------------------------------

def decrease(fx):
    def mfx(number):
        result = fx(number)
        return result - 1
    return mfx


@decrease
def nums(number: int):
    return number

print(nums(5)) # 4
