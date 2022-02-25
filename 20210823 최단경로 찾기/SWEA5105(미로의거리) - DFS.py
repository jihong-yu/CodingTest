import sys

sys.stdin = open('input.txt', 'r')


def dfs(r, c, count):
    global min_

    if r < 0 or r >= N or c < 0 or c >= N or array[r][c] == 1:
        return
    # 가지치기
    if count > min_:  # 만약 횟수가 이미 저장된 최솟값보다 크다면 리턴
        return
    # 기저
    if array[r][c] == 3:
        if min_ > count:
            min_ = count
        return
    else:
        array[r][c] = 1

    # 재귀
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        dfs(nr, nc, count + 1)

    array[r][c] = 0


T = int(input())
dr = [-1, 0, 1, 0]  # 상우하좌
dc = [0, 1, 0, -1]  # 상우하좌

for order in range(1, T + 1):
    N = int(input())
    array = []
    start = (-1, -1)
    min_ = 1 << 20
    for i in range(N):
        temp = list(map(int, input()))
        for j in range(len(temp)):
            if temp[j] == 2:
                start = (i, j)
                break
        array.append(temp)
    dfs(start[0], start[1], 1)
    if min_ >= 1 << 20:
        min_ = 2
    print(f'#{order} {min_ - 2}')
