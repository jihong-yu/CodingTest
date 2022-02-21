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

# 백준 2961(https://www.acmicpc.net/problem/2961)
ans = 1 << 60
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


# 4번 템플릿(조합, 3번 템플릿보다 직관적, 2차원 리스트의 dfs를 위한 템플릿)
def recur4(depth, cnt, a, b):
    global ans

    if cnt == len_:  # 혹은 cnt != 0 으로 밑에서 반복문 안돌리고도 가능
        ans = min(ans, abs(a - b))
        return

    if depth == n:
        return

    recur4(depth + 1, cnt + 1, a * arr[depth][0], b * arr[depth][1])
    recur4(depth + 1, cnt, a, b)


# 1개 부터 n 개까지 뽑는다.
for i in range(1, n + 1):
    len_ = i
    recur4(0, 0, 1, 0)


# 4번 템플릿2(조합, 3번 템플릿보다 직관적, 2차원 리스트의 dfs를 위한 템플릿)
# 백준 1941(https://www.acmicpc.net/problem/1941)
def recur4_2(r, c, cnt, scnt):
    global ans

    if cnt == 7:  # 혹은 cnt != 0 으로 밑에서 반복문 안돌리고도 가능
        if scnt < 4:
            return

    if c == 5:  # 열이 이중리스트의 범위를 벗어난다면
        r += 1  # 다음 행의
        c = 0  # 첫열로 초기화
        return

    if r == 5:  # 만약 조건의 행의 범위를 벗어난다면 종료
        return

    recur4_2(r, c + 1, cnt + 1, scnt + (arr[r][c] == 'S'))
    recur4_2(r, c + 1, cnt, scnt)


# 1개 부터 n 개까지 뽑는다.
for i in range(1, n + 1):
    len_ = i
    recur4(0, 0, 1, 0)
