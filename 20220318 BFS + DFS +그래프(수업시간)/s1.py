from collections import deque

a = [[1, 2], [3, 4]]

queue = deque()
for i in range(len(a)):
    queue.append(a[i])

queue = deque([1])
print(queue)
