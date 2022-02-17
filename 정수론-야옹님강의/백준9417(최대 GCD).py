# 최대 공약수 찾는 공식: 유클리드 호제법


T = int(input())

for _ in range(T):

    nums = list(map(int, input().split()))
    nums.sort()  # 유클리드 호제법을 실행하기 위해 정렬해준다.

    max_GCD = 0  # 가장 큰 최대 공약수 저장할 변수
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            a, b = nums[j], nums[i]  # a > b
            while a % b != 0:  # 유클리드 호제법 실행
                a, b = b, a % b
            if max_GCD < b:
                max_GCD = b

    print(max_GCD)
