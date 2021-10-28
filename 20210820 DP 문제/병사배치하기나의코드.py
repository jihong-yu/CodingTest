n = int(input())
array = list(map(int, input().split()))

result = 0
for i in range(n):
    if i != n - 1:
        if array[i] < array[i + 1]:
            result += 1
print(result)
