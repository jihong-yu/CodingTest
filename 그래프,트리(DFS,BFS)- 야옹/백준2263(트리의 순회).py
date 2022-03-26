n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


def in_order_search(cur, end):
    print(inorder[cur], end=" ")

    index_ = -1
    for i in postorder[::-1]:
        if i in inorder[:cur]:
            postorder.remove(i)
            index_ = inorder.index(i)
            break
    if index_ != -1:
        in_order_search(index_, cur)

    index_ = -1
    for i in postorder[::-1]:
        if i in inorder[cur + 1:end]:
            postorder.remove(i)
            index_ = inorder.index(i)
            break
    if index_ != -1:
        in_order_search(index_, end)


in_order_search(inorder.index(postorder.pop()), n)  # root노드부터 탐색