def dfs(depth, num):
    global flag
    if flag:
        return

    if depth > 1:
        if not operator_dic[oprator[depth - 2]](int(num[-2]), int(num[-1])):
            return
        if depth == N + 1:
            print(num)
            flag = True
            return

    for i in range(10):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, num + str(i))

            visited[i] = False


def dfs_2(depth, num):
    global flag

    if flag:
        return

    if depth > 1:
        if not operator_dic[oprator[depth - 2]](int(num[-2]), int(num[-1])):
            return 0
        if depth == N + 1:
            print(num)
            flag = True
            return

    for i in range(10)[::-1]:
        if not visited[i]:
            visited[i] = True
            dfs_2(depth + 1, num + str(i))
            visited[i] = False


N = int(input())

operator_dic = {
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y
}

oprator = input().split(' ')
flag = False
visited = [False] * 10
dfs_2(0, '')
flag = False
visited = [False] * 10
dfs(0, '')
