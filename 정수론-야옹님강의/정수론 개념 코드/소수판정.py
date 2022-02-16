# 수를 하나 입력 받는다.
N = int(input())
count = 0

# 1. 일반적인 판정 : 1~N 까지 모두 돌면서 검사
for i in range(1, N + 1):

    if N % i == 0:
        count += 1

if count == 2:
    print("YES")
else:
    print("NO")

# 2 개선코드: 1 ~ (root n) 까지의 약수가 정확히 하나인지 구한다.
# 이론
# 12의 약수
# 1 2 3 4 6 12
# (1,12) (2,6) (3,4) 의 순서쌍을 볼 수 있다.
# 왼쪽 <= sqrt(오른쪽) 이하임을 알 수 있다.
# 즉, 어차피 1,2,3 까지만 검사하면 자동적으로 4 6 12도 검사가 된다는 뜻.

count = 0
for i in range(1, N + 1):
    if N == 1 or i * i > N:
        break
    if N % i == 0:
        count += 1

if count == 1:
    print("YES")
else:
    print("NO")


