N, K, B = map(int, input().split())
signal = [1 for _ in range(N + 1)]  # 신호등 정보를 1로 받는다.
result = 0  # 고장난 신호등 개수를 저장할 변수

for i in range(B):  # 고장난 신호등 B개를 0으로 바꿔준다.
    temp = int(input())
    signal[temp] = 0
    if temp <= K:  # 초기 고장난 신호등 개수를 저장하기 위해 입력받은 신호등이 K보다 적으면
        result += 1  # 개수 한개 추가

e = K  # 끝 인덱스
s = 1  # 시작 인덱스
count = result  # 각 K개의 구간마다 개수를 저장할 변수
while True:

    if e >= N:  # e가 N과 같아지면 더이상 비교할 필요가 없으므로 탈출
        break
    # 빼야할 맨 앞 신호등이 고장난 신호등이라면 현재 고장난 개수에서 -1 빼준다.
    if not signal[s]:  # 만약 신호등이 0이라면
        count -= 1  # 개수 한개를 빼준다.

    s += 1  # 시작 인덱스 한개 추가
    e += 1  # 끝 인덱스 1개를 추가

    # 새로 넣을 신호등이 고장난 신호등이라면 1개 추가해준다.
    if not signal[e]:
        count += 1  # 개수 한개를 추가해준다.

    # 만약 저장된 값보다 작다면
    if result > count:
        result = count

print(result)
