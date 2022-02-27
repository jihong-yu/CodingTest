def dfs(depth, num):
    global count
    global check

    if check:
        return

    if len(num) > n:
        return

    if depth > 0:
        temp = 0
        for i in num:
            temp += int(i)
        if temp == n:
            count += 1

        if count == k:
            print('+'.join(num))
            check = True
            return

    for i in range(1, 3 + 1):
        dfs(depth + 1, num + str(i))


n, k = map(int, input().split())
count = 0
check = False
dfs(0, '')
if not check:
    print(-1)
