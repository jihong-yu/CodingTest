#현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

dx=list(map(int,[0,0,+1,-1])) #동 서 남 북 ,행
dy=list(map(int,[1,-1,0,0])) #동 서 남 북 ,열
count = 0



#경우의수 동동남,동동북,서서남,서서북,남남서,남남북,북북서,북북동
nx = column + dy[0] + dy[0] #동동남
ny = row + dx[2]
if(nx < 8 and ny < 8 ):
    count += 1
nx = column + dy[0] + dy[0] #동동북
ny = row + dx[3]
if(nx < 8 and ny > 0 ):
    count += 1
nx = column + dy[1] + dy[1] #서서남
ny = row + dx[2]
if(nx > 0 and ny < 8 ):
    count += 1
nx = column + dy[1] + dy[1] #서서북
ny = row + dx[3]
if(nx > 0 and ny > 0 ):
    count += 1
nx = column + dy[1] #남남서
ny = row + dx[2] + dx[2]
if(nx > 0 and ny < 8 ):
    count += 1
nx = column + dy[0]  #남남동
ny = row + dx[2] + dx[2]
if(nx < 8 and ny < 8 ):
    count += 1
nx = column + dy[1] #북북서
ny = row + dx[3] + dx[3]
if(nx > 0 and ny > 0 ):
    count += 1
nx = column + dy[0]  #북북동
ny = row + dx[3] + dx[3]
if(nx < 8 and ny > 0 ):
    count += 1

print(count)



