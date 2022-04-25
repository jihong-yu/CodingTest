def find(x):
    # 자기 자신이 아니라면
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union_(a, b):
    a = find(a)
    b = find(b)

    # 만약 부모가 같다면 리턴
    if a == b:
        return

    if rank[a] > rank[b]:  # 만약 랭크 a가 더 깊다면
        parent[b] = a  # b의 부모를 a로
    elif rank[b] > rank[a]:  # 만약 랭크 b가 더 깊다면
        parent[a] = b  # a의 부모를 b로
    else:  # 랭크가 동일하다면
        parent[a] = b  # a의 부모를 b로 해주고
        rank[b] += 1  # b의 랭크 1 증가


V, E = map(int, input().split())
parent = [i for i in range(V + 1)]  # 부모를 자기 자신으로 설정
rank = [0 for _ in range(V + 1)]  # 랭크 설정

for _ in range(E):
    a, b = map(int, input().split())
    union_(a, b)

print(parent)
print(rank)