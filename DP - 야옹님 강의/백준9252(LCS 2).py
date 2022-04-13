a = '#' + input()
b = '-' + input()
dp = [[0 for _ in range(len(b))] for _ in range(len(a))]

'''
단순히 생각해서 2개의 문자열에 뒤에 같은 문자가 들어오면 공통 부분 문자열의 개수가 1개씩 증가한다는 개념을 이용해서
DP를 구하면 쉽다
'''
# 역추적을 위한 pre배열
pre = [[[-1, -1] for _ in range(len(b))] for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            pre[i][j] = [i - 1, j - 1]
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                pre[i][j] = [i - 1, j]
            else:
                dp[i][j] = dp[i][j - 1]
                pre[i][j] = [i, j - 1]
print(dp[len(a) - 1][len(b) - 1])

x = len(a) - 1
y = len(b) - 1
ans = ''
while x != 0 and y != 0:
    if pre[x][y][0] == x - 1 and pre[x][y][1] == y - 1:
        ans += a[x]

    x, y = pre[x][y][0], pre[x][y][1]

if ans != '':
    print(ans[::-1])