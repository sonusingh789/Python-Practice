# --------------------------
##  STACK
# --------------------------

st = []

# 1 . Push , Add element to top.
st.append(10)
st.append(20)
st.append(30)

# 2 . pop , remove and return top element.
st.pop()  # it removes as well as retuns removed element.

# 3 . peek , get top element without removing it.
st[-1]  # returns last or top element.

# 4 check if the stack is empty.
print(not st)  # True/False

# 5 size/length of stack.
len(st)

# clear
st.clear()
