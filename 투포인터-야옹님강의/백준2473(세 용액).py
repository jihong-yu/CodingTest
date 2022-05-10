N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = []  # i,s,e 순서
min_ = 1 << 40
for i in range(N - 2):
    # 출발점을 i + 1, 끝점을 N - 1로 잡는다.
    s, e = i + 1, N - 1

    while s < e:
        sum_ = arr[i] + arr[s] + arr[e]

        if abs(sum_) < abs(min_):
            min_ = sum_
            ans = [arr[i], arr[s], arr[e]]

        if sum_ < 0:
            s += 1
        elif sum_ > 0:
            e -= 1
        else:
            print(*sorted(ans))
            exit()

print(*sorted(ans))
