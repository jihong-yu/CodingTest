N, result = map(int, input().split())

count = 0
X = result
while X <= N:
    count += N // X
    X *= result
print(count)
