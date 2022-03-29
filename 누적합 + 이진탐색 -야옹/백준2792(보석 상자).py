import sys

input = sys.stdin.readline

N, M = map(int, input().split())
array = []
for _ in range(M):
    array.append(int(input()))

s = 1  # 1명부터
e = 10 ** 9  # 10^9 까지의 사람수가 존재한다.


def check(x):
    total_person = 0  # 사람수 저장

    # 현재의 질투심이 x일때의 총 사람수 계산
    for i in array:
        total_person += i // x + (i % x != 0)

    return total_person <= N  # 만약 그사람수가 N보다 적다면 True


ans = 0
while s <= e:

    mid = (s + e) // 2

    if check(mid):  # 질투심이 mid 일때 사람수가 N보다 작거나 같다면
        ans = mid  # 그 값을 질투심으로 저장 후
        e = mid - 1  # 다시 왼쪽으로 탐색
    else:  # 질투심이 mid 일때 사람수가 N보다 크다면
        s = mid + 1  # 질투심을 증가시켜서 사람수를 줄인다

print(ans)
