data = input() # 문자열데이터입력

result = int(data[0]) # 첫 번째 문자를 인트형으로 대입

for i in range(1,len(data)): 
    #두수모두 1보다 클 경우 곱하기수행
    if int(data[i]) > 1 and int(data[i-1]) > 1:
        # int(data[i]) <= 1 or int(data[i=1] <= 0)
        result *= int(data[i])
    else:
        result += int(data[i])
print(result)


