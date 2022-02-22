import sys

# 입력 빠르게 받기
input = sys.stdin.readline
MAX = 1000000
result = [0] * (MAX + 1)  # 누적합을 저장할 리스트
result[1] = 1  # 1의 약수의 합은 1

dp = [1] * (MAX + 1)  # 각 약수의 합들을 저장할 리스트
# 2~MAX 구간에서 각 배수들을 계속 더해준다.
for N in range(2, MAX + 1):

    j = 1  # 배수 설정
    while N * j <= MAX:  # 각 수의 약수의 합 구하기
        dp[N * j] += N  # N의 배수는 N을 무조건 약수로 가짐
        j += 1  # 배수 +1씩 해주기
    # 누적합 구하기
    result[N] = result[N - 1] + dp[N]

T = int(input())
for _ in range(T):
    N = int(input())
    print(result[N])
