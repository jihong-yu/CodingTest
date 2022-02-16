N = int(input())
M = int(input())
# 파이썬 경우
pow(N, M, 100000007)  # N의 M승을 구하는데 100000007 으로 계속 나눠줌(모듈러)


# 재귀로 빠른 거듭제곱 구현
def pows(N, M):
    if M == 0:
        return 1

    ret = pows(N, M // 2)
    ret *= ret
    ret %= 100000007

    if M % 2 == 0:
        return ret
    else:
        return (ret * N) % 100000007


print(pows(N, M))
