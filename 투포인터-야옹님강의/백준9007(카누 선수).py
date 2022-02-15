T = int(input())

for _ in range(T):
    k, n = map(int, input().split())
    weights = [list(map(int, input().split())) for _ in range(4)]

    new_arr1 = []
    new_arr2 = []

    # 각각의 카누 선수 정보 4개중 두개씩 조합하여 합을 새로운 리스트에 담는다.
    for i in range(n):
        for j in range(n):
            new_arr1.append(weights[0][i] + weights[1][j])
            new_arr2.append(weights[2][i] + weights[3][j])

    # 투포인터를 돌기위해 정렬
    new_arr1.sort()
    new_arr2.sort()

    # 투포인터를 돈다.
    s = 0  # 시작포인터
    e = len(new_arr1) - 1  # 끝포인터
    result = new_arr1[s] + new_arr2[e]  # 가장 근접한 카누선수의 몸무게를 출력할 변수
    while s <= len(new_arr1) - 1 and e >= 0:

        if new_arr1[s] + new_arr2[e] == k:
            result = new_arr1[s] + new_arr2[e]
            break
        elif abs(k - result) >= abs(k - (new_arr1[s] + new_arr2[e])):
            if abs(k - result) == abs(k - (new_arr1[s] + new_arr2[e])):
                result = min(result, (new_arr1[s] + new_arr2[e]))
            else:
                result = new_arr1[s] + new_arr2[e]

        if new_arr1[s] + new_arr2[e] > k:
            e -= 1
        else:
            s += 1

    print(result)
