input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 #아스키코드를 구하여 첫번째 a의 아스키값을 찾아 빼주고 + 1 한다.
result =0

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)] #2차원 배열을 이용한 방향벡터이용
# 북북서,서서북,서서남,남남서,남남동,동동남,동동북,북북동
dx=[-2,-1,1,2,2,1,-1,-2] #각각의 방향씩 표기가능
dy=[-1,-2,-2,-1,1,2,2,1] #각각의 방향으로 표기가능


#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    #해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >=1 and next_column <= 8 and next_column >=1 and next_column <= 8:
        result += 1

# for i in range(8):
#     next_row = row + dx[i]
#     next_column = column + dy[i]
#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_column <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1
print(result)


