N = int(input())
arr = list(map(int, input().split()))
v = [-100000]
for i in range(N):
    s = 0
    e = len(v) - 1
    idx = 0
    while s <= e:
        mid = (s + e) // 2

        if v[mid] < arr[i]:
            idx = mid
            s = mid + 1
        else:
            e = mid - 1

    if idx == len(v) - 1: #지금 고른 숫자가 가장 큰 숫자이면 마지막에 추가해준다
        v.append(arr[i])
    elif idx == len(v) - 2: #지금 고른 숫자가 마지막 숫자보다 작다면 그 숫자를 마지막 숫자로 처리
        v[idx + 1] = arr[i]


print(len(v) - 1)
