N = int(input())

count = 0

for i in range(N+1):
    for m in range(60):
        for s in range(60):
            if(s == 3 or m == 3 or i == 3):
                count += 1
            elif(s == 13 or m == 13 or i == 13):
                count +=1
            elif(s== 23 or m == 23 or i == 23):
                count +=1
            elif (s == 43 or m == 43):
                count += 1
            elif (s == 53 or m == 53):
                count += 1
            elif ((s >= 30 and s<=39) or (m >= 30 and m<=39)):
                count += 1
print(count)
