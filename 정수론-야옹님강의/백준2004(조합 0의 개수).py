# 5의 승수 구하기
def five_power_n(N):
    count_5_1 = 0
    X = 5
    while X <= N:
        count_5_1 += N // X
        X *= 5
    return count_5_1


# 2의 승수 구하기
def tow_power_n(N):
    count_2_1 = 0
    X = 2
    while X <= N:
        count_2_1 += N // X
        X *= 2
    return count_2_1


N, M = map(int, input().split())

# 각각의 승수 구하기( n!/m!*(n-m)! ) 이기 때문에 승수 나누기는 빼기와 같다.
count_5 = five_power_n(N) - five_power_n(N - M) - five_power_n(M)
count_2 = tow_power_n(N) - tow_power_n(N - M) - tow_power_n(M)

print(min(count_5, count_2)) #2와 5의 짝 개수 찾기
