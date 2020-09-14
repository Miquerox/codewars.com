# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python


def solution(number):
    result = 0
    for n in range(0, number):
        if n % 3 == 0 or n % 5 == 0:
            result += n
    return result
