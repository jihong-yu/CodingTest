from collections import deque

a = [[1, 2], [3, 4]]

queue = deque()
for i in range(len(a)):
    queue.append(a[i])

print(queue)
queue2 = deque()

print(queue2)
