def dfs(depth, num):
    if depth > 1:
        if not operator_dic[oprator[depth - 2]](int(num[-2]), int(num[-1])):
            return 0
        if depth == N + 1:
            print(num)
            return 1

    for i in range(10):
        if not visited[i]:
            visited[i] = True
            if dfs(depth + 1, num + str(i)):
                return 1
            visited[i] = False


def dfs_2(depth, num):
    if depth > 1:
        if not operator_dic[oprator[depth - 2]](int(num[-2]), int(num[-1])):
            return 0
        if depth == N + 1:
            print(num)
            return 1

    for i in range(10)[::-1]:
        if not visited[i]:
            visited[i] = True
            if dfs_2(depth + 1, num + str(i)):
                return 1
            visited[i] = False


N = int(input())

operator_dic = {
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y
}

oprator = input().split(' ')
visited = [False] * 10
dfs_2(0, '')
visited = [False] * 10
dfs(0, '')
