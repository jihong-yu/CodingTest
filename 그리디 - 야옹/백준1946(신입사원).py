import sys

input = sys.stdin.readline
T = int(input())

for tc in range(T):
    N = int(input())
    freshman = [list(map(int, input().split())) + [i + 1] for i in range(N)]

    freshman.sort(key=lambda x: x[0])

    rank = freshman[0][1]  # 첫 비교대상 면접점수를 저장
    cnt = 1  # 개수를 1로 초기화

    for i in range(1, N):
        if rank > freshman[i][1]:  # 만약 지금 저장된 순위보다 더 작은 순위가 나왔다면
            rank = freshman[i][1]  # 그 순위를 저장하고
            cnt += 1  # 개수 1개 추가

    print(cnt)
