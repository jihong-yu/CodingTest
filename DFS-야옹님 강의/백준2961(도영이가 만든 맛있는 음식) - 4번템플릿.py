def dfs(depth, cnt):
    global result

    # 기저
    if depth == len_:
        if cnt != 0:

            lemon = 1  # 신맛
            bad = 0  # 쓴맛
            for i in arr:  # 뽑은 신맛 쓴맛을 계산한다.
                lemon *= i[0]  # 신맛 값들을 곱해준다.
                bad += i[1]  # 쓴맛 값들을 더해준다.
            if abs(bad - lemon) < result:  # 만약 그 차가 저장된 값보다 적다면
                result = abs(bad - lemon)  # 그 차를 결과에 저장
        return

    # 재귀
    arr.append(cuisine[depth])  # 리스트에 넣어준다.
    dfs(depth + 1, cnt + 1)  # 깊이와 개수 모두 증가시켜준다.
    arr.pop()  # 방금 넣었던 것을 빼준다.
    dfs(depth + 1, cnt)  # 깊이만 증가시키고 개수는 증가시키지 않는다.


N = int(input())
cuisine = [list(map(int, input().split())) for i in range(N)]
arr = []
result = 1 << 100  # 결과값을 처음에 아주 큰 값으로 초기화

for i in range(1, N + 1):
    len_ = i
    dfs(0, 0)

print(result)
