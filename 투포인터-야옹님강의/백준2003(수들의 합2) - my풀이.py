N, M = map(int, input().split())
array = list(map(int, input().split()))

s = 0
e = N - 1
count = 0
sum_ = sum(array[:])
temp_sum = sum_
while True:

    if sum_ == M:
        count += 1

    if s == N - 1:
        break

    sum_ -= array[e]
    e -= 1

    if s > e:
        sum_ = temp_sum - array[s]
        temp_sum = sum_
        s += 1
        e = N - 1

print(count)
