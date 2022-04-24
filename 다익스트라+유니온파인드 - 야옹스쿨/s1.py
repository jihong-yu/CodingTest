import sys
from collections import deque

input = sys.stdin.readline


def bfs(s):
    global ans
    visited[s] = True
    que.append(s)
    #
    while que:
        val = que.popleft()
        for nxt in lst[val]:
            if not visited[nxt]:
                visited[nxt] = True
                que.append(nxt)

    ans += 1


N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
visited = [False for _ in range(N + 1)]
que = deque()
ans = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)

print(ans)
