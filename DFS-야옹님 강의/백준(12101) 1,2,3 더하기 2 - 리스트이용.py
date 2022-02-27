def dfs(depth):
    global count
    global check

    if check:  # 만약 check 변수가 true라면 전체 재귀 종료
        return

    if len(arr) > n:  # 만약 뽑은 수의 개수가 n보다 크다면 종료
        return

    if depth > 0:  # 1개 이상 뽑았다면
        if sum(arr) == n:  # 그 합이 n가 같다면
            count += 1  # 개수 1개 증가

        if count == k:  # 만약 그 개수가 k랑 같다면
            print('+'.join(map(str, arr)))  # 그 값을 출력한 후
            check = True  # 전체 재귀 종료를 위해 check값을 true로 변경 후
            return  # 리턴

    for i in range(1, 3 + 1):
        arr.append(i)
        dfs(depth + 1)
        arr.pop()


n, k = map(int, input().split())
count = 0
arr = []
check = False
dfs(0)
if not check:  # 만약 k랑 같은 조건을 만나지 못했다면
    print(-1)  # -1 출력
