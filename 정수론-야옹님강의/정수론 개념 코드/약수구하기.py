# 1. 완탐으로 하는 방법

N = int(input())
prime = []

for i in range(1, N + 1):
    if N % i == 0:
        prime.append(i)

print(*prime)

# 2. 순서쌍으로 하는방법 ( => 제곱수를 조심해야 한다. )
# 약수의 개수가 홀수 <=> 제곱수랑 필요충분조건이다(=동치다)
prime = []
for i in range(1, N + 1):
    if i * i > N:
        break
    if N % i == 0:
        prime.append(i)
        if i*i != N:
            prime.append(N // i)
prime.sort()
print(*prime)

