# 목표 1~n 까지의 자연수 중에서 소수를 모두 출력

N = int(input())
isPrime = [True for _ in range(N + 1)]
isPrime[0], isPrime[1] = False, False
# 1. 완탐으로 하는방법
for i in range(2, N + 1):
    if not isPrime[i]:
        continue

    for j in range(2 * i, N + 1, i):
        isPrime[j] = False
print(isPrime)

# 2. 가지치기 한 방법(최종형태)
isPrime = [True for _ in range(N + 1)]
isPrime[0], isPrime[1] = False, False

for i in range(2, N + 1):
    if not isPrime[i]:
        continue

    for j in range(i * i, N + 1, i):
        isPrime[j] = False

print(isPrime)

# 3. 2 ~ n 까지의 자연수 각각의 가장 작은 소인수 출력

prime = [-1 for i in range(N + 1)]
for i in range(2, N + 1):
    if prime[i] != -1:
        continue

    prime[i] = i
    for j in range(i * i, N + 1, i):
        if prime[j] == -1:
            prime[j] = i

print(*prime[2:])
