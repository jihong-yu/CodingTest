def uclid(a, b):
    while a % b != 0:
        a, b = b, a % b

    return b


def solution():
    gcd = arr[1] - arr[0]
    for i in range(2, N):
        gcd = uclid(gcd, arr[i] - arr[i - 1])

    result = []
    for i in range(1, gcd):
        if i * i > gcd:
            break

        if gcd % i == 0:
            result.append(i)
            if i * i != gcd:
                result.append(gcd // i)
    result.sort()
    print(*result[1:])


N = int(input())

arr = [int(input()) for _ in range(N)]
arr.sort()
solution()
