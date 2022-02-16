# 목표 : 두 자연수 a, b 가 주어질 때 이 둘의 최대 공약수를 구한다. (log n)
# a < b일 때 a와 b-a를 남기는 작업을 반복하면된다.
# 결국 반복하고 남은것이 a % b와 같다 단, 1이 나오는 경우를 위해서 계속 반복문을 돌아줘야함

# 1. 최대 공약수를 구하는 법(gcd)

a, b = map(int, input().split())  # a > b 라고 하자

c, d = a, b

while a % b != 0:
    a, b = b, a % b

print(b)

# 2. 최소 공배수 구하는 법(LCM) 유클리드 호제법 응용
A, B = c, d
while c % d != 0:
    c, d = d, c % d

print(A * B // d)
