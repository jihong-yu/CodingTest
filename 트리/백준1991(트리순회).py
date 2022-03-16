# 전위 순회
def pre_order(v):
    if v:
        print(v, end="")
        pre_order(tree[v][0])
        pre_order(tree[v][1])


# 중위 순회
def in_order(v):
    if v:
        in_order(tree[v][0])
        print(v, end="")
        in_order(tree[v][1])


# 후위 순회
def post_order(v):
    if v:
        post_order(tree[v][0])
        post_order(tree[v][1])
        print(v, end="")


N = int(input())

tree = {}
for i in range(65, 65 + N):
    tree[chr(i)] = ['', '', '']  # 왼쪽자식,오른쪽자식,부모

for _ in range(N):
    node, left, right = map(str, input().split())
    if left.isalpha():
        tree[node][0] = left
        tree[left][2] = node
    if right.isalpha():
        tree[node][1] = right
        tree[right][2] = node

pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()
