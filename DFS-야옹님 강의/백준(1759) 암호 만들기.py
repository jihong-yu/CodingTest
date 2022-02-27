def dfs(depth, start, password):
    if depth == L:
        vowel_count = 0  # 모음 개수 저장
        for i in password:  # 만들어진 password를 돈다
            if i in 'aeiou':  # 만약 해당 문자열에 모음이 있다면
                vowel_count += 1  # 모음 개수 +1
        if vowel_count <= 0 or vowel_count >= L - 1:  # 만약 모음개수가 0이거나, 길이-1개 이상이라면
            return  # 자음이 최소 2개 이상 있거나, 모음이 최소 1개 이상 없으므로 재귀 종료
        print(password)  # 그 외경우 password 출력하고
        return  # 재귀 종료

    for i in range(start, C):
        dfs(depth + 1, i + 1, password + pw[i])


L, C = map(int, input().split())
pw = list(input().split())

pw.sort()
dfs(0, 0, '')
