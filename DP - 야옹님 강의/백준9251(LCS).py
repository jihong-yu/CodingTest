a = '#' + input()
b = '#' + input()
dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

'''
단순히 생각해서 2개의 문자열에 뒤에 같은 문자가 들어오면 공통 부분 문자열의 개수가 1개씩 증가한다는 개념을 이용해서
DP를 구하면 쉽다
'''
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(a) - 1][len(b) - 1])