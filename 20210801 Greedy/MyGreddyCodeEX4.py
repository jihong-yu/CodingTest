n = int(input())
data = list(map(int,input().split()))
data.sort() #오름 차순 정리

count = 0 #현재 그룹의 사람수
result =0 #총 그룹의 수

for i in range(data.__len__()): # for i in data 도 가능
    count += 1 #현재 그룹에 사람수 한명 추가
    if count == data[i]: # 만약 현재 사람수가 공포심하고 같다면
        result += 1 # 총그룹의 수에 추가시키고
        count = 0 #현재 그룹의 수는 초기화
print(result)












