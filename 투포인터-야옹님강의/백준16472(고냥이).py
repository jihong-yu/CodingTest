alpha = [0] * 26

N = int(input())
word = input() + 'z'  # 문자열의 범위를 벗어나지 않게 하기 위해 아무 문자로 패딩

s = 0  # 시작인덱스
e = 0  # 끝인덱스
ans = 0  # 최대 개수
type_cnt = 1  # 문자 종류의 총 개수
cur_len = 1  # 현재 문자열의 길이
alpha[ord(word[0]) - ord('a')] += 1  # 알파의 개수를 1개 추가

while s < len(word) - 1 and e < len(word) - 1:

    if type_cnt <= N:  # 만약 문자종류가 N보다 작거나 같다면
        if ans < cur_len:  # 문자의 종류가 N보다 작아도 정답이 될 수 있으므로 최대값으로 갱신해주고
            ans = cur_len
        e += 1  # 범위를 한칸 늘려준다.
        if not alpha[ord(word[e]) - ord('a')]:  # 만약 새로운 문자의 종류가 추가된다면
            type_cnt += 1  # 종류를 1개 늘려주고
        alpha[ord(word[e]) - ord('a')] += 1  # 해당 알파벳의 개수를 1개 추가
        cur_len += 1  # 전체 문자열의 길이도 1 증가

    elif type_cnt > N:  # 만약 문자종류가 N보다 크다면
        alpha[ord(word[s]) - ord('a')] -= 1  # 개수를 줄여주어야 하기 떄문에 맨앞의 문자 한개를 빼준다.
        if not alpha[ord(word[s]) - ord('a')]:  # 만약 개수가 0이라면 문자 종류가 1개 줄어든 것이기 때문에
            type_cnt -= 1  # 문자 종류를 -1 개 해준다.
        s += 1  # 그후 맨앞 인덱스를 1개 증가시킨 후
        cur_len -= 1  # 전체 길이를 한개 줄여준다.

print(ans)
