N=int(input())          # 발전기의 개수
cost=[list(map(int, input().split())) for _ in range(N)]
yn=input()
P=int(input())
size=2**(N-1)
dp=[[-1]*(1<<N) for _ in range(N)]
init=float('inf')
cnt=0
pNum=0

for i in range(N) : # 켜진 발전기 개수 세기
    if yn[i] == 'Y' :
        cnt+=1
        pNum |= (1<<i)      # 추가

def dfs(cnt, pNum) :
    if cnt >= P :
        return 0
    if dp[cnt][pNum] != -1 : return dp[cnt][pNum]

    dp[cnt][pNum]=init

    for i in range(N) :
        if pNum & (1<<i) == (1<<i) :    # 포함?
            for j in range(N) :
                if i == j or pNum & (1<<j) == (1<<j):
                    continue
                dp[cnt][pNum]=min(dp[cnt][pNum], dfs(cnt+1, pNum|(1<<j))+cost[i][j])

    return dp[cnt][pNum]

ans=dfs(cnt, pNum)
if ans == init :
    print(-1)
else :
    print(ans)