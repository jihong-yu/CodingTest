N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

visit = 0
info = input()
s_cnt = 0
for i in range(len(info)):
    if info[i] == 'Y':
        visit |= (1 << i)  # 비트를 킨다.
        s_cnt += 1

P = int(input())  # 적어도 발전소가 정상이어야하는 수
dp = [-1] * (1 << N)


def dfs(visit, cnt):
    if cnt >= P:
        return 0

    if dp[visit] != -1:
        return dp[visit]

    ret = 10000000

    for i in range(N):  # 행
        if visit & (1 << i) != 0:  # 해당 발전소가 켜저있으면
            for j in range(N):  # 열
                if visit & (1 << j) != 0:  # 이미 비트가 켜져있는 경우는 발전소를 킬필요가 없으므로
                    continue

                ret = min(ret, dfs(visit | (1 << j), cnt + 1) + arr[i][j])

    dp[visit] = ret

    return dp[visit]


ans = dfs(visit, s_cnt)
if ans >= 10000000:
    print(-1)
else:
    print(ans)
