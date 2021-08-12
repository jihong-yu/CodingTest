n = int(input())
data = list(map(str,input().split()))

nx = 1
ny = 1

dx = [0,-1,0,1] #동,북,서,남 #R U L D
dy = [1,0,-1,0] #동,북,서,남 #R U L D

for i in range(len(data)):
    if(data[i] == "R"): #  data[i] 가 "R" 이라면
        nx += dx[0]
        ny += dy[0]
        if ny == 0 or ny == n+1: # 단,ny가 0이거나 n의크기보다 커지면
            ny -= 1 #다시 더했던 것을 빼준다.
    elif (data[i] == "U"):
        nx += dx[1]
        ny += dy[1]
        if nx == 0 or nx == n+1:
            nx += 1
    elif (data[i] == "L"):
        nx += dx[2]
        ny += dy[2]
        if ny == 0 or ny == n + 1:
            ny += 1
    elif (data[i] == "D"):
        nx += dx[3]
        ny += dy[3]
        if nx == 0 or nx == n + 1:
            nx -= 1

print(nx,ny)