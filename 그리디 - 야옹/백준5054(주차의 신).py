T = int(input())

for tc in range(T):
    n = int(input())
    x = list(map(int, input().split()))

    x.sort()
    sum_ = 0
    for i in range(n - 1):
        sum_ += (x[i + 1] - x[i])

    sum_ += (x[-1] - x[0])

    print(sum_)
