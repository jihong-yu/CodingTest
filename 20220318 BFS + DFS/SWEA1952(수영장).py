import sys

sys.stdin = open('input.txt', 'r')


def dfs(month, cost):
    global result
    # 12월에서 3달비용을 이용하는 경우도 1달밖에 이용하지 못하지만 3달비용이 나오므로
    # 최대 15까지 month값이 정해진다.
    if 13 <= month <= 15:
        if cost < result:  # 만약 현재 저장된 값보다 값이 적다면
            result = cost  # 그 값을 현재 값으로 바꿔준다.
        return

    dfs(month + 1, cost + one_cost[month])  # 현재 비용 + 다음달 비용
    dfs(month + 3, cost + three_m)  # 현재비용 + 3달비용


T = int(input())

for tc in range(1, T + 1):
    day, m, three_m, y = map(int, input().split())

    plan = [0] + list(map(int, input().split()))
    one_cost = [0]  # 한달 단위로 최저가 구하기(일가격과 한달중 적은 가격을 구해준다.)
    for i in range(1, 13):  # 1월부터 12월 까지 돌면서
        if plan[i] * day > m:  # 만약 계획일 * 일가격 보다 한달 가격이 더싸다면
            one_cost.append(m)  # 한달가격을 적용시킨다.
        else:  # 반대라면
            one_cost.append(plan[i] * day)  # 그 값을 적용

    result = 1 << 60  # 결과를 출력할 변수
    dfs(1, 0)  # 1월부터 dfs를 돈다.(한달과 3달중 적은 가격을 구해준다.)
    if result > y:  # 만약 년가격이 더 싸다면
        result = y  # 년가격을 대입

    print(f'#{tc} {result}')
