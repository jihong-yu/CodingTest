def dfs(depth, num):
    global max_
    global min_

    if depth == N - 1:

        if min_ > num:
            min_ = num
        if max_ < num:
            max_ = num
        return

    for i in range(len(oper)):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, operation[oper[i]](num, nums[depth + 1]))
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

max_ = -1e+20
min_ = 1e+20
visited = [False] * len(oper)
dfs(0, nums[0])
print(max_)
print(min_)
