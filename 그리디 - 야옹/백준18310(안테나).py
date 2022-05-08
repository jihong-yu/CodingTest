N = int(input())
house = list(map(int, input().split()))

house.sort()

mid = N // 2
if not N % 2:
    mid -= 1
print(house[mid])
