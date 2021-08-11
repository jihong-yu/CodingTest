data = input() # 문자열데이터입력

result = int(data[0]) # 첫 번째 문자를 인트형으로 대입

for i in range(1,len(data)): 
    #두수중 하나라도 0혹은 1인 경우 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)


