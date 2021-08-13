N = int(input())

count = 0

for i in range(N+1):
    for m in range(60):
        for s in range(60):
            if( i % 10 == 3 or i // 10 == 3 or m % 10 == 3 or m // 10 == 3 or s % 10 == 3 or s // 10 == 3):
                count += 1
print(count)

