def dfs(depth):
    global time_
    global min_

    if depth == N - 1:
        temp = 0
        start = nums[0]
        for j in range(N - 1):
            temp = operation[arr[j]](start, nums[j + 1])
            start = temp

        if min_ > temp:
            min_ = temp
        if max_ < temp:
            max_ = temp
        return

    for i in range(len(oper)):
        if not visited[i]:
            visited[i] = True
            arr.append(oper[i])
            dfs(depth + 1)
            arr.pop()
            visited[i] = False


operation = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'x': lambda x, y: x * y,
    '%': lambda x, y: x // y if x > 0 else -(abs(x) // y),

}
N = int(input())
arr = []
nums = list(map(int, input().split()))
temp = list(map(int, input().split()))
oper = []
for _ in range(temp[0]):
    oper.append('+')
for _ in range(temp[1]):
    oper.append('-')
for _ in range(temp[2]):
    oper.append('x')
for _ in range(temp[3]):
    oper.append('%')

time_ = -1e+20
min_ = 1e+20
visited = [False] * len(oper)
dfs(0)
print(time_)
print(min_)
