N = int(input())
vote = list(int(input()) for _ in range(N))
result = 0
while True:
    # 만약 최댓값의 개수가 1이고 그 최댓값의 인덱스가 0이라면 탈출
    if vote.count(max(vote)) == 1 and vote.index(max(vote)) == 0:
        break
    else:  # 만약 최댓값의 개수가 2이상이라면 매수시작
        vote[vote.index(max(vote), 1)] -= 1  # 2번째 수부터 끝까지 중에서 최댓값 중 -1 해준다.
        # (만약 index인자에 1을 안주면 최댓값이 다솜이를 포함해서 동일하게 10일 경우에 다솜이의 인덱스가 젤 빠르기 때문에 다솜이의 표를 -1 해버린다.)
        vote[0] += 1  # 다솜이의 투표수를 1개 추가
        result += 1  # 매수한 사람 1명 추가.

print(result)
