N = int(input())
card = list(map(int, input().split()))
M = int(input())
saguen = list(map(int, input().split()))

card.sort()

for i in range(M):

    s = 0
    e = N - 1
    ans_1 = -1
    # 시작부분 찾기
    while s <= e:

        mid = (s + e) // 2

        if card[mid] == saguen[i]:
            ans_1 = mid
            e = mid - 1
        elif card[mid] > saguen[i]:
            e = mid - 1
        else:
            s = mid + 1

    s = 0
    e = N - 1
    ans_2 = -1
    # 끝부분 찾기
    while s <= e:

        mid = (s + e) // 2

        if card[mid] == saguen[i]:
            ans_2 = mid
            s = mid + 1
        elif card[mid] > saguen[i]:
            e = mid - 1
        else:
            s = mid + 1

    if ans_1 == -1 and ans_2 == -1:  # 둘다 -1이라면(즉 해당 수가 없다면)
        print(0, end=" ")
    else:
        print(ans_2 - ans_1 + 1, end=" ")
