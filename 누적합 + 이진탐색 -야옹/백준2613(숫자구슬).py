N, M = map(int, input().split())
array = list(map(int, input().split()))

s = max(array)  # 시작값을 최대값으로 설정(중요!!)
e = sum(array)  # 끝값을 전체합으로 설정
ans_list = []  # 그룹 합을 저장할 리스트
ans = 0  # 최소 그룹의 합을 저장


def check(mid):
    global ans_list

    temp = []  # 임시 그룹들의 구슬 개수를 저장할 리스트
    group_count = 0  # 만든 총 그룹의 개수를 저장
    need_group = M  # 필요한 그룹의 개수 저장
    i = 0  # 시작인덱스
    while i <= N - 1:  # i가 범위를 벗어나지 않을때 까지
        sum_ = 0  # 구슬의 총합
        cnt = 0  # 한 그룹내의 구슬 개수
        while i <= N - 1:  # 범위를 벗어나지 않을 때 까지

            sum_ += array[i]  # 합을 저장
            cnt += 1  # 개수를 증가

            if sum_ > mid:  # 만약 합이 이분탐색으로 구한 최솟값보다 크다면
                cnt -= 1  # 다시 1개빼주고
                sum_ -= array[i]  # 마지막에 더한 값을 빼주고
                break  # 탈출

            if need_group - group_count == N - i:  # 만약 남은 인원이 만들어야할 그룹의 개수와 같다면
                i += 1  # 남은 사람들을 (1사람 => 한그룹) 으로 만들어야 하므로 i만 증가시켜주고
                break  # 탈출

            i += 1  # 위의 2가지 조건에 걸리지 않는다면 i는 계속 증가하여 다음 구슬들 탐색

        temp.append(cnt)  # 반복문 빠져나왔다면 구한 cnt를 저장해주고
        group_count += 1  # 그룹의 개수를 1개 증가

    if M >= group_count:  # 만약 그룹카운트가 M보다 크거나 같을때만
        ans_list = temp  # result값을 정답리스트에 저장

    return M >= group_count


# 이분탐색
while s <= e:

    mid = (s + e) // 2

    if check(mid):
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)
print(*ans_list)
