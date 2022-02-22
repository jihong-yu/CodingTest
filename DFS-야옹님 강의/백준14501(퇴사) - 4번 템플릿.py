N = int(input())
consult = [list(map(int, input().split())) for _ in range(N)]


def dfs(depth, cnt):
    global result

    if cnt != 0:
        if cnt == 1:
            if arr[0][0] + arr[0][2] <= N:
                if result < arr[0][1]:
                    result = arr[0][1]
            else:
                return
        else:
            if arr[cnt - 2][0] + arr[cnt - 2][2] > arr[cnt - 1][2] or arr[cnt - 1][0] + arr[cnt - 1][2] > N:
                return
            else:
                temp = 0
                for i in arr:
                    temp += i[1]
                    if temp > result:
                        result = temp
    if depth >= N:
        return

    arr.append(consult[depth] + [depth])
    dfs(depth + 1, cnt + 1)
    arr.pop()
    dfs(depth + 1, cnt)


result = 0
arr = []
dfs(0, 0)
print(result)
