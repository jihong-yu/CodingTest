N, X = map(int, input().split())

array = list(map(int, input().split()))

array.sort()  # 투포인터 찾기위한 정렬
count = 0  # 개수를 셀 변수
count += array.count(X)  # 이미 X인것은 교체할 필요가 없으므로
for i in range(count):  # 그 개수 만큼
    array.pop()  # 리스트에서 빼준다.

s = 0  # 투포인터 시작인덱스
e = N - 1 - count  # 투포인터 끝인덱스(위에서 인덱스의 범위가 줄었으므로)
rest_count = N - count  # 남은 병 개수
while s < e:

    # 만약 두개의 병이 절반 이상이라면 2개의 병으로도 한개의 꽉찬 병을 만들 수 있으므로
    if array[s] + array[e] >= X / 2:
        count += 1  # 해당 병 2개를 꽉찬 용기로 교체한다.
        rest_count -= 2  # 병을 2개씩 빼준다.
        e -= 1  # 끝 인덱스를 한칸 앞으로 땡긴다.
        s += 1  # 시작 인덱스를 뒤로 한칸 민다.
    else:  # 만약 교환할 수 있는 양보다 적다면
        s += 1  # 시작 인덱스를 한칸 뒤로 민다.

print(count + rest_count // 3)  # 구한 개수와 남은 개수에서 3개씩 뽑아서 더해서 가면 된다.
