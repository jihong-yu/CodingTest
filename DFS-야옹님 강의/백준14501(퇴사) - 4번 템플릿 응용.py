N = int(input())
consult = [list(map(int, input().split())) for _ in range(N)]


def dfs(day, profit):
    global result

    if day == N + 1:
        result = max(result, profit)
        return
    if day > N + 1:
        return

    dfs(day + consult[day][0], profit + consult[day][1])
    dfs(day + 1, profit)


result = 0
arr = []
dfs(0, 0)
print(result)
