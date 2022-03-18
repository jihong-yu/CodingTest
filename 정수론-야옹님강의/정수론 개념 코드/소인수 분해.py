# 1. 완탐으로 하는 방법

N = int(input())

result = N
for i in range(2, N + 1):
    while result % i == 0:
        print(i, end=" ")
        result //= i
print()
# 2. sqrt 활용하기
# n => a, b, c, d, e, f, g, h , i
# a*b*c*d*e*f*g*h*i => n

# 이 때 소인수가 sqrt N 보다 큰 경우는 많아봐야 1개이거나 거의 없다.

X = N  # N이 불변해야 i*i > N 이성립

for i in range(2, N + 1):
    if i * i > N:
        break

    while X % i == 0:
        print(i, end=" ")
        X //= i
if X != 1:
    print(X)
