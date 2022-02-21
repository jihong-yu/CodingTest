# 1~3 템플릿

# 1번 템플릿 : n자리 1~m 수 출력 (순열)
n, m = map(int, input().split())
arr = []


def recur1(depth):
    if depth == n:
        print(*arr)
        return

    for i in range(1, m):
        arr.append(i)
        recur1(depth + 1)
        arr.pop()


recur1(0)

# 1번 템플릿 야옹님 코드
arr = [0] * n


def recur1_2(depth):
    if depth == n:
        print(*arr)
        return

    for i in range(1, m + 1):
        arr[depth] = i
        recur1_2(depth + 1)


recur1_2(0)

# 2번 템플릿 (중복 제거 순열)
# visited 처리
visited = [False for i in range(m + 1)]
arr = []


def recur2(depth):
    if depth == n:
        print(*arr)
        return

    for i in range(1, m + 1):
        if not visited[i]:
            arr.append(i)
            visited[i] = True
            recur2(depth + 1)
            visited[i] = False
            arr.pop()


recur2(0)

# 3번 템플릿(중복 허용하지 않으면서 n개 뽑는 경우) 조합
# start

arr = []


def recur3(depth, start):
    if depth == n:
        print(*arr)
        return

    for i in range(start, m + 1):
        arr.append(i)
        recur3(depth + 1, i + 1)
        arr.pop()


recur3(0, 1)

# 4번 템플릿(조합, 3번 템플릿보다 직관적, 2차원 dfs)
def recur4(depth,start):pass