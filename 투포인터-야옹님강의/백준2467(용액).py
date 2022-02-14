import sys

N = int(input())
array = list(map(int, input().split()))

s = 0
e = N - 1
r_s = 0  # 출력을 위해 최솟값 시작 인덱스를 저장할 변수
r_e = N - 1  # 출력을 위해 최솟값 끝 인덱스를
result = sys.maxsize  # 최댓값으로 설정
while s < e:

    if array[s] + array[e] == 0:  # 만약 합이 0이라면
        r_s, r_e = s, e  # 그 위치를 저장후
        break  # 탈출
    elif abs(array[s] + array[e]) < result:  # 만약 합의 절대값이 저장된 값보다 더 작다면(0에 가깝다면)
        result = abs(array[s] + array[e])  # 그 값을 저장하고
        r_s, r_e = s, e  # 그 위치도 저장

    # 위치 처리
    if array[s] + array[e] < 0:  # 만약 음수라면
        s += 1  # 시작인덱스를 한칸 뒤로 민다.
    elif array[s] + array[e] > 0:  # 만약 양수라면
        e -= 1  # 끝 인덱스를 한칸 당긴다.

print(array[r_s], array[r_e])
