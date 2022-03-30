import sys

input = sys.stdin.readline
N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()  # 오름차순 정렬
s = 1  # 시작 인덱스 저장
e = home[-1] - home[0]  # 끝 인덱스 저장
ans = 0


def check(mid):
    total = 0  # 설치가능한 집의 개수를 저장
    s = 0  # 비교할 첫번째 인덱스
    e = 1  # 비교할 두번째 인덱스
    while s < len(home) and e < len(home):  # 인덱스 범위를 벗어나지 않는 범위내에서

        if home[s] + mid <= home[e]:  # 만약 첫번째 home + 거리 더한 값이 두번째 집보다 작거나 같다면
            total += 1  # 설치가능한 집개수 1개를 추가해주고
            s = e  # 첫번째 인덱스를 2번째 집으로 이동해주고
            e += 1  # 두번째 인덱스를 그 다음집으로 이동해준다.
        else:  # 크다면(즉, 설치할 수 없다면)
            e += 1  # 두번째 인덱스를 그 다음집으로 이동하여 검사

    return (total + 1) >= C  # 만약 그 개수가 설치할 수 있는 공유기 개수인 C보다 많거나 같다면 True


while s <= e:

    mid = (s + e) // 2

    if check(mid):  # 만약 해당 거리로 설치가 가능하다면
        ans = mid  # 설치가능한 거리를 저장
        s = mid + 1  # 그 후 최대거리를 검사하기 위해 시작 범위를 mid + 1 해준다.
    else:  # 해당 거리로 설치가 불가능 하다면
        e = mid - 1  # 거리를 좁히기 위해 끝 범위를 줄여준다.

print(ans)
