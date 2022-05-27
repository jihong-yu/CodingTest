N, K, M = map(int, input().split())


def eratosThenes(N):
    for i in range(2, N + 1):
        if i * i <= N:
            if not sieve[i]:
                for j in range(i + i, N + 1, i):
                    sieve[j] = True


def calculatePrime(N, K):
    for i in range(2, N + 1):
        if not sieve[i]:
            factor = i
            while factor <= N:
                numberOfPrime[i] += (N // factor) - (K // factor) - ((N - K) // factor)
                factor *= i


sieve = [0] * 4000001
numberOfPrime = [0] * 4000001
eratosThenes(N)
calculatePrime(N, K)

ans = 1
for i in range(2, N + 1):
    for j in range(numberOfPrime[i]):
        ans *= i
        ans %= M

print(ans)
