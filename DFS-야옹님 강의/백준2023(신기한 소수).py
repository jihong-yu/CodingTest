import math


# 소수판별 함수
def check_not_prime(num):
    temp_num = ''  # 각 자리마다 소수를 계산할 변수
    for i in range(len(num)):
        count = 0  # 나눠 떨어지는 횟수를 셀 변수
        temp_num += num[i]  # 1의 자리부터 10의자리 100의 자리.. 계속 문자열로 더해준다.
        for j in range(1, int(math.sqrt(int(temp_num))) + 1):
            if int(temp_num) % j == 0:  # 만약 나누어 떨어진다면
                count += 1  # 횟수를 1 증가
            if count >= 2:  # 그 횟수가 2이상이라면 소수가 아니므로
                return True  # True로 탈출
    return False  # 소수이므로 False


def dfs(depth, num):
    if depth == 1:  # 숫자 길이가 1일때
        if num in ['0', '1', '4', '6', '8', '9']:  # 첫째자리가 소수가 아니라면
            return  # 탈출
        if N == 1:  # 만약 1이라면
            print(num)  # num 출력 후
            return  # 탈출
    elif N >= depth >= 2:  # 숫자 길이가 2이상이고 N이하 일때
        if int(num[-1]) % 2 == 0:  # 만약 끝자리가 짝수이면 탈출
            return
        if check_not_prime(num):  # 소수 판별
            return
        if depth == N:  # 만약 N까지 왔다면
            print(num)  # num출력 후
            return  # 탈출

    for i in range(0, 9 + 1):
        dfs(depth + 1, num + str(i))


N = int(input())
dfs(0, '')
