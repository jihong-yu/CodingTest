
N = int(input())
count = 1

i = 3
index = 0
while True:

    for j in range(1, i + 1):
        index += 1

    if index >= N:
        break

    i += 2
    count += 1

print(count)


