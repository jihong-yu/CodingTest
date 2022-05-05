N = int(input())

trees = list(zip(map(int, input().split()), map(int, input().split())))

trees.sort(key=lambda x: (x[1], x[0]))  # 1. 성장하는 길이만큼, 2. 초기 나무길이 만큼 오름차순 정리

ans = 0
for i in range(N):
    ans += (trees[i][0] + (i * trees[i][1])) # 초기 나무길이 + (성장한 날짜 * 성장하는 길이)

print(ans)
