from collections import deque

T = int(input())


def bfs():
    global result
    # 화덕을 큐로 지정
    queue = deque()
    # 우선 N개의 피자를 화덕에 넣어준다.
    for i in range(N):
        queue.append([i, cheeze[i]])

    next = N  # 다음 들어갈 피자번호를 저장
    while queue:  # 큐가 존재한다면 계속 반복문을 돈다.
        # 해당 피자번호와 치즈양을 꺼내준다.
        pizza, c = queue.popleft()
        c //= 2  # 치즈 양을 절반으로 나눠주고
        if c != 0:  # 그 치즈양이 아직 0이아니라면
            queue.append([pizza, c])  # 그대로 다시 화덕에 넣는다
        else:  # 치즈 양이 0이라면
            if next < M:  # 만약 다음 피자번호가 범위를 벗어나지 않는다면
                queue.append([next, cheeze[next]])  # 다음 피자를 넣고
                next += 1  # 다음 피자 번호를 1개 증가
        # 만약 큐에 피자가 1개 남았다면
        if len(queue) == 1:
            result = queue.popleft()[0] + 1  # 그 값을 저장 후
            return  # 종료


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheeze = list(map(int, input().split()))  # 치즈 양 저장
    result = 0  # 결과를 출력할 피자 번호
    bfs()

    print(f'#{tc} {result}')
