
def pattern1():
    for i in range(4):
        for j in range(4):
            print("*", end=" ")
        print()
def p1j(n):
    if n>3:
        return
    print("*", end=" ")
    p1j(n+1)
def p1i(n):
    if n>3:
        return
    p1j(0)
    print()
    p1i(n+1)

# * * * *
# * * * *
# * * * *
# * * * *

# pattern1() iterative
# p1i(0) recursive
#---------------------------------------------------------------------
