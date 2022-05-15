N = int(input())
arr = list(map(int, input().split()))

ans = [-1] * N  # 초기 정답을 -1로 설정
stack = [0]  # 첫 인덱스 0을 넣어준다.
for i in range(1, N):
    # 만약 스택의 마지막 인덱스의 arr값이 해당 비교하고자 하는 값보다 작다면
    # 그 값보다 클때까지 해당 값을 오른쪽의 큰 수로 설정해준다.
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]
    stack.append(i)  # 해당 인덱스를 무조건 스택에 넣어준다.

print(*ans)
