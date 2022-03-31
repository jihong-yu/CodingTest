# N이 100일 때
# 1 2 3 1단
# 2 4 6 2단
# 3 6 9 3단
# ...
# 100 200 300 10000 N단

# 7보다 작은 수가 몇개 있냐
# 1 2 3 4 5 6 7 8 9
# 1 3 5 6 6 8 8 8 9 ...
# x x x x x o o o o ... 해당 수의 가장작은 숫자 찾기

# 100 * 100 mid = 140 일때
# 1 2 3 4 5 6 ... 100 100개
# 2 4 6 8 10 .... 200 70개
# 3 6 9 12 15 ....300 46개
# ...
# 100 200 300 .. 100 #1개
# 즉 (찾고자하는 값 // i단) 개를 가진다.(단, 해당 단의 전체개수를 넘을 경우 해당 단의 전체개수로 설정)

N = int(input())
K = int(input())

s = 1
e = min(10 ** 9, N * N)
ans = 0


def check(mid):
    total = 0
    for i in range(1, N + 1):
        total += min(N, mid // i)

    return K <= total


while s <= e:

    mid = (s + e) // 2
    if check(mid):
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)
