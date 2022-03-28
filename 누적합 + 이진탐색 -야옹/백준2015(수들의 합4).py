N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))  # 입력받은 수들을 저장

prefix = [0]  # 누적합을 저장할 리스트

for i in range(1, N + 1):
    prefix.append(prefix[i - 1] + arr[i])

# 만약 모든 값들이 양수이고(누적합이 계속해서 증가) K의 값이 적당할 때는 리스트를 만들어 다음과같이 사용
# cnt = [0 for _ in range(100010)]  # 값의 개수를 저장할 리스트
# ans = 0
# for i in range(1, N + 1):
#     ans += cnt[prefix[i] - K]
#
#     cnt[prefix[i]] += 1
#
# print(ans)

# 만약 음수가 존재하고 K의 값이 아주 큰값일 때는 딕셔너리를 만들어 사용
cnt = {}
ans = 0
for i in range(N + 1):
    ans += cnt.get(prefix[i] - K, 0)

    cnt[prefix[i]] = cnt.get(prefix[i], 0) + 1

print(ans)
