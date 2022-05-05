S = int(input())

cur = 0  # 현재 값
i = 1  # 더할 값(1씩 증가)
cnt = 0  # 더한 횟수
while True:

    cur += i  # i만큼 계속 더한다
    cnt += 1  # 횟수를 1씩 증가
    if cur > S:  # 만약 S보다 크다면 한개 줄이면 되므로
        cnt -= 1  # 횟수를 1개 줄이고
        break  # 탈출
    elif cur == S:  # S와 같다면
        break  # 바로 탈출
    i += 1  # 더하는 값 1씩 증가

print(cnt)
