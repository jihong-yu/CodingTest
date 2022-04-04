# 입력받은 해당 진수의 값을 10진수로 변환
def convert(num, b):
    return int(num, base=b)


# 각 자리수를 바꿔 검사해보는 함수
def check(bit, b, order):
    temp_bit = list(bit)

    for i in range(len(bit)):
        init = temp_bit[i]
        for j in range(b):
            if temp_bit[i] == str(j):
                for k in range(b):
                    if str(j) == str(k):
                        continue
                    temp_bit[i] = str(k)
                    result[order].add(convert(''.join(temp_bit), b))
        temp_bit[i] = init


T = int(input())

for tc in range(1, T + 1):
    bit = input()  # 2진수 입력
    three_bit = input()  # 3진수 입력
    result = [set(), set()]  # 각진수의 자리수를 바꿔보며 10진수를 저장할 set 2개를 리스트에 저장
    check(bit, 2, 0)  # 2진수 변환
    check(three_bit, 3, 1)  # 3진수 변환

    print(f'#{tc}', *result[0] & result[1])  # 두개의 교집합을 출력
