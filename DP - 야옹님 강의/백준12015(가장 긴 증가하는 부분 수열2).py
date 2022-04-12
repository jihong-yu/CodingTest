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

    if idx == len(v) - 1:  # 지금 고른 숫자가 가장 큰 숫자이면 마지막에 추가해준다
        v.append(arr[i])
    else:  # 가장 큰 숫자가 아니라면 (탐색한 위치 + 1) 에 해당 숫자로 바꿔준다.
        v[idx + 1] = arr[i]

print(len(v) - 1)
