N, M = map(int, input().split())
array = list(map(int, input().split()))

s = 0
e = N - 1
count = 0
sum_ = sum(array[:])
while True:

    if sum_ == M:
        count += 1

    if s == N - 1:
        break

    sum_ -= array[e]

    e -= 1

    if s > e:
        s += 1
        e = N - 1
        sum_ = sum(array[s:e + 1])
print(count)
