import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union_(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[a] = b
        rank[b] += 1


N, M = map(int, input().split())  # 뉴런의 개수와 시냅스의 개수
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)
set_count = set()
cnt = 0
for _ in range(M):
    a, b = map(int, input().split())

    # 만약 두 노드가 싸이클이 형성되어 있다면 연산 횟수 1 증가
    if find(a) == find(b):
        cnt += 1
    else:  # 싸이클이 형성되어 있지 않다면 유니온 처리
        union_(a, b)

# 현재 연결되지 않은 연결요소 집합이 몇개 존재하는지 set함수를 통해 확인
for i in range(1, N + 1):
    set_count.add(find(i))

# 싸이클이 형성된 횟수 + 연결요소에 존재하는 집합의 개수 - 1을 출력
print(cnt + len(set_count) - 1)
