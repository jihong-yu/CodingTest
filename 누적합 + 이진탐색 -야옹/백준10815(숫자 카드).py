N = int(input())
card = list(map(int, input().split()))
M = int(input())
saguen = list(map(int, input().split()))

card.sort()

for i in range(M):
    s = 0
    e = N - 1
    x = saguen[i]
    ans = 0
    while s <= e:

        mid = (s + e) // 2

        if card[mid] == x:
            ans = 1
            break
        elif card[mid] < x:
            s = mid + 1
        else:
            e = mid - 1

    print(ans, end=" ")

