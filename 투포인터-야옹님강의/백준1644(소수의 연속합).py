N = int(input())

# 빠른 소수 구하기 (에라토스 테네스의 체 최적화)
sosu = [True for i in range(N + 1)]
sosu[0], sosu[1] = False, False
temp_sosu = []
for i in range(2, len(sosu)):
    if not sosu[i]:
        continue

    temp_sosu.append(i)
    index = i
    while i * index < len(sosu):
        sosu[i * index] = False
        index += 1

temp_sosu += [0]  # 인덱스가 벗어나는 것을 방지하기 위해 패딩해준다.
s = 0  # 시작인덱스
e = 0  # 끝 인덱스
ans = 0
temp = temp_sosu[0]  # 첫번째 값으로 지정
while e < len(temp_sosu) - 1 and s < len(temp_sosu) - 1:  # 두 인덱스 모두 구간안에 있고

    if temp < N:  # 만약 N보다 작다면
        e += 1  # 끝 인덱스를 한칸 올려주고
        temp += temp_sosu[e]  # 새로운 값을 추가
    elif temp > N:  # 만약 N보다 크다면
        temp -= temp_sosu[s]  # 현재 시작인덱스값을 빼주고
        s += 1  # 시작인덱스를 한칸 증가
    else:  # 만약 N과 같다면
        ans += 1  # 개수 추가
        e += 1  # 끝 인덱스를 하나 추가하고
        temp += temp_sosu[e]  # 끝 인덱스 값을 하나 추가

print(ans)
