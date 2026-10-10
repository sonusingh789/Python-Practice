import heapq

h = []

# 1.insert an element

heapq.heappush(h, 30)
heapq.heappush(h, 10)
heapq.heappush(h, 20)

print(h)  # [10 30 20]

# 2 view the smallest element
print(h[0])

# 3 remove and return the smallest element.
print(heapq.heappop(h))

# 4 size/length
print(len(h))

# 5 check is empty.
print(not h)

# 6 clear
h.clear()


# ------------------
# Max-heap


h = []

# Insert elements as negative values
heapq.heappush(h, -10)
heapq.heappush(h, -30)
heapq.heappush(h, -20)

# Peek at the maximum
print(-h[0])  # 30

# Poll/remove the maximum
print(-heapq.heappop(h))  # 30
print(-heapq.heappop(h))  # 20
print(-heapq.heappop(h))  # 10
