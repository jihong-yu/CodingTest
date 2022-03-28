import sys

input = sys.stdin.readline

N, H = map(int, input().split())
down = [0] * (H + 1)
up = [0] * (H + 1)

for i in range(N):

    if i % 2 == 0:
        down[int(input())] += 1  # 입력받은 길이의 개수를 저장
    else:
        up[int(input())] += 1  # 입력받은 길이의 개수를 저장

dp_down = [0] * (H + 2)  # 뒤에서부터 누적합 적용을 위해 H + 2개를 만들어 준다.
dp_up = [0] * (H + 2)  # 뒤에서부터 누적합 적용을 위해 H + 2개를 만들어 준다.
for i in range(1, H + 1)[::-1]:  # 반대로 누적합을 적용
    dp_down[i] = dp_down[i + 1] + down[i]  # 뒤에서 앞으로 더해가면서 더해준다.
    dp_up[i] = dp_up[i + 1] + up[i]  # 뒤에서 앞으로 가면서 더해준다.

range_count = 0  # 해당 구간의 총 개수를 저장
min_count = 1 << 60  # 피해야 하는 장애물 개수 저장

for i in range(1, H + 1):  # 1부터 H까지 돈다.
    if min_count > dp_down[i] + dp_up[H - i + 1]:  # 저장된 값보다 피해야하는 장애물이 적다면
        min_count = dp_down[i] + dp_up[H - i + 1]  # 그 값을 저장 후
        range_count = 1  # 그 구간의 개수를 1로 지정
    elif min_count == dp_down[i] + dp_up[H - i + 1]:  # 저장된 값보다 피해야하는 장애물이 같다면
        range_count += 1  # 그 구간의 개수를 1개 추가

print(min_count, range_count)
