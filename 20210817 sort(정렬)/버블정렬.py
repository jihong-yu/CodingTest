array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8, 8, 3]

for i in range(0, len(array)):  # 하나의 인덱스를 기준으로
    for j in range(i + 1, len(array)):  # 그 다음 인덱스부터 비교하여 비교 대상보다 크다면 자리를 바꾼다.
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print(array)
