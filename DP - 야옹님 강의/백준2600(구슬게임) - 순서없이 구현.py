def win(p, q):
    # 이미 계산된 적 있으면 해당 결과를 리턴
    if dp[p][q] >= 0:
        return dp[p][q]

    # p에 있는 구슬들을 우선 뺀다.
    for i in range(3):
        if b[i] <= p and not win(p - b[i], q):
            dp[p][q] = 1  # 해당 플레이어 승리 저장
            return dp[p][q]  # 승리를 리턴

    # 그 후 q에 있는 구슬들을 뺀다.
    for j in range(3):
        if b[j] <= q and not win(p, q - b[j]):
            dp[p][q] = 1  # 해당 플레이어 승리 저장
            return dp[p][q]  # 승리를 리턴

    # 구슬을 뺄 수 없다면 패배이기 때문에 해당 플레이어에 0을 대입
    dp[p][q] = 0
    return dp[p][q]  # 패배를 리턴


# dp[p][q][w] = 구슬이 한 통에는 p개, 한 통에는 q개 있을 때 이길 수 있는지.
# A의 차례는 1, B의 차례는 0
dp = [[-1 for _ in range(501)] for _ in range(501)]
b = list(map(int, input().split()))
for _ in range(5):
    k1, k2 = map(int, input().split())
    if win(k1, k2):
        print("A")
    else:
        print("B")
