def dfs(depth, num):
    global exit_flag

    if exit_flag:  # 재귀 전체 종료 변수 체킹
        return

    if 1 <= depth <= N:  # 길이가 1부터 N 까지
        for j in range(len(num) - 1):  # 마지막 전 변수까지
            for k in range(1, len(num) // 2 + 1):  # 1개부터~문자열 길이의 절반까지 비교한다.
                if num[j: j + k] == num[j + k:j + 2 * k]:  # 만약 j 부터 j + k 까지와 j + k 부터 j + 2k 까지의 배열이 동일하다면
                    return  # 나쁜수열 이므로 리턴

    if depth == N:
        print(num)  # 첫 number 찾고
        exit_flag = True  # 바로탈출 변수 True
        return  # 재귀 전체 종료

    for i in range(1, 3 + 1):
        dfs(depth + 1, num + str(i))


N = int(input())
exit_flag = False

dfs(0, '')
