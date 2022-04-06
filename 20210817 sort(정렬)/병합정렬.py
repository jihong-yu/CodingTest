import sys

sys.stdin = open('input.txt', 'r')


def merge_sort(arr):

    # 원소가 하나밖에없으면 바로 리턴
    if len(arr) <= 1:
        return arr

    # 절반 나눈다
    mid = len(arr) // 2

    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    # 병합
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    # 끝났다면은 나머지는 무조건 뒤에붙이기만 하면된다
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr


T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
