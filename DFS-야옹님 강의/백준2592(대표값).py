count = [0] * (1000 + 1)  # 개수를 셀 1000까지의 리스트를 0으로 초기화

sum_ = 0
for _ in range(10):
    num = int(input())
    sum_ += num  # 합을 계속 더해준다.
    count[num] += 1  # 해당 num의 개수를 +1 씩 해준다.

print(sum_ // 10)  # 최대값
print(count.index(max(count)))  # 최빈값
