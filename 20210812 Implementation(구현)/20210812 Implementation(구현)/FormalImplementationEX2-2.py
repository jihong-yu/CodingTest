N = int(input())

count = 0

for i in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(i)+str(m)+str(s): #i m s 를 문자로 바꿔버린다.
                count += 1
print(count)

