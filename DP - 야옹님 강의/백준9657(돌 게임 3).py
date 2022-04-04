N = int(input())

dp = {1: 1, 2: 0, 3: 1, 4: 1}

for i in range(5, N + 1):
    if dp[i - 1] == 0 or dp[i - 3] == 0 or dp[i - 4] == 0:
        dp[i] = 1
    else:
        dp[i] = 0

if dp[N]:
    print('SK')
else:
    print('CY')

# dp에서 자주나오는 것들
'''
경우의 수를 구해라 => 무조건 DP
최대값을 구해라 => 이진탐색 or DP
누구 이기냐 => 무조건 DP

'''
