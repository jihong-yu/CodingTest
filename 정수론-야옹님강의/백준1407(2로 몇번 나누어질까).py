#잘몰라서 구글링함

a, b = map(int, input().split())


def func(num):
    cnt = num
    i = 2
    # 범위에서 2^k의 배수의 개수를 sum
    while i <= num:
        cnt += (num//i)*(i//2)
        i *= 2
    return cnt


print(func(b)-func(a-1))