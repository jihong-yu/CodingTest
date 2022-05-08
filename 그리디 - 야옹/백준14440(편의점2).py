import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: x[0])  # x축 기준 정렬

mid_x = arr[N // 2][0]

arr.sort(key=lambda x: x[1])  # y축 기준 정렬
mid_y = arr[N // 2][1]

ans = 0

for i in range(N):
    ans += (abs(arr[i][0] - mid_x) + abs(arr[i][1] - mid_y))

print(ans)