n, k = map(int, input().split())

result = 0

while True:
    # n >= k 인지 아닌지 검사
    if n >= k:
        if n % k != 0:  # n이 k로 나누어 떨어지지 않으면 n에서 1을 뺀다.
            n -= 1
            result += 1
        if n % k == 0:  # n이 k로 나누어 떨어지면 나누어준다.
            n //= k
            result += 1
        if n == 1: break  # n==1이라면 반복문 탈출

    # n < k 인지 아닌지 검사
    else:
        if n == 1:
            break  # n==1이라면 반복문 탈출
        while True:
            n -= 1  # n이 k보다 작기 때문에 계속해서 n을 뺀다.
            result += 1
            if n == 1: break

print("result : ", result)
