N, M = map(int, input().split())
array = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(N):

    # end를 가능한 만큼 이동시키기
    while interval_sum < M and end < N:
        interval_sum += array[end]
        end += 1

        # 부분합이 m일때 카운트 증가
    if interval_sum == M:
        count += 1

    interval_sum -= array[start]  # 위의 while내부의 조건때문에 반드시 interval >= m 상태로 while문을  빠져 나온다.

print(count)
