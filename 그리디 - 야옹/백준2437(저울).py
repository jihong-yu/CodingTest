N = int(input())
arr = list(map(int, input().split()))

arr.sort()

sum_ = 0  # 누적합을 저장
for i in range(N):

    if arr[i] > sum_ + 1:  # 만약 해당 i번째의 값이 그전누적합 + 1 보다 크다면
        print(sum_ + 1)  # 누적합 + 1 을 출력후 종료
        exit()
    sum_ += arr[i]  # 그렇지 않으면 계속 누적합을 구해준다.

print(sum_ + 1)  # 위의 if에 걸리지 않았다면 모두 더한 값 + 1이 정답
