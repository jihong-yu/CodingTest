N = int(input())
word = input()
W_acc = [0] * N
E_acc = [0] * N

W_acc[0] = int(word[0] == 'W')
E_acc[-1] = int(word[-1] == 'E')

# 각각의 방향으로 W, E의 누적합 개수 구하기
idx = N - 2
for i in range(1, N):
    W_acc[i] = W_acc[i - 1] + int(word[i] == 'W')
    E_acc[idx] = E_acc[idx + 1] + int(word[idx] == 'E')
    idx -= 1

ans = 0
for i in range(N):
    # H을 만날때마다 계산해주기
    if word[i] == 'H':
        ans += (W_acc[i] * (pow(2, E_acc[i], 1000000007) - E_acc[i] - 1))

print(ans % 1000000007)
