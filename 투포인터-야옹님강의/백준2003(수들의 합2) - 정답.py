N, M = map(int, input().split())
array = list(map(int, input().split())) + [0]  # 인덱스 오류 방지를 위해 한칸 뒤에 의미없는 0값을 추가

s = 0  # 첫번째 포인터
e = 0  # 두번째 포인터

total = array[0]  # 구간합을 저장할 변수 첫번째 값을 넣어 놓는다.
count = 0  # 횟수를 셀 변수
while e < N:  # 끝 인덱스가 N 전까지

    if total == M:  # 만약 구간 합이 M이라면
        count += 1  # 개수 1개 추가
        e += 1  # 두번째 포인터를 한칸 뒤로옮겨준다.
        total += array[e]  # 구간 합에 해당 값을 추가
    elif total < M:  # 만약 구간합이 M보다 작다면
        e += 1  # 두번째 포인터 한칸 뒤로 옮겨준다.
        total += array[e]  # 구간 합에 해당 값을 추가
    else:  # 만약 구간합이 M보다 크다면
        total -= array[s]  # 구간합에서 첫번째 포인터가 가리키는 값을 제거한 후
        s += 1  # 첫번째 포인터 한칸 뒤로 이동

print(count)
