# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python


def find_even_index(arr):
    index = 0
    while index < len(arr):
        lhs_sum = sum(arr[:index]) or 0
        rhs_sum = sum(arr[index + 1:]) or 0
        if lhs_sum == rhs_sum:
            return index
        index += 1
    return -1
