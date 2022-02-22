N = int(input())
consult = [list(map(int, input().split())) for _ in range(N)]


def dfs(depth, start):
    global result

    # 만약 깊이가 1이상 N이하라면
    if 1 <= depth <= N:
        if depth == 1:  # 1개 뽑았다면
            if temp[0][2] + temp[0][0] <= N:  # 범위를 벗어나지 않는다면
                if result < temp[0][1]:
                    result = temp[0][1]
            else:  # 범위를 벗어난다면
                return
        # 만약 먼저들어온 날짜 + 소요일이 늦게 들어온 날짜보다 크다면 오류이므로 재귀 종료
        elif temp[depth - 2][0] + temp[depth - 2][2] > temp[depth - 1][2] or temp[depth - 1][2] + \
                temp[depth - 1][
                    0] > N:
            return
        else:  # 위의 조건들을 통과했다면 최댓값을 계산해준다.
            temp_result = 0
            for i in temp:
                temp_result += i[1]
            if result < temp_result:
                result = temp_result
    elif depth > N:  # 만약 깊이가 최대 길이를 벗어난다면 재귀 종료
        return

    for i in range(start, N):
        temp.append((consult[i] + [i]))
        dfs(depth + 1, i + 1)
        temp.pop()


result = 0
temp = []
dfs(0, 0)
print(result)
