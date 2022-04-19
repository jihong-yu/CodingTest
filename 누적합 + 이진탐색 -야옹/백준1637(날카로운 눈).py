import sys

input = sys.stdin.readline

N = int(input())

nums = []
time_ = 0
dp = {}
for _ in range(N):
    temp = list(map(int, input().split()))
    if time_ < temp[1]:
        time_ = temp[1]
    nums.append(temp)

s = 1
e = time_
ans = 0


def check(mid):

    total = 0

    for i in nums:
        temp_mid = mid

        A, C, B = i[0], i[1], i[2]

        if A > temp_mid:
            continue

        if temp_mid > C:
            temp_mid = C

        total += ((temp_mid - A) // B + 1)

    dp[mid] = total

    return (total % 2) == 1


while s <= e:

    mid = (s + e) // 2

    if check(mid):
        ans = mid
        e = mid - 1
    else:
        s = mid + 1


def count_check(mid):
    total = 0

    for i in nums:
        temp_mid = mid

        A, C, B = i[0], i[1], i[2]

        if A > temp_mid:
            continue

        if temp_mid > C:
            temp_mid = C

        total += ((temp_mid - A) // B + 1)

    return total


if ans:
    if dp.get(ans - 1, 0):
        print(ans, dp[ans] - dp[ans - 1])
    else:
        print(ans, dp[ans] - count_check(ans - 1))
else:
    print("NOTHING")
