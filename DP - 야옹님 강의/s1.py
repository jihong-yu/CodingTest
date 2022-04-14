'''
| 특정 비트를 킬때 사용
& 특정비트가 켜저있는지 혹은 특정 비트를 끌 때 사용 (x & (1 << 2)) != 0 or (x & ~(1 << @))
^ 특정 비트 상태를 반전시킬 때 사용
tip) x & (-x) x의 제일 오른쪽 1이 나온다.
'''


def DFS(li, cnt):
    if cnt == M:
        res.add(li)
        return
    for i in range(len(arr)):
        if visited[i] == 0:
            visited[i] = 1
            DFS(li + ' ' + str(arr[i]), cnt + 1)
            visited[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = set()

visited = [0] * N
DFS('', 0)
solution = [[] for _ in range(len(res))]
print(res)
for idx, val in enumerate(res):
    solution[idx] = list(map(int,val.split()))

solution.sort()
print(solution)