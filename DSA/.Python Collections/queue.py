from collections import deque

dq = deque()

# 1. Add to the right

dq.append(10)
dq.append(20)
dq.append(30)


# 2. Add to the left
dq.appendleft(5)

# 3. View first element first.
dq[0]

# 4. view last element
dq[-1]

# 5. Remove first element.
dq.popleft()

# 6 . remove last Element.
dq.pop()

# check if queue is empty.
print(not dq)

# length of queue
len(dq)
