
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
def pattern2():
    for i in range(0,4):
        for j in range(i+1):
            print("*", end=" ")
        print()
# pattern2()
def p2j(n,count):
    if count>n:
        return
    print ("*" , end=" ")
    p2j(n,count+1)

def p2i(n):
    if n>3:
        return
    p2j(n,0)
    print()
    p2i(n+1)

# *
# * *
# * * *
# * * * *
# pattern2() iterative
# p2i(0) recursive

#----------------------------------------
def pattern3():
    for i in range(1,6):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

def p3j(n,count):
    if count>n:
        return
    print(count , end=" ")
    p3j(n,count+1)

def p3i(n):
    if n>5:
        return
    p3j(n,1)
    print()
    p3i(n+1)

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# pattern3() iterative
# p3i(1) recursive
#-------------------------------------------------------------------
def pattern4():
    for i in range(1,6):
        for j in range(1,i+1):
            print(i, end=" ")
        print()

def p4j(n,count):
    if count>n:
        return
    print(n, end=" ")
    p4j(n,count+1)

def p4i(n):
    if n>5:
        return
    p4j(n,1)
    print()
    p4i(n+1)

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# pattern4() iterative
# p4i(1) recursive
#--------------------------------------------------------------

def pattern5():
    for i in range(1,6):
        for j in range(6-i):
            print("*", end=" ")
        print()
# pattern5()

