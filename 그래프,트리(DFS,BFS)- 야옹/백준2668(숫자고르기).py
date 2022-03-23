N = int(input())
graph = [[] for _ in range(N + 1)]
count = 0  # 결과를 출력할 개수
result = []  # 집합을 저장할 리스트
visited = [False] * (N + 1)  # 방문처리
for i in range(N):
    a = int(input())
    if i + 1 == a:  # 만약 이미 카드가 같다면 해당 카드를 바로 뽑으면 되므로
        count += 1  # 개수를 1증가한 후
        result.append(a)  # 해당 카드를 저장
        visited[a] = True  # 방문처리

    graph[i + 1].append(a)  # i+1 -> a 로 그래프를 등록해준다.


def dfs(v, start, cnt):
    global count

    if cnt != 0 and v == start:  # 만약 뽑은개수가 0이 아니고 출발점과 같다면
        count += cnt  # 개수를 1증가
        for x in temp:  # 저장된 집합을 돌면서
            result.append(x)  # 집합의 원소를 저장해 준다.
        return True  # 그 후 True저장

    for i in graph[v]:  # 해당 그래프와 연결된 카드를 돌면서
        if not visited[i]:  # 만약 방문하지 않았다면
            visited[i] = True  # 해당 카드 방문처리
            temp.append(i)  # 해당 카드 저장
            if not dfs(i, start, cnt + 1):  # 만약 False를 반환했다면(집합이 사이클을 돌지 않는다면)
                visited[i] = False  # 다시 방문처리 해제
            else:  # 만약 True라면(싸이클을 돈다면)
                return True  # 계속해서 True반환
    return False


for i in range(1, N):
    if not visited[i]:  # 만약 방문하지 않았다면 dfs를 돈다.
        temp = []  # 싸이클을 형성하는 집합의 원소를 담을 temp리스트 선언
        dfs(i, i, 0)  # dfs를 돈다.

result.sort()  # 오름차순정렬 후 출력

print(count)
for i in result:
    print(i)
