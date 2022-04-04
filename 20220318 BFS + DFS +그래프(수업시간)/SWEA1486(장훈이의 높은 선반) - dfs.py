T = int(input())


# 조합 dfs 이용
def dfs(depth, start, height):
    global max_

    # 1개이상 N개 이하로 뽑은 경우
    if 0 < depth <= N:
        if height >= B:  # 뽑은 키의 합이 선반의 높이보다 크거나 같으면
            if height >= max_:  # 저장되어있는 최댓값보다 크거나 같다면
                return  # 재귀 종료
            max_ = height  # 작다면 해당 키를 저장
            return

        if depth == N:  # N개까지 뽑았다면 dfs종료
            return

    for i in range(start, N):
        dfs(depth + 1, i + 1, height + info[i])


for tc in range(1, T + 1):
    N, B = map(int, input().split())
    info = list(map(int, input().split()))

    max_ = 1 << 60  # B보단 크거나 같으면서 그 중 최소의 점원의 키의 합

    dfs(0, 0, 0)

    print(f'#{tc} {max_ - B}')
