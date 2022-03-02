def check(select_chicken):
    global min_

    temp = 0  # 뽑은 M개의 치킨집과의 거리 구하기
    for i in house:  # 집들에서
        temp_dis = 1 << 60  # 해당 집에서 치킨집까지의 거리를 저장할 변수
        for j in select_chicken:  # 선택된 치킨집과의 거리를 계산
            temp_dis = min(temp_dis, abs(i[0] - j[0]) + abs(i[1] - j[1]))
        temp += temp_dis  # 그 거리를 계속 더해준다.

        if temp >= min_:  # 만약 그거리가 이미 저장된 최솟값보다 크거나 같다면
            return  # 종료

    if temp < min_:  # 만약 구한 거리가 최솟값보다 작다면
        min_ = temp  # 그 최솟값을 저장


def dfs(depth, start):
    if depth == M:  # M개를 뽑으면
        check(select_chicken)  # 선택된 치킨집들의 거리를 체크
        return  # 재귀종료

    for i in range(start, len(chicken)):
        select_chicken.append(chicken[i])
        dfs(depth + 1, i + 1)
        select_chicken.pop()


N, M = map(int, input().split())
house = []  # 집 좌표 저장
chicken = []  # 치킨집 좌표 저장
select_chicken = []  # 선택된 M개의 치킨 좌표들을 저장
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            house.append((i, j))
        elif temp[j] == 2:
            chicken.append((i, j))

min_ = 1 << 50  # 결과를 출력할 최소 거리
dfs(0, 0)
print(min_)
