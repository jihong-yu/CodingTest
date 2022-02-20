import math

T = int(input())


# 수 x의 약수를 찾는 함수
def prime_find(x):
    for i in range(1, int(math.sqrt(x)) + 1):

        if x % i == 0:
            prime.append(i)
            if i * i != x:
                prime.append(x // i)


# 첫번째와 두번째 약수 중에서 전체 수와의 공약수를 계산
# 만약 전체를 돈 후에 어떤 수와의 공약수가 아닌것의 개수가 1이하라면
# 해당 공약수는 전체 최대 공약수가 될 수 있다.
def check(x):
    count = 0
    for i in range(n):
        if arr[i] % x != 0:
            count += 1
    return count <= 1


for order in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    prime = []  # 약수를 담을 함수
    # 문제에서 아무리 많아야 수를 1개 제거(교체)할 수 있기 때문에
    # 오름차순 정렬했을 때 반드시 첫번째와 두번째 값중 하나의 약수중에서 최대공약수가 나온다.
    prime_find(arr[0])
    prime_find(arr[1])
    result = 0  # 최대공약수를 출력할 변수
    # 저장된 약수 중에서 전체 수와 비교하여 최대 공약수를 찾는다.
    for i in prime:
        if check(i):
            result = max(result, i)
    print(f'#{order} {result}')
